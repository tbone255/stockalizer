import React, { Component } from 'react';
import Plot from 'react-plotly.js';

export default class extends Component {
  render() {
    return (
      <Plot
        data={[
          {
            x: [1, 2, 3],
            y: [2, 6, 3],
            type: 'scatter',
            mode: 'lines+markers',
            marker: {color: 'red'},
          },
          {type: 'bar', x: [1, 2, 3], y: [2, 5, 3]},
        ]}
        layout={ {width: 640, height: 420, title: 'A Fancy Plot'} }
      />
    );
  }
}