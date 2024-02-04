import React from "react";

export default function SearchBar({
  searchQuery,
  onSearchChange,
  onSearchSubmit,
}) {
  return (
    <>
      <input
        type="text"
        id="large-input"
        placeholder="who are you searching for?"
        value={searchQuery}
        onChange={(e) => onSearchChange(e.target.value)}
        onKeyDown={onSearchSubmit}
        className="placeholder:text-center block w-3/4 md:w-3/4 lg:w-1/2 p-4 rounded-md  text-gray-700 bg-gray-100  md:text-2xl sm:text-lg text-sm focus:outline-none caret-red-500"
      />
    </>
  );
}
