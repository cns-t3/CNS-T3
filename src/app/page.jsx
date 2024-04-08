import React from 'react';
import Image from 'next/image';
import SearchBar from '@/components/Search/SearchBar';

export default function Home() {
  return (
    <div className="flex flex-col h-screen w-full">
      <div className="h-1/2 flex justify-center items-end">
        <Image
          width={1000}
          height={1000}
          className="md:w-1/4 sm:w-1/3 w-1/2 m-3"
          src="/logo.png"
        />
      </div>
      <div className="h-1/2 w-full items-start flex justify-center">
        <SearchBar />
      </div>
    </div>
  );
}
