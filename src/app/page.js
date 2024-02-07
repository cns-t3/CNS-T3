"use client";
import Image from "next/image";
import { useEffect, useState } from "react";
import axios from "axios";

export default function Home() {
  const [data1, setData] = useState([]);

  useEffect(() => {
    axios
      .get("http://10.0.142.62:8000/news/tim%20cook")
      .then((response) => {
        console.log(response); // Check the response structure
        setData(response.data); // Set the state with response.data
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);
  return (
    <main className="">
      <button>test</button>
      {data1?.map((item, index) => (
        <p key={index}>{item.title}</p>
      ))}

    </main>
  );
}
