import React, { useState, useRef, useEffect } from "react";
import { BiSortAlt2 } from "react-icons/bi";
import SortDropDown from "./SortDropDown";

function SortButton({ selectedSortOption, setSelectedSortOption }) {
  const [sortCardOpen, setSortCardOpen] = useState(false);
  const dropdownRef = useRef();

  function handleClickOutside(event) {
    if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
      setSortCardOpen(false);
    }
  }

  useEffect(() => {
    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, []);

  const handleSortCardOpen = () => {
    setSortCardOpen((isOpen) => !isOpen);
  };

  return (
    <div className="inline-block" id="sortByButton" ref={dropdownRef}>
      <button onClick={handleSortCardOpen} type="button">
        <div className="flex flex-row text-gray-500 pr-5">
          <BiSortAlt2 size={20} />
          <span className="text-sm pl-1">Sort</span>
        </div>
      </button>
      {sortCardOpen && (
        <div className="absolute right-0 bg-white rounded-md border border-gray-200 shadow-lg z-50 w-64 py-2 px-3">
          <form>
            <div className="mx-2 my-2 font-semibold">Sort By</div>
            <SortDropDown
              selectedSortOption={selectedSortOption}
              setSelectedSortOption={setSelectedSortOption}
            />
            <div className="grid grid-cols-2 gap-2 m-2 mt-5" />
          </form>
        </div>
      )}
    </div>
  );
}

export default SortButton;
