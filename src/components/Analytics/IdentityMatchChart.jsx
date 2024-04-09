'use client';

import React, { useRef, useEffect } from 'react';
import Chart from 'chart.js/auto';
import ChartDataLabels from 'chartjs-plugin-datalabels';

function IdentityMatchChart({
  identityData,
}) {
  const identityChartRef = useRef(null);
  const labels = [
    '0 - 19%',
    '20 - 39%',
    '40 - 59%',
    '60 - 79%',
    '80 - 100%',
  ];
  const rgbColours = [
    'rgb(107 114 128)',
    'rgb(75 85 99)',
    'rgb(55 65 81)',
    'rgb(31 41 55)',
    'rgb(17 24 39)',
  ];

  useEffect(() => {
    const identityCtx = identityChartRef.current.getContext('2d');
    const values = Object.values(identityData);
    const colours = rgbColours.slice(rgbColours.length - values.length);

    const identityConfig = {
      type: 'bar',
      data: {
        labels,
        datasets: [
          {
            data: values,
            backgroundColor: colours,
            hoverBackgroundColor: 'RGB(230, 0, 0)',
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
    <div className="py-2 w-full sm:w-[50%] lg:w-full sm:pr-7 lg:pr-0">
      <div className="text-sm text-textgrey font-semibold py-3">
        Identity Score
      </div>
      <div className="w-full">
        <canvas ref={identityChartRef} className="w-full h-auto" />
      </div>
    </div>
  );
}

export default IdentityMatchChart;
