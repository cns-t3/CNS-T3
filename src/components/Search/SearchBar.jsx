'use client';

import React, { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { MdOutlineSearch } from 'react-icons/md';
import Spinner from './Spinner';
import SimilarPeople from './SimilarPeople';

export default function SearchBar() {
  const [search, setSearch] = useState('');
  const [routerStr, setRouterStr] = useState(0);
  const [findPeople, setFindPeople] = useState('');
  const [doSearch, setDoSearch] = useState();
  const [isLoading, setIsLoading] = useState(false);
  const router = useRouter();

  const handleSearchChange = (value) => {
    setSearch(value);
  };
  const handleSearchSubmit = (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      setIsLoading(true);
      setFindPeople(true);
    }
  };

  useEffect(() => {
    if (doSearch) {
      router.push(`/search/${routerStr}`);
    }
  }, [doSearch]);

  return (
    <div className="w-full">
      <div className="w-full flex items-center justify-center">
        <div className="flex w-4/5 sm:w-3/5 md:w-1/2 justify-end items-center">
          <div className="flex flex-cols w-full p-4 rounded-md text-gray-700 bg-beige space-x-2">
            <MdOutlineSearch size={25} />
            <input
              type="text"
              id="large-input"
              value={search}
              onChange={(e) => handleSearchChange(e.target.value)}
              onKeyDown={handleSearchSubmit}
              autoComplete="off"
              className="text-gray-700 bg-transparent w-full text-base focus:outline-none caret-red-500"
            />
          </div>
          {isLoading ? <Spinner /> : null}
        </div>
      </div>
      <div className="flex justify-center">
        <SimilarPeople
          query={search}
          setRouterStr={setRouterStr}
          findPeople={findPeople}
          setFindPeople={setFindPeople}
          setDoSearch={setDoSearch}
          setIsLoading={setIsLoading}
          isSmall={false}
        />
      </div>
    </div>
  );
}
