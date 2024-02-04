"use client";
import SearchBar from "@/components/SearchBar";
import { useState } from "react";
import { useRouter } from "next/navigation";

export default function Home() {
  const [search, setSearch] = useState("");
  const router = useRouter();
  const handleSearchChange = (value) => {
    setSearch(value);
  };
  const handleSearchSubmit = (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      router.push(`/search/${search}`);
    }
  };

  return (
    <div className="flex h-screen justify-center items-center">
      <div className="w-full flex-col flex justify-center items-center">
        <img src="/logo.png" className="sm:w-1/3 w-1/2 m-3"></img>
        <SearchBar
          searchQuery={search}
          onSearchChange={handleSearchChange}
          onSearchSubmit={handleSearchSubmit}
        ></SearchBar>
      </div>
    </div>
  );
}
