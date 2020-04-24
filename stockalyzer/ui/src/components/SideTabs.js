import React from "react";
import PropTypes from "prop-types";
import { makeStyles, Tabs, Tab, Typography, Box } from "@material-ui/core";

/**
 * The tabs on the side of the page with a list of stocks
 * Template Source: https://github.com/mui-org/material-ui/blob/master/docs/src/pages/components/tabs/VerticalTabs.js
 */

function TabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <Typography
      component="div"
      role="tabpanel"
      hidden={value !== index}
      id={`vertical-tabpanel-${index}`}
      aria-labelledby={`vertical-tab-${index}`}
      {...other}
    >
      {value === index && <Box p={3}>{children}</Box>}
    </Typography>
  );
}

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.any.isRequired,
  value: PropTypes.any.isRequired
};

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
    backgroundColor: theme.palette.background.paper,
    display: "fixed",
    height: 800,
    width: 270
  },
  tabs: {
    borderRight: `1px solid ${theme.palette.divider}`
  }
}));

export default function VerticalTabs(props) {
  const classes = useStyles();
  const [value, setValue] = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
    props.tabChange(newValue);
  };

  return (
    <div className={classes.root}>
      <Tabs
        orientation="vertical"
        variant="scrollable"
        value={value}
        onChange={handleChange}
        aria-label="Vertical tabs example"
        className={classes.tabs}
      >

        {props.tickers.map( (ticker) => 
          <Tab key = {ticker.id} label = {ticker.company}> </Tab>
        )}

      </Tabs>
    </div>
  );
}