import React from 'react';
import { makeStyles, Table, TableBody, TableCell, TableContainer, TableRow, Paper } from '@material-ui/core';

// table to display the stock data

const useStyles = makeStyles({
  table: {
    minWidth: 300,
  },
});

export default function SimpleTable(props) {
  const classes = useStyles();

  return (
    <TableContainer component={Paper}>
      <Table className={classes.table} aria-label="simple table">
        <TableBody>
            <TableRow> 
                <TableCell align="left">Yesterclose</TableCell>
                <TableCell align="right">{props.yesterclose}</TableCell>
            </TableRow>
            <TableRow> 
                <TableCell align="left">First Mention</TableCell>
                <TableCell align="right">{props.first_mention}</TableCell>
            </TableRow>
            <TableRow> 
                <TableCell align="left">Last Price</TableCell>
                <TableCell align="right">{props.last_price}</TableCell>
            </TableRow>
            <TableRow> 
                <TableCell align="left">Last Volume</TableCell>
                <TableCell align="right">{props.last_volume}</TableCell>
            </TableRow>
        </TableBody>
      </Table>
    </TableContainer>
  );
}
