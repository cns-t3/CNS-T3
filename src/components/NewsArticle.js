"use client";
import React, { useRef, useEffect } from "react";
// import Chart from "chart.js/auto";
// import ChartDataLabels from "chartjs-plugin-datalabels";

const NewsArticle = ({ articleDetails }) => {
  // const matchChartRef = useRef(null);
  // const riskChartRef = useRef(null);

  // useEffect(() => {
  //   const matchCtx = matchChartRef.current.getContext("2d");
  //   const riskCtx = riskChartRef.current.getContext("2d");

  //   // Match chart configuration
  //   const matchConfig = {
  //     type: "doughnut",
  //     data: {
  //       datasets: [
  //         {
  //           data: [articleDetails.score, 1 - articleDetails.score],
  //           backgroundColor: ["#5B5D5C", "transparent"],
  //           borderWidth: 0,
  //         },
  //       ],
  //     },
  //     options: {
  //       cutout: "90%",
  //       rotation: 270,
  //       circumference: 360,
  //       plugins: {
  //         datalabels: {
  //           display: false, // Hide the labels in the chart
  //         },
  //         tooltip: { enabled: false },
  //         legend: { display: false },
  //       },
  //     },
  //     plugins: [ChartDataLabels],
  //   };

  //   // Risk chart configuration
  //   const riskConfig = {
  //     type: "doughnut",
  //     data: {
  //       datasets: [
  //         {
  //           data: [
  //             articleDetails.risk_rating === "low" ? 1 : 0,
  //             articleDetails.risk_rating === "low" ? 0 : 1,
  //           ],
  //           backgroundColor: ["#2ecc71", "transparent"],
  //           borderWidth: 0,
  //         },
  //       ],
  //     },
  //     options: {
  //       cutout: "90%",
  //       rotation: 270,
  //       circumference: 360,
  //       plugins: {
  //         datalabels: {
  //           display: false, // Hide the labels in the chart
  //         },
  //         tooltip: { enabled: false },
  //         legend: { display: false },
  //       },
  //     },
  //     plugins: [ChartDataLabels],
  //   };

  //   // Render charts
  //   const matchChart = new Chart(matchCtx, matchConfig);
  //   const riskChart = new Chart(riskCtx, riskConfig);

  //   // Clean up on unmount
  //   return () => {
  //     matchChart.destroy();
  //     riskChart.destroy();
  //   };
  // }, [articleDetails]);

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
    <div
      id="news-article-container"
      className="flex justify-between items-center bg-white px-4 py-5 shadow rounded-lg relative my-5"
    >
      <div className="flex-1 pr-3">
        <p
          id="article-tag"
          className="text-xs font-semibold text-gray-500 border border-gray-300 rounded px-2 py-1 mb-2 block md:hidden w-min"
        >
          {articleDetails.tag}
        </p>
        <p
          id="article-publisher"
          className="text-sky-800 text-xs font-bold uppercase"
        >
          {articleDetails.publisher}
        </p>
        <div className="flex items-center flex-row">
          <h2
            id="article-title"
            className="text-xl font-bold text-gray-900 my-1"
          >
            {articleDetails.title}
          </h2>
          <p
            id="article-tag-hidden"
            className="text-xs font-semibold text-gray-500 border border-gray-300 rounded px-2 py-1 ml-5 hidden md:block"
          >
            {articleDetails.tag}
          </p>
        </div>
        <p id="article-summary" className="text-gray-500 text-sm line-clamp-2">
          {formatDate(articleDetails.publishedAt)} — "{articleDetails.summary}"
        </p>
      </div>
      {/* <div className="flex items-center md:space-x-0 space-x-0 relative md:flex-row flex-col ">
        <div className="relative flex flex-col md:pr-3 py-2 md:py-0">
          <canvas ref={matchChartRef} width="80" height="80" />
          <div className="absolute inset-0 flex items-center justify-center">
            <p className="text-center text-gray-900 text-xs md:pr-3">
              <span className="text-sm font-semibold">
                {(articleDetails.score * 100).toFixed(0)}%
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
                {articleDetails.risk_rating.toUpperCase()}
              </span>{" "}
              <span className="block text-xs max-w-full overflow-hidden overflow-ellipsis whitespace-nowrap">
                RISK
              </span>
            </p>
          </div>
        </div>
      </div> */}
    </div>
  );
};

export default NewsArticle;
