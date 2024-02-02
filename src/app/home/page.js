import SearchBar from "@/components/SearchBar";
import Image from "next/image";

export default function Home() {
  return (
    <div className="flex h-screen justify-center items-center">
      <div className="w-full flex-col flex justify-center items-center">
        <Image src="/logo.png" width={350} height={300} className="m-4"></Image>
        <SearchBar></SearchBar>
      </div>
    </div>
  );
}
