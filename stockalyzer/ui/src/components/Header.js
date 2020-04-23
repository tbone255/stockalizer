import React from "react";
import { Typography } from "@material-ui/core";

// Header that displays the company name and symbol 
export default function Header(props) {
    return(
        <div style={{ padding:20}} > 
            <Typography variant = "h5"> 
                <b>
                    {props.company} {"(" + props.symbol + ")"}
                </b>
            </Typography>
        </div>
    )
}