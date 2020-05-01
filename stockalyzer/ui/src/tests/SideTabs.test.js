import React from 'react';
import { render, cleanup } from "@testing-library/react";
import '@testing-library/jest-dom/extend-expect'
import {SideTabs} from "../components";

const tickers = [];

afterEach(cleanup);

it("renders", () => {
    const {asFragment} = render(<SideTabs tickers={tickers} />);
    expect(asFragment()).toMatchSnapshot(); 
});