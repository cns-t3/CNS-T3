import React from 'react';
import { BiSortAlt2 } from 'react-icons/bi';

function SortButton() {
  return (
    <div className="flex flex-row text-gray-500 pr-5">
      <BiSortAlt2 size={20} />
      <span className="text-sm pl-1">Sort</span>
    </div>
  );
}

export default SortButton;
