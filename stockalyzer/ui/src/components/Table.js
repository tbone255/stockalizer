import React from 'react';
import { makeStyles, Table, TableBody, TableCell, TableContainer, TableRow, Paper } from '@material-ui/core';

/**
 * Table to display the stock data
 * Template Source: https://github.com/mui-org/material-ui/blob/master/docs/src/pages/components/tables/SimpleTable.js
 */

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
                <TableCell align="left">Marketcap</TableCell>
                <TableCell align="right">{props.info.marketcap}</TableCell>
            </TableRow>
            <TableRow> 
                <TableCell align="left">peRatio</TableCell>
                <TableCell align="right">{props.info.peratio}</TableCell>
            </TableRow>
            <TableRow> 
                <TableCell align="left">Next Earnings Day</TableCell>
                <TableCell align="right">{props.info.nextEarningsDay}</TableCell>
            </TableRow>
            <TableRow> 
                <TableCell align="left">Employees</TableCell>
                <TableCell align="right">{props.info.employees}</TableCell>
            </TableRow>
            <TableRow> 
                <TableCell align="left">Float</TableCell>
                <TableCell align="right">{props.info.float}</TableCell>
            </TableRow>
            <TableRow> 
                <TableCell align="left">ttmEPS</TableCell>
                <TableCell align="right">{props.info.ttmeps}</TableCell>
            </TableRow>
            <TableRow> 
                <TableCell align="left">Week 52 change</TableCell>
                <TableCell align="right">{props.info.week52Change}</TableCell>
            </TableRow>
            <TableRow> 
                <TableCell align="left">Week 52 low</TableCell>
                <TableCell align="right">{props.info.week52Low}</TableCell>
            </TableRow>
            <TableRow> 
                <TableCell align="left">Week 52 high</TableCell>
                <TableCell align="right">{props.info.week52High}</TableCell>
            </TableRow>

        </TableBody>
      </Table>
    </TableContainer>
  );
}
