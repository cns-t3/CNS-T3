'use client';

import React, { useRef, useEffect, useState } from 'react';
import Chart from 'chart.js/auto';
import ChartDataLabels from 'chartjs-plugin-datalabels';

function RiskRating({ riskRating, riskJustification }) {
  const riskChartRef = useRef(null);
  const [showJustification, setShowJustification] = useState(false);
  const handleMouseEnter = (event) => {
    event.stopPropagation(); // Prevents the click event on the parent element
    setShowJustification(true); // Shows the tooltip
  };

  const handleMouseLeave = (event) => {
    event.stopPropagation(); // Prevents the click event on the parent element
    setShowJustification(false); // Hides the tooltip
  };
  useEffect(() => {
    const riskCtx = riskChartRef.current.getContext('2d');

    // Determine the chart color based on the risk rating
    let chartColor;
    switch (riskRating) {
      case 'Low':
        chartColor = '#2ecc71'; // Green for low risk
        break;
      case 'Medium':
        chartColor = '#f39c12'; // Orange for medium risk
        break;
      case 'High':
        chartColor = '#E60000'; // Red for high risk
        break;
      default:
        chartColor = 'transparent'; // Default case
    }

    // Risk chart configuration
    const riskConfig = {
      type: 'doughnut',
      data: {
        datasets: [
          {
            data: [1],
            backgroundColor: [chartColor],
            borderWidth: 0,
          },
        ],
      },
      options: {
        cutout: '90%',
        rotation: 270,
        circumference: 360,
        plugins: {
          datalabels: {
            display: false,
          },
          tooltip: { enabled: false },
          legend: { display: false },
        },
        onHover: (event, chartElement) => {
          // Show or hide the risk justification tooltip based on hover state
          setShowJustification(chartElement.length > 0);
        },
      },
      plugins: [ChartDataLabels],
    };

    // Render charts
    const riskChart = new Chart(riskCtx, riskConfig);

    // Clean up on unmount
    return () => {
      riskChart.destroy();
    };
  }, [riskRating]);

  return (
    <div className="relative flex flex-col items-center py-2 md:py-0" onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave}>
      <canvas ref={riskChartRef} width="80" height="80" />
      <div className="absolute inset-0 flex items-center justify-center">
        <p className="text-center text-gray-900 text-xs">
          <span className="text-sm font-semibold riskRating">
            {riskRating.toUpperCase()}
          </span>
          {' '}
          <span className="block text-xs max-w-full overflow-hidden overflow-ellipsis whitespace-nowrap">
            RISK
          </span>
        </p>
      </div>
      {/* {showJustification && (
        <div className="absolute z-10 w-auto p-2 bg-white rounded-md shadow-lg 
        text-sm text-gray-700 transform -translate-x-1/2 left-1/2 
        top-full mt-2"
        >
          {riskJustification}
        </div>
      )} */}
    </div>
  );
}

export default RiskRating;
