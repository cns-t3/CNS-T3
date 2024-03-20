'use client';

import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import Image from 'next/image';
import SearchBar from '@/components/Search/SearchBar';

export default function Home() {
  const [search, setSearch] = useState('');
  const [similarPeople, setSimilarPeople] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const router = useRouter();

  async function getSimilarPeople(input) {
    const personDNS = process.env.NEXT_PUBLIC_PERSON_DNS || '127.0.0.1';
    const url = `http://${personDNS}:8001/person/similar_search/?name=${input}`;
    try {
      const res = await fetch(url, { cache: 'no-store' });
      if (!res.ok) {
        throw new Error('Failed to fetch data');
      }
      return res.json();
    } catch {
      return [];
    }
  }

  const handleSearchChange = (value) => {
    setSearch(value);
    setSimilarPeople(getSimilarPeople(value));
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
          className="md:w-1/4 sm:w-1/3 w-1/2 m-3"
          src="/logo.png"
        />
        <SearchBar
          searchQuery={search}
          onSearchChange={handleSearchChange}
          onSearchSubmit={handleSearchSubmit}
          similarPeople={similarPeople}
          loading={isLoading}
        />
      </div>
    </div>
  );
}
