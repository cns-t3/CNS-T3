import SmallSearchBar from "@/components/SmallSearchBar";
import Image from "next/image";
import React from "react";

export default function Search({ params }) {
  const query = decodeURIComponent(params.query);
  return (
    <>
      <div className="flex md:flex-row flex-col m-6 items-center justify-center">
        <Image
          src="/logo.png"
          width={160}
          height={100}
          alt="logo"
          className="m-4"
        ></Image>
        <SmallSearchBar initialValue={query}></SmallSearchBar>
      </div>
    </>
  );
}
