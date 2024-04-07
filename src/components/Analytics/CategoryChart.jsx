'use client';

import React, { useRef, useEffect } from 'react';
import Chart from 'chart.js/auto';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import LegendLabel from './LegendLabel';

function CategoryChart({
  categoryData,
}) {
  const categoryChartRef = useRef(null);
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
    'bg-darkestRed',
    'bg-darkerRed',
    'bg-darkRed',
    'bg-mediumRed',
    'bg-lightRed',
    'bg-lighterRed',
    'bg-lightestRed',
  ];

  useEffect(() => {
    const categoryCtx = categoryChartRef.current.getContext('2d');
    const values = Object.values(categoryData);
    const colours = rgbColours.slice(rgbColours.length - values.length);

    const categoryConfig = {
      type: 'doughnut',
      data: {
        datasets: [
          {
            data: values,
            backgroundColor: colours,
            borderWidth: 0,
          },
        ],
      },
      options: {
        cutout: '55%',
        rotation: 270,
        circumference: 360,
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
    const categoryChart = new Chart(categoryCtx, categoryConfig);

    // Clean up on unmount
    return () => {
      categoryChart.destroy();
    };
  }, [categoryData]);

  return (
    <div className="py-2">
      <div className="text-sm text-textgrey font-semibold py-3">
        Category
      </div>
      <div className="grid grid-cols-2 space-x-5">
        <div>
          <canvas ref={categoryChartRef} />
        </div>
        <div className="flex flex-col">
          {Object.keys(categoryData).map((label, index) => (
            <LegendLabel key={label} label={label} colour={twColours[index]} />
          ))}
        </div>
      </div>
    </div>
  );
}

export default CategoryChart;
