import React from 'react';
import { makeStyles, Link } from '@material-ui/core';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';

/**
 * The media card that displays news information
 * Template Source: https://github.com/mui-org/material-ui/blob/master/docs/src/pages/components/cards/ImgMediaCard.js
 */

const useStyles = makeStyles({
  root: {
    maxWidth: 600,
    width: 600,
  }
});

export default function MediaCard(props) {
  const classes = useStyles();

  return (
    <div style={{paddingTop:20, paddingLeft: 20}}>
    <Card className={classes.root}>
      <CardActionArea>
        <CardContent height="200">
          <Typography gutterBottom variant="h5" component="h2">
            News
          </Typography>
          <Typography variant="body2" color="textSecondary" component="p">
            {props.news.title}
          </Typography>
        </CardContent>
      </CardActionArea>
      <CardActions style={{ paddingTop: 50 }}>
        <Button size="small" color="primary" onClick={props.handleBack} disabled={props.backDisabled}>
          Back
        </Button>
        <Button size="small" color="primary" onClick={props.handleNext} disabled={props.nextDisabled}>
          Next
        </Button>
        <Button size="small" color="primary" component={Link} href={props.news.url} disabled={props.linkDisabled}>
          Learn More
        </Button>
      </CardActions>
    </Card>
    </div>
  );
}
