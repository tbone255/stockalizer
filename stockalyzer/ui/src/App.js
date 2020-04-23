import React, { Component, Fragment } from "react";
import { AppBar, SideTabs, Header, Table, TweetCounts, Graph } from "./components";
import { Grid } from '@material-ui/core/';
import axios from "axios";

export default class extends Component {
  constructor(props) {
    super(props);
    this.handleSearch = this.handleSearch.bind(this);
    this.tabChange = this.tabChange.bind(this);
  }

  state = {
    tickers: [], // tickers from django database
    search: "", // value in the search bar
    symbol: "", 
    company: "",
    count: 0,
    yesterclose: 0,
    first_mention: 0,
    last_price: 0,
    last_volume: 0
    
  };

  // Returns user Search
  handleSearch(event) {
    this.setState({ search: event.target.value });
  }

  // Swap the values in state
  tabChange(newValue){
    this.setState({ search: newValue });
    console.log(this.state.tickers[0].symbol)
    this.setState({ symbol: this.state.tickers[newValue].symbol });
    this.setState({ company: this.state.tickers[newValue].company });
    axios.get("/api/trends/"+newValue).then(res => {
      const trend = res.data;
      this.setState({ count: trend.count })
    })
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

      <Grid container>

        <Grid sm={2}>
          <SideTabs tickers={this.state.tickers} tabChange={this.tabChange} />
        </Grid>

        <Grid> 
          <Header company={this.state.company} symbol={this.state.symbol}/>
          <TweetCounts count={this.state.count} />
          <Table yesterclose={this.state.yesterclose} first_mention={this.state.first_mention} last_price={this.state.last_price} last_volume={this.state.last_volume} />
        </Grid>

        <Grid style={{padding: 20}}>
          <Graph />
        </Grid>

      </Grid>
      
    </Fragment>);
  }
}