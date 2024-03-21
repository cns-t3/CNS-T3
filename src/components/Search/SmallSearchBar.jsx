'use client';

import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import { MdOutlineSearch } from 'react-icons/md';

import Spinner from './Spinner';

export default function SmallSearchBar({ initialValue }) {
  const [value, setValue] = useState(initialValue);
  const [isLoading, setIsLoading] = useState(false);
  const router = useRouter();
  const handleChange = (e) => {
    setValue(e.target.value);
  };

  const onSearchSubmit = (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      setIsLoading(true);
      router.push(`/search/${value}`);
    }
  };

  return (
    <div className="w-full md:mx-6 pl-4 border-l-4 border-red">
      <div className="w-full p-4 rounded-md text-gray-700 bg-beige flex justify-between">
        <input
          type="text"
          id="small-input"
          defaultValue={value}
          autoComplete="off"
          onChange={handleChange}
          onKeyDown={onSearchSubmit}
          className="md:text-base text-sm bg-transparent w-4/5 focus:outline-none caret-red-500"
        />
        <div className="w-1/5 flex justify-end items-center">
          {isLoading ? (
            <Spinner />
          ) : (
            <MdOutlineSearch size={25} />
          )}
        </div>
      </div>
    </div>
  );
}
