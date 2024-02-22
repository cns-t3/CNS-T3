'use client';

import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import Image from 'next/image';
import SearchBar from '@/components/Search/SearchBar';

export default function Home() {
  const [search, setSearch] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const router = useRouter();
  const handleSearchChange = (value) => {
    setSearch(value);
  };
  const handleSearchSubmit = (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      setIsLoading(true);
      router.push(`/search/${search}`);
    }
  };

  return (
    <div className="flex h-screen justify-center items-center">
      <div className="w-full flex-col flex justify-center items-center">
        <Image
          width={1000}
          height={1000}
          className="sm:w-1/3 w-1/2 m-3"
          src="/logo.png"
        />
        <SearchBar
          searchQuery={search}
          onSearchChange={handleSearchChange}
          onSearchSubmit={handleSearchSubmit}
          loading={isLoading}
        />
      </div>
    </div>
  );
}
