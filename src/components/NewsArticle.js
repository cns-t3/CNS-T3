"use client";
import React, { useRef, useEffect } from "react";
import Chart from "chart.js/auto";
import ChartDataLabels from "chartjs-plugin-datalabels";

const NewsArticle = ({
  title,
  publishedAt,
  summary,
  score,
  riskRating,
  tag,
  publisher,
}) => {
  const matchChartRef = useRef(null);
  const riskChartRef = useRef(null);

  useEffect(() => {
    const matchCtx = matchChartRef.current.getContext("2d");
    const riskCtx = riskChartRef.current.getContext("2d");

    // Match chart configuration
    const matchConfig = {
      type: "doughnut",
      data: {
        datasets: [
          {
            data: [score, 1 - score],
            backgroundColor: ["#3498db", "transparent"],
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
            display: false, // Hide the labels in the chart
          },
          tooltip: { enabled: false },
          legend: { display: false },
        },
      },
      plugins: [ChartDataLabels],
    };

    // Risk chart configuration
    const riskConfig = {
      type: "doughnut",
      data: {
        datasets: [
          {
            data: [riskRating === "low" ? 1 : 0, riskRating === "low" ? 0 : 1],
            backgroundColor: ["#2ecc71", "transparent"],
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
            display: false, // Hide the labels in the chart
          },
          tooltip: { enabled: false },
          legend: { display: false },
        },
      },
      plugins: [ChartDataLabels],
    };

    // Render charts
    const matchChart = new Chart(matchCtx, matchConfig);
    const riskChart = new Chart(riskCtx, riskConfig);

    // Clean up on unmount
    return () => {
      matchChart.destroy();
      riskChart.destroy();
    };
  }, [score, riskRating]);

  // Format the date
  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString("en-SG", {
      day: "2-digit",
      month: "short",
      year: "numeric",
      timeZone: "Asia/Singapore",
    });
  };

  return (
    <div className="flex justify-between items-center bg-white px-4 py-5 shadow rounded-lg relative">
      <div className="flex-1 pr-3">
        <p className="text-xs font-semibold text-gray-500 border border-gray-300 rounded px-2 py-1 mb-2 block md:hidden w-min">
          {tag}
        </p>
        <p className="text-sky-800 text-xs font-bold uppercase">{publisher}</p>
        <div className="flex items-center flex-row">
          <h2 className="text-xl font-bold text-gray-900 my-1">{title}</h2>
          <p className="text-xs font-semibold text-gray-500 border border-gray-300 rounded px-2 py-1 ml-5 hidden md:block">
            {tag}
          </p>
        </div>
        <p className="text-gray-500 text-sm">
          {formatDate(publishedAt)} — "{summary}"
        </p>
      </div>
      <div className="flex items-center md:space-x-0 space-x-0 relative md:flex-row flex-col ">
        <div className="relative flex flex-col md:pr-3 py-2 md:py-0">
          <canvas ref={matchChartRef} width="80" height="80" />
          <div className="absolute inset-0 flex items-center justify-center">
            <p className="text-center text-gray-900 text-xs md:pr-3">
              <span className="text-sm font-semibold">
                {(score * 100).toFixed(0)}%
              </span>{" "}
              <span className="block text-xs max-w-full overflow-hidden overflow-ellipsis whitespace-nowrap">
                MATCH
              </span>
            </p>
          </div>
        </div>
        <div className="relative flex flex-col items-center py-2 md:py-0">
          <canvas ref={riskChartRef} width="80" height="80" />
          <div className="absolute inset-0 flex items-center justify-center">
            <p className="text-center text-gray-900 text-xs">
              <span className="text-sm font-semibold">
                {riskRating === "low" ? "LOW" : "HIGH"}
              </span>{" "}
              <span className="block text-xs max-w-full overflow-hidden overflow-ellipsis whitespace-nowrap">
                RISK
              </span>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default NewsArticle;
