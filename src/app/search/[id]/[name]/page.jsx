import React from 'react';
import Image from 'next/image';
import Result from '@/components/Result/Result';
import SmallSearchBar from '@/components/Search/SmallSearchBar';

async function getData(id) {
  const searchDNS = process.env.NEXT_PUBLIC_SEARCH_DNS || '127.0.0.1';
  const url = `http://${searchDNS}:8000/search?person_id=${id}`;
  try {
    const res = await fetch(url, { cache: 'no-store' });
    if (!res.ok) {
      throw new Error('Failed to fetch data');
    }
    return res.json();
  } catch {
    return null;
  }
}

export default async function Search({ params }) {
  const id = decodeURIComponent(params.id);
  const name = decodeURIComponent(params.name);
  const data = await getData(id);

  return (
    <div>
      <div className=" w-full flex md:flex-row flex-col p-6 pb-3 items-center md:items-start justify-center top-0 left-0 right-0 fixed">
        <a href="/" className="w-1/3 lg:w-1/6 justify-self-center" id="logoLink" aria-label="Home">
          <Image
            layout="responsive"
            width={700}
            height={700}
            className="m-3"
            src="/logo.png"
          />
        </a>
        <SmallSearchBar initialValue={name} />
      </div>
      <div className="flex md:flex-row flex-col p-6 pt-0 items-center justify-center" />
      {data === null ? (
        <p className="m-6 fixed top-[160px] md:top-[110px] right-0 left-0">
          No Results Found
        </p>
      ) : <Result data={data} />}
    </div>
  );
}
