import React from "react";
import { Typography } from "@material-ui/core";

/**
 * Header that displays the company name and symbol 
 */

export default function Header(props) {
    return(
        <Typography variant = "h5"> 
            <b>{props.company.name} {"(" + props.company.symbol + ")"}</b>
        </Typography>
    )
}