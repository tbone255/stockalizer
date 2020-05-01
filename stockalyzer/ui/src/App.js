import React, { Component } from "react";
import { AppBar, SideTabs, Header, Table, TweetCounts, CandleChart, NewsCard, LineChart } from "./components";
import { Grid } from '@material-ui/core/';
import axios from "axios";

export default class extends Component {
  constructor(props) {
      super(props);
      this.menuHandler = this.menuHandler.bind(this);
      this.handleSearch = this.handleSearch.bind(this);
      this.tabChange = this.tabChange.bind(this);
      this.handleNext = this.handleNext.bind(this);
      this.handleBack = this.handleBack.bind(this);
  }

  state = {
    series: [], // Data pass into the graph 
    series2: [], // Data pass into the line graph
    tabIndex: 0, // Index of the current tab
    tickers: [], // The current tickers in the tab
    company:{ // current company being displayed 
      symbol: "Loading", // stock symbol 
      name: "Loading", // company name
    },

    info: {
      marketcap: 0,
      peratio: 0,
      nextEarningsDay: 0,
      employees: 0,
      float: 0, 
      ttmeps: 0,
      week52Change: 0,
      week52Low: 0,
      week52High: 0
    },

    tweetCounts: 0, 
    tweetChange: 0,

    // current news being displayed 
    recentNews: [], // most recent news
    news:{
      index: 0,
      title: "Fetching the News",
      url: "Fake News"
    },

    searchColor: "white", // color of the text in the search bar
    backDisabled: true, // disables the back button on the news card
    nextDisabled: true, // disables the next button on the news card
    linkDisabled: true // disables the link on the news card 
  }
// ----------------------------------------------------------------------------------------------------
  // Given a ticker, update the name and symbol displayed 
  updateCompany(ticker){
    this.setState(prev => ({
      company: {
        ...prev.company,
        symbol: ticker.symbol,
        name: ticker.company
      }
    }))
  }

  // Given a ticker id, get trends and update related variables 
  updateTrends(id){
    axios.get("/api/tickers/" + id + "/trends/")
      .then(res=> {
        // if there is a response
        if (res.data.length > 0){
          this.setState({ tweetCounts: res.data[res.data.length-1].count,  // set tweet counts to most recent 
                          recentNews: res.data[res.data.length-1].news,  // set news to the most recent 
                          backDisabled:true});
            // if there is a previous trend
            if (res.data.length > 1){
              var change = res.data[res.data.length-1].count-res.data[res.data.length-2].count;
              if (change !== 0 && res.data[res.data.length-1].count === 0){
                change = change * 100;
                this.setState({ tweetChange: change});
              }
              // Make sure we don't divide by zero 
              if (change !== 0){
                this.setState({ tweetChange: ( Math.round(change/res.data[res.data.length-2].count * 10) / 10)});
              }
              else{
                this.setState({ tweetChange: 0});
              }
            }
            else {
              var change2 = 0-res.data[res.data.length-1].count;
              // Make sure todays count isn't zero
              if (change2 !== 0){
                change2 = change2*100;
                this.setState({ tweetChange: change2 });
              }
              else{
                this.setState({ tweetChange: 0});
              }
            }
          // Check for news 
          if (this.state.recentNews.length > 0){
            this.setState(prev => ({
              news: {
                ...prev.news,
                title: this.state.recentNews[0].news.title, // set news title
                url: this.state.recentNews[0].news.url, // set url
                index: 0 // reset index
              }
            }))
            // check if there is more than 1 news item 
            if (this.state.recentNews.length > 1){
              this.setState({nextDisabled: false, linkDisabled: false}); // enable link and next button
            }
            else{
              this.setState({nextDisabled: true, linkDisabled: false}); // disable next button and enable link
            }
          }
          // there was no news
          else{
            this.setState({nextDisabled: true, linkDisabled: true}); // disable next button and link
            this.setState(prev => ({ // set news and link to some default variables 
              news: {
                ...prev.news,
                title: "No News Today :(",
                url: "No Link",
                index: 0
              }
            }))

          }
        }
        // there was no response
        else{
          this.setState({tweetCounts: 0, tweetChange: 0, backDisabled:true, nextDisabled: true}); // set tweet counts to 0, disable news
          this.setState(prev => ({ // set news and link to some default variables 
            news: {
              ...prev.news,
              title: "No News Today :(",
              url: "No Link",
              index: 0
            }
          }))
        }
      })
  }

  // get the graph data and update 
  updateGraph(id){
    axios.get("/api/tickers/" + id + "/graph_data/")
      .then(res => {
        this.processData(res.data);
      }).catch((error) => {
        this.setState({series: []})
      })
  }

  updateInfo(id){
    axios.get("/api/tickers/" + id + "/price_info/")
      .then(res => {
        this.setState(prev => ({
          info: {
            ...prev.info,
              marketcap: res.data.marketcap,
              peratio: res.data.peRatio,
              nextEarningsDay: res.data.nextEarningsDate,
              employees: res.data.employees,
              float: res.data.float, 
              ttmeps: res.data.ttmEPS,
              week52Change: res.data.week52change,
              week52Low: res.data.week52high,
              week52High: res.data.week52low
          }
        }))
      }).catch((error) => {
        this.setState(prev => ({
          info: {
            ...prev.info,
              marketcap: "",
              peratio: "",
              nextEarningsDay: "",
              employees: "",
              float: "",
              ttmeps: "",
              week52Change: "",
              week52Low: "",
              week52High: "",
          }
        }))
      })
  }

  // Update the entire page given a ticker
  updatePage(ticker){
    this.updateCompany(ticker);
    this.updateTrends(ticker.id);
    this.updateGraph(ticker.id);
    this.updateInfo(ticker.id)
  }

// ----------------------------------------------------------------------------------------------------
  // Handles a search on the searchbar
  handleSearch(event) {
    this.setState({searchColor: "white"}); // reset text color  to white on any interaction 
    if (event.keyCode === 13){ // check if enter key was hit
      axios.get("/api/tickers/?search="+event.target.value.toUpperCase()) 
        .then(response => { 
          // if results are found 
          if (response.data.length > 0){
            var TopResults = [];
            // only get first 10 search result 
            for(let i=0; i<response.data.length; i++){
              if (i === 10){
                break;
              }
              TopResults.push(response.data[i]);
            }
            this.updatePage(TopResults[0]); // update the page with the top search result 
            this.setState({tickers: TopResults, tabIndex: 0}); // update tickers and set the tab index back to zero
          }
          // no results were found, set the text color to red 
          else{
            this.setState({searchColor: "red"})
          }
        })
    }
  }
// ----------------------------------------------------------------------------------------------------
  // Handles a tab change 
  tabChange(newValue){
    // Return if clicking on the same tab
    if (newValue === this.state.tabIndex){
      return;
    }
    this.setState({tabIndex: newValue}); // Update the tab index 
    this.updatePage(this.state.tickers[newValue]); // Update the page with info on the new ticker 
  }
  menuHandler(){
    this.componentDidMount();
  }
// ----------------------------------------------------------------------------------------------------

  handleBack(){
    // enable the next botton if next element is not the last element 
    if (this.state.news.index === this.state.recentNews.length-1){
      this.setState({ nextDisabled: false})
    }
    // diable the back button if next element is 0
    if (this.state.news.index-1 === 0){
      this.setState({ backDisabled: true})
    }
    this.setState(prev => ({
      news: {
        ...prev.news,
        title: this.state.recentNews[this.state.news.index-1].news.title,
        url: this.state.recentNews[this.state.news.index-1].news.url,
        index: this.state.news.index - 1
      }
    }))
  }
  handleNext(){
    // enable the back button if next index is not 0
    if (this.state.news.index === 0){
      this.setState({ backDisabled: false})
    }
    // disable the next button if next index is the last element 
    if (this.state.news.index+2 === this.state.recentNews.length){
      this.setState({ nextDisabled: true})
    }
    // update news 
    this.setState(prev => ({
      news: {
        ...prev.news,
        title: this.state.recentNews[this.state.news.index+1].news.title,
        url: this.state.recentNews[this.state.news.index+1].news.url,
        index: this.state.news.index + 1
      }
    }))
  }
// ----------------------------------------------------------------------------------------------------
  // Take all the data format it for the graph
  processData(Data){
    var data = [];
    var vwap = [];
    var BB_U = [];
    var BB_L = [];
    var BB_M = [];
    var MA_5 = [];
    var MA_15 = [];
    var Open = [];
    var High = [];
    var Low = [];
    var Close = [];
    for (let [key, value] of Object.entries(Data.Date)){
      var y = [];
      y.push(
        Data.Open[key].toString(), Data.High[key].toString(), Data.Low[key].toString(), Data.Close[key].toString());
      var x = new Date(value.slice(0,4), value.slice(5,7), value.slice(8,10));
      data.push({x, y}); // candlestick data
      vwap.push({x: x.getTime(), y: Data.VWAP[key]});  
      BB_U.push({x: x.getTime(), y: Data.BB_U[key]});  
      BB_L.push({x: x.getTime(), y: Data.BB_L[key]});  
      BB_M.push({x: x.getTime(), y: Data.BB_M[key]}); 
      MA_5.push({x: x.getTime(), y: Data.MA_5[key]}); 
      MA_15.push({x: x.getTime(), y: Data.MA_15[key]}); 
      Open.push({x: x.getTime(), y: Data.Open[key]}); 
      High.push({x: x.getTime(), y: Data.High[key]}); 
      Low.push({x: x.getTime(), y: Data.Low[key]}); 
      Close.push({x: x.getTime(), y: Data.Close[key]}); 
    }
    var newSeries = [];
    newSeries.push({data});
    var newSeries2 = [];
    newSeries2.push({name: "VWAP",data: vwap});
    newSeries2.push({name: "BB U",data: BB_U});
    newSeries2.push({name: "BB L",data: BB_L});
    newSeries2.push({name: "BB M",data: BB_M});
    newSeries2.push({name: "MA 5",data: MA_5});
    newSeries2.push({name: "MA 15",data: MA_15});
    newSeries2.push({name: "Open",data: Open});
    newSeries2.push({name: "High",data: High});
    newSeries2.push({name: "Low",data: Low});
    newSeries2.push({name: "Close",data: Close});
    this.setState({series: newSeries, series2: newSeries2})
  }
// ----------------------------------------------------------------------------------------------------
  // Setup page with top tickers 
  componentDidMount() {
    // Get the top tickers from django
    axios.get("/api/trends/top")
        .then(res => {
          const topTrends = res.data;
          var topTickers = [];
          
          if (topTickers.length != 0){
            axios.all([
              axios.get("/api/tickers/"+topTrends[0].ticker_id),
              axios.get("/api/tickers/"+topTrends[1].ticker_id),
              axios.get("/api/tickers/"+topTrends[2].ticker_id),
              axios.get("/api/tickers/"+topTrends[3].ticker_id),
              axios.get("/api/tickers/"+topTrends[4].ticker_id)
            ]).then(res => {
              topTickers.push(res[0].data);
              topTickers.push(res[1].data);
              topTickers.push(res[2].data);
              topTickers.push(res[3].data);
              topTickers.push(res[4].data);
              this.setState({tickers: topTickers});
              this.updatePage(topTickers[0])
            })
          }
    });
  }
// ----------------------------------------------------------------------------------------------------
  render(){
    return(
      <div>
        <Grid container spacing={2} >
          <Grid item xs={12}>
            <AppBar 
              handleSearch={this.handleSearch}
              color={this.state.searchColor}
              menuHandler={this.menuHandler}/>
          </Grid>
          <Grid item xs={6} sm={3}>
            <SideTabs tickers={this.state.tickers} tabChange={this.tabChange} index={this.tabIndex}/>
          </Grid>
          <Grid item xs={6} sm={3}>
            <Header company={this.state.company}/>
            <TweetCounts count={this.state.tweetCounts} change={this.state.tweetChange}/>
            <Table info={this.state.info}/>
          </Grid>
          <Grid item xs={12} sm={6}>
            <LineChart series={this.state.series2}/>
            <CandleChart series={this.state.series}/> 
            <NewsCard 
              news={this.state.news} 
              handleNext={this.handleNext}
              handleBack={this.handleBack}
              backDisabled={this.state.backDisabled} 
              nextDisabled={this.state.nextDisabled}
              linkDisabled={this.state.linkDisabled}/>
          </Grid>
        </Grid>
        </div>
    )
  }

}