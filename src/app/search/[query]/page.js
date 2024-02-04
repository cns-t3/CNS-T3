import SmallSearchBar from "@/components/SmallSearchBar";
import React from "react";

async function getData(query) {
  const url = "http://127.0.0.1:8000/search?search_query=" + query;
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error("Failed to fetch data");
  }
  return res.json();
}

export default async function Search({ params }) {
  const query = decodeURIComponent(params.query);
  const data = await getData(query);
  const string = JSON.stringify(data);
  return (
    <>
      <div className="flex md:flex-row flex-col m-6 items-center justify-center">
        <img src="/logo.png" className="md:w-2/12 sm:w-1/3 w-1/2 m-3"></img>
        <SmallSearchBar initialValue={query}></SmallSearchBar>
      </div>
    </>
  );
}
