import React from 'react';
import { render, cleanup } from "@testing-library/react";
import '@testing-library/jest-dom/extend-expect'
import {NewsCard} from "../components";

const news = {
  index: 0,
  title: "Fetching the News",
  url: "Fake News"
};

const backDisabled = true;
const nextDisabled =true;
const linkDisabled = true; 

afterEach(cleanup);

it("renders", () => {
    const {asFragment} = render(<NewsCard 
        news={news} 
        backDisabled={backDisabled} 
        nextDisabled={nextDisabled}
        linkDisabled={linkDisabled}/>);
    expect(asFragment()).toMatchSnapshot(); 
});

//handleNext={this.handleNext}
//handleBack={this.handleBack}