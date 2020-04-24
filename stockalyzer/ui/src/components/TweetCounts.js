import React from 'react';
import { makeStyles, Table, TableBody, TableCell, TableContainer, TableRow, Paper } from '@material-ui/core';

// table to display the tweet count

const useStyles = makeStyles({
  table: {
    minWidth: 300,
  },
});

export default function SimpleTable(props) {
  const classes = useStyles();

  return (
    <div style={{paddingTop:20, paddingBottom:20}}>
    <TableContainer 
      component={Paper} 
      style={{backgroundColor: "#81DAF5"}}>

      <Table 
        className={classes.table} 
        aria-label="simple table">
          
        <TableBody>
            <TableRow style={{width: 1}} > 
                <TableCell align="left"><b>Tweet Count</b></TableCell>
                <TableCell align="right"><b>{props.count}</b></TableCell>
            </TableRow>
        </TableBody>
      </Table>
    </TableContainer>
    </div>
  );
}




