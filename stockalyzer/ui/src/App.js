import React, { Component, Fragment } from "react";
import { AppBar, SideTabs, Header, Table, TweetCounts, Graph, NewsCard } from "./components";
import { Grid } from '@material-ui/core/';
import axios from "axios";

export default class extends Component {
  constructor(props) {
    super(props);
    this.handleSearch = this.handleSearch.bind(this);
    this.tabChange = this.tabChange.bind(this);
    this.handleNext = this.handleNext.bind(this);
    this.handleBack = this.handleBack.bind(this);
  }

  state = {
    tickers: [], // tickers from django database
    search: "", // value in the search bar

    // information on the stock
    symbol: "", 
    company: "",
    count: 0,
    yesterclose: 0,
    first_mention: 0,
    last_price: 0,
    last_volume: 0,
    
    backDisabled: true, // disable back button at start 
    nextDisabled: false, // check that there are articles first 
    newsIndex: 0, 
    newsTitles: ["iPhone SE: A powerful new smartphone in a popular design", "Apple Aims to Sell Macs With Its Own Chips Starting in 2021"],
    newsUrls: ["https://www.apple.com/newsroom/2020/04/iphone-se-a-powerful-new-smartphone-in-a-popular-design/", "https://www.bloomberg.com/news/articles/2020-04-23/apple-aims-to-sell-macs-with-its-own-chips-starting-in-2021"]
    
  };

  // User Search (search bar)
  handleSearch(event) {
    this.setState({ search: event.target.value });
  }

  // Swap the values in state
  tabChange(newValue){
    // search for the ticker in state
    this.setState({ symbol: this.state.tickers[newValue].symbol });
    this.setState({ company: this.state.tickers[newValue].company });

    // get trends for the new ticker (use newValue for now)
    axios.get("/api/trends/"+newValue).then(response => {
      const trend = response.data;
      this.setState({ count: trend.count })
    })

  }

  handleNext(){
    // enable the back button if next index is not 0
    if (this.state.newsIndex === 0){
      this.setState({ backDisabled: false})
    }
    // disable the next button if next index is the last element 
    if (this.state.newsIndex+2 === this.state.newsTitles.length){
      this.setState({ nextDisabled: true})
    }
    this.setState({ newsIndex: this.state.newsIndex + 1})
  }

  handleBack(){
    // enable the next botton if next element is not the last element 
    if (this.state.newsIndex === this.state.newsTitles.length-1){
      this.setState({ nextDisabled: false})
    }
    // diable the back button if next element is 0
    if (this.state.newsIndex-1 === 0){
      this.setState({ backDisabled: true})
    }
    this.setState({ newsIndex: this.state.newsIndex - 1})
  }

  // get tickers from django 
  componentDidMount() {
    axios.get("/api/tickers")
        .then(res => {
        const tickers = res.data;
        this.setState({ tickers });
        // Set the symbol and company to that of the first element in array
        this.setState({ symbol: tickers[0].symbol });
        this.setState({ company: tickers[0].company });
    });
  }

  render() {
    return ( <Fragment>
       
      <AppBar handleSearch={this.handleSearch} />

      <Grid container wrap={"nowrap"}>

        <Grid item sm={2}>
          <SideTabs tickers={this.state.tickers} tabChange={this.tabChange} />
        </Grid>

        <Grid> 
          <Header company={this.state.company} symbol={this.state.symbol}/>
          <TweetCounts count={this.state.count} />
          <Table yesterclose={this.state.yesterclose} first_mention={this.state.first_mention} last_price={this.state.last_price} last_volume={this.state.last_volume} />
        </Grid>

        <Grid style={{padding: 20}}>
          <Graph />
          <NewsCard 
            titles={this.state.newsTitles} 
            urls={this.state.newsUrls}
            index={this.state.newsIndex} 
            handleNext={this.handleNext} 
            handleBack={this.handleBack} 
            backDisabled={this.state.backDisabled}
            nextDisabled={this.state.nextDisabled}/>
        </Grid>

      </Grid>
    </Fragment>);
  }
}