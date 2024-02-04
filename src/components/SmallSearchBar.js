"use client";

import React from "react";
import { useState } from "react";
import { useRouter } from "next/navigation";

export default function SmallSearchBar({ initialValue }) {
  const [value, setValue] = useState(initialValue);
  const router = useRouter();
  const handleChange = (e) => {
    setValue(e.target.value);
  };

  const onSearchSubmit = (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      router.push(`/search/${value}`);
    }
  };

  return (
    <>
      <div className="w-full md:m-6 pl-4 border-l-4 border-red-700 flex justify-end items-center">
        <input
          type="text"
          id="large-input"
          defaultValue={value}
          onChange={handleChange}
          onKeyDown={onSearchSubmit}
          className="block w-full p-4 rounded-md  text-gray-700 bg-gray-100 lg:text-2xl md:text-xl sm:text-xs focus:outline-none caret-red-500"
        />
        <img
          src="/search.svg"
          className="absolute mr-2 w-10"
          alt="Search Icon"
        />
      </div>
    </>
  );
}
