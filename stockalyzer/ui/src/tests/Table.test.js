import React from 'react';
import { render, cleanup } from "@testing-library/react";
import '@testing-library/jest-dom/extend-expect'
import {Table} from "../components";

const info = {
    marketcap: 0,
    peratio: 0,
    nextEarningsDay: 0,
    employees: 0,
    float: 0, 
    ttmeps: 0,
    week52Change: 0,
    week52Low: 0,
    week52High: 0
}

afterEach(cleanup);

it("renders", () => {
    const {asFragment} = render(<Table info={info}/>);
    expect(asFragment()).toMatchSnapshot(); 
});