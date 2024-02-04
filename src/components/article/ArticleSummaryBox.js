export default function ArticleSum({ article }) {
  return (
    <div className="flex flex-row-reverse"> {/* Reverse the row so the content aligns to the right */}
      <div className="bg-grey-100 shadow-lg rounded-lg p-6 mb-4 w-full lg:w-1/2"> {/* Adjusted width to take half the screen on large screens */}
        {/* Article Header */}
        <div className="flex items-center justify-between">
          <h1 className="text-2xl font-bold text-gray-800">{article.title}</h1>
          {/* <span className="text-sm text-gray-500">
            Published at: {new Date(article.publishedAt).toLocaleDateString()}
          </span> */}
        </div>

        {/* Content */}
        <div className="mt-4">
          <p> Summary:</p>
          <p className="text-gray-600 whitespace-pre-wrap">{article.summary}</p> {/* Use whitespace-pre-wrap to maintain formatting */}
        </div>

        {/* Read More Link */}
        <div className="mt-4">
          <p> Source URL: 
          <a href={article.source_url} target="_blank" rel="noopener noreferrer" className="text-indigo-600 hover:text-indigo-800 transition duration-300 ease-in-out">
            {article.source_url}
          </a>
          </p>
        </div>

        <div className="mt-4">
          <p>Analytics: {article.analytics}</p> {/* Use whitespace-pre-wrap to maintain formatting */}
        </div>
      </div>

      <div className="w-full lg:w-1/2"> {/* This empty div takes up the remaining space */}
        {/* This is where the left side content would go if you have any */}
      </div>
    
    </div>
  );
}
