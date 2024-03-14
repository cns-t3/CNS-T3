import React from 'react';

async function getData() {
  const url = 'http://127.0.0.1:8002/news/anthony%20tan';
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

export default async function test() {
  const data = await getData();

  return <div><pre>{JSON.stringify(data, null, 2)}</pre></div>;
}
