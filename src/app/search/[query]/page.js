import React from "react";
import NewsArticle from "../../../components/NewsArticle";
import Profile from "@/components/Profile";

const SearchPage = () => {
  const json = {
    profile: {
      person_id: 456,
      name: "Tim Cook",
      occupation: "CEO",
      dob: "1960-11-01",
      nationality: "American",
      description:
        "Tim Cook is a distinguished business leader known for his role as the CEO of Apple Inc., a position he assumed in 2011 following the iconic Steve Jobs. Cook's professional trajectory is marked by his strategic vision, operational prowess, and commitment to innovation. Renowned for his disciplined management style and focus on sustainability, Cook has steered Apple through significant milestones, including the launch of groundbreaking products like the iPhone X and the Apple Watch. Under his stewardship, Apple has expanded its global footprint, diversified its product offerings, and emphasized corporate social responsibility initiatives. Cook's leadership is characterized by a blend of foresight, integrity, and a relentless drive for excellence, making him a pivotal figure in the tech industry.",
      company: "Apple Inc.",
      img_url:
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Visit_of_Tim_Cook_to_the_European_Commission_-_P061904-946789.jpg/1024px-Visit_of_Tim_Cook_to_the_European_Commission_-_P061904-946789.jpg",
    },
  };
  return (
    <div className="grid grid-cols-3">
      <div className="col-span-2"></div>

      <Profile profileDetails={json.profile} />
    </div>
  );
};

export default SearchPage;
