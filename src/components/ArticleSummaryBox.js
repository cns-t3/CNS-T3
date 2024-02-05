// export default function ArticleSum({ article }) {
//   return (
//     <div className="flex justify-end"> {/* Content aligns to the right */}
//       <div className="bg-custom-beige shadow-lg rounded-lg p-6 mb-4 w-full lg:w-2/3"> {/* Adjusted width to 2/3 on large screens for ~65% */}
//         {/* Article Header */}
//         <div className="flex items-center justify-between">
//           <h1 className="text-xl font-bold text-gray-800">{article.title}</h1>
//         </div>

//         {/* Summary with smaller font */}
//         <div className="mt-4">
//           <p className="font-semibold">Summary:</p>
//           <p className="text-gray-600 text-sm whitespace-pre-wrap pt-2">{article.summary}</p>
//         </div>

//         {/* Content with a top border as a divider and smaller font */}
//         <div className="mt-4 pt-4 border-t border-blue-300">
//           <p className="text-gray-600 text-sm whitespace-pre-wrap">{article.content}</p>
//         </div>

//         {/* Read More Link */}
//         <div className="mt-4">
//           <p> Source URL:
//             <a href={article.source_url} target="_blank" rel="noopener noreferrer" className="text-indigo-600 hover:text-indigo-800 transition duration-300 ease-in-out">
//               {article.source_url}
//             </a>
//           </p>
//         </div>

//         <div className="mt-4">
//           <p>Analytics: {article.analytics}</p>
//         </div>
//       </div>
//     </div>
//   );
// }

// import { useState } from 'react';

export default function ArticleSum({ article }) {
  // const [isVisible, setIsVisible] = useState(true); // State to manage the visibility of the container
  const isVisible = true;
  // Function to handle closing the container
  const handleClose = () => {
    setIsVisible(false);
  };

  // Return null if the container should not be visible
  // if (!isVisible) return null;

  return (
    <div className="flex justify-end">
      {" "}
      {/* Content aligns to the right */}
      <div className=" w-full">
        {" "}
        {/* Adjusted width to 2/3 on large screens for ~65% */}
        <div className="top-4 left-4">
          {" "}
          {/* Position the back button */}
          <button className="text-gray-600 hover:text-gray-800 transition duration-300 ease-in-out">
            {/* Replace with your own SVG or use a text-based back button */}
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M15 19l-7-7 7-7"
              />
            </svg>
          </button>
          {/* Article Header */}
          <div className="flex items-center justify-between">
            <h1 className="text-xl font-bold text-gray-800">{article.title}</h1>
          </div>
          {/* Summary with smaller font */}
          <div className="mt-4">
            <p className="font-semibold">Summary:</p>
            <p className="text-gray-600 text-sm whitespace-pre-wrap pt-2">
              {article.summary}
            </p>
          </div>
          {/* Content with a top border as a divider and smaller font */}
          <div className="mt-4 pt-4 border-t border-blue-300">
            <p className="text-gray-600 text-sm whitespace-pre-wrap">
              {article.content}
            </p>
          </div>
          {/* Read More Link */}
          <div className="mt-4">
            <p>
              {" "}
              Source URL:
              <a
                href={article.source_url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-indigo-600 hover:text-indigo-800 transition duration-300 ease-in-out"
              >
                {article.source_url}
              </a>
            </p>
          </div>
          <div className="mt-4">
            <p>Analytics: {article.analytics}</p>
          </div>
        </div>
      </div>
    </div>
  );
}
