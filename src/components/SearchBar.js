import React from "react";

const SearchBar = () => {
  return (
    <>
      <input
        type="text"
        id="large-input"
        placeholder="who are you searching for?"
        className="placeholder:text-center block w-1/2 p-4 rounded-md text-gray-700 bg-gray-100 lg:text-3xl md:text-2xl sm:text-sm caret-red-500"
      />
    </>
  );
};

export default SearchBar;
