import React from 'react';
import { render, cleanup } from "@testing-library/react";
import '@testing-library/jest-dom/extend-expect'
import {AppBar} from "../components";


afterEach(cleanup);

it("renders", () => {
    const {asFragment} = render(<AppBar />);
    expect(asFragment()).toMatchSnapshot(); 
});