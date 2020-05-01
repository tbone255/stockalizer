import React from 'react';
import { render, cleanup } from "@testing-library/react";
import '@testing-library/jest-dom/extend-expect'
import {Header} from "../components";

const company = { 
    symbol: "Loading", 
    name: "Loading",
}

afterEach(cleanup);

it("renders", () => {
    const {asFragment} = render(<Header company={company}/>);
    expect(asFragment()).toMatchSnapshot(); 
});
