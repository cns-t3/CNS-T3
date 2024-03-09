'use client';

import React, { useRef, useEffect } from 'react';
import Chart from 'chart.js/auto';
import ChartDataLabels from 'chartjs-plugin-datalabels';

function IdentityMatching({ score }) {
  const identityMatchingChartRef = useRef(null);

  useEffect(() => {
    const identityMatchingCtx = identityMatchingChartRef.current.getContext('2d');

    // Match chart configuration
    const matchConfig = {
      type: 'doughnut',
      data: {
        datasets: [
          {
            data: [score, 1 - score],
            backgroundColor: ['#5B5D5C', 'transparent'],
            borderWidth: 0,
          },
        ],
      },
      options: {
        cutout: '90%',
        rotation: 270,
        circumference: 270,
        plugins: {
          datalabels: {
            display: false, // Hide the labels in the chart
          },
          tooltip: { enabled: false },
          legend: { display: false },
        },
      },
      plugins: [ChartDataLabels],
    };
    // Render charts
    const identityMatchingChart = new Chart(identityMatchingCtx, matchConfig);

    // Clean up on unmount
    return () => {
      identityMatchingChart.destroy();
    };
  }, [score]);

  return (
    <div className="relative flex flex-col md:pr-3 py-2 md:py-0" id="identityMatching">
      <canvas ref={identityMatchingChartRef} width="80" height="80" />
      <div className="absolute inset-0 flex items-center justify-center">
        <p className="text-center text-gray-900 text-xs md:pr-3">
          <span className="text-sm font-semibold identityMatching">
            {score.toFixed(0)}
            %
          </span>
          {' '}
          <span className="block text-xs max-w-full overflow-hidden overflow-ellipsis whitespace-nowrap">
            MATCH
          </span>
        </p>
      </div>
    </div>
  );
}

export default IdentityMatching;
