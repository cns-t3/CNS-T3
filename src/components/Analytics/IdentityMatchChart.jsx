'use client';

import React, { useRef, useEffect } from 'react';
import Chart from 'chart.js/auto';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import LegendLabel from './LegendLabel';

function IdentityMatchChart({
  identityData,
}) {
  const identityChartRef = useRef(null);
  const labels = ["0 - 19%", "20 - 39%", "40 - 59%", "60 - 79%", "80 - 100%"]
  const rgbColours = [
    'rgb(252 165 165)',
    'rgb(248 113 113)',
    'rgb(239 68 68)',
    'rgb(220 38 38)',
    'rgb(185 28 28)',
    'rgb(153 27 27)',
    'rgb(127 29 29)',
  ];
  const twColours = [
    'darkestRed',
    'darkerRed',
    'darkRed',
    'mediumRed',
    'lightRed',
    'lighterRed',
    'lightestRed',
  ];

  useEffect(() => {
    const identityCtx = identityChartRef.current.getContext('2d');
    const values = Object.values(identityData);
    const colours = rgbColours.slice(rgbColours.length - values.length);

    const identityConfig = {
      type: 'bar',
      data: {
        datasets: [
          {
            data: values,
            backgroundColor: colours,
            borderColor: colours,
            barThickness: 6,
            borderWidth: 0,
            minBarLength: 1,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
        plugins: {
          datalabels: {
            display: false,
          },
          tooltip: { enabled: false },
          legend: { display: false },
        },
      },
      plugins: [ChartDataLabels],
    };

    // Render charts
    const identityChart = new Chart(identityCtx, identityConfig);

    // Clean up on unmount
    return () => {
      identityChart.destroy();
    };
  }, [identityData]);

  return (
    <div className="py-2">
      <div className="text-sm text-textgrey font-semibold py-3">
        Identity Score
      </div>
      <div className="w-full">
        <canvas ref={identityChartRef} />
      </div>
      <div>
        <div className="flex flex-row">
          <LegendLabel label={labels[0]} colour={twColours[0]} />
          <LegendLabel label={labels[1]} colour={twColours[1]} />
          <LegendLabel label={labels[2]} colour={twColours[2]} />
        </div>
        <div className="flex flex-row">
          <LegendLabel label={labels[3]} colour={twColours[3]} />
          <LegendLabel label={labels[4]} colour={twColours[4]} />
        </div>
      </div>
    </div>
  );
}

export default IdentityMatchChart;
