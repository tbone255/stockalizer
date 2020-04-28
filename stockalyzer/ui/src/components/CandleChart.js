import React from "react";
import ReactApexChart from "react-apexcharts";

const options = {
  chart: {
    type: 'candlestick',
    height: 350
  },
  title: {
    text: 'OHLC',
    align: 'left'
  },
  xaxis: {
    type: 'datetime'
  },
  yaxis: {
    tooltip: {
      enabled: true
    }
  }
}

export default function (props) {
  
  return (
<div id="chart">
<ReactApexChart options={options} series={props.series} type="candlestick" height={"350"} />
</div>
  );
}
