import React from 'react';
import { render, cleanup } from "@testing-library/react";
import '@testing-library/jest-dom/extend-expect'
import {TweetCounts} from "../components";

afterEach(cleanup);

it("renders", () => {
    const {asFragment} = render(<TweetCounts count={10000} change={""}/>);
    expect(asFragment()).toMatchSnapshot(); 
});
