"use client";

import { useRef, useEffect } from "react";
import Chart from "chart.js/auto";
import ChartDataLabels from "chartjs-plugin-datalabels";

const RiskRating = ({ riskRating }) => {
  const riskChartRef = useRef(null);

  useEffect(() => {
    const riskCtx = riskChartRef.current.getContext("2d");

    // Determine the chart color based on the risk rating
    let chartColor;
    switch (riskRating) {
      case "low":
        chartColor = "#2ecc71"; // Green for low risk
        break;
      case "medium":
        chartColor = "#f39c12"; // Orange for medium risk
        break;
      case "high":
        chartColor = "#E60000"; // Red for high risk
        break;
      default:
        chartColor = "transparent"; // Default case
    }

    // Risk chart configuration
    const riskConfig = {
      type: "doughnut",
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
        cutout: "90%",
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
    const riskChart = new Chart(riskCtx, riskConfig);

    // Clean up on unmount
    return () => {
      riskChart.destroy();
    };
  }, [riskRating]);

  return (
    <div className="relative flex flex-col items-center py-2 md:py-0">
      <canvas ref={riskChartRef} width="80" height="80" />
      <div className="absolute inset-0 flex items-center justify-center">
        <p className="text-center text-gray-900 text-xs">
          <span className="text-sm font-semibold riskRating">
            {riskRating.toUpperCase()}
          </span>{" "}
          <span className="block text-xs max-w-full overflow-hidden overflow-ellipsis whitespace-nowrap">
            RISK
          </span>
        </p>
      </div>
    </div>
  );
};

export default RiskRating;
