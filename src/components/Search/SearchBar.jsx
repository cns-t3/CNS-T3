import React from 'react';
import { MdOutlineSearch } from 'react-icons/md';
import Spinner from './Spinner';

export default function SearchBar({
  searchQuery,
  onSearchChange,
  onSearchSubmit,
  loading,
}) {
  return (
    <div className="flex w-4/5 sm:w-3/5 md:w-1/2 justify-end items-center">
      <div className="flex flex-cols w-full p-4 rounded-md text-gray-700 bg-beige space-x-2">
        <MdOutlineSearch size={25} />
        <input
          type="text"
          id="large-input"
          value={searchQuery}
          onChange={(e) => onSearchChange(e.target.value)}
          onKeyDown={onSearchSubmit}
          autoComplete="off"
          className="text-gray-700 bg-transparent md:text-base text-sm focus:outline-none caret-red-500"
        />
      </div>
      {loading ? <Spinner /> : null}
    </div>
  );
}
