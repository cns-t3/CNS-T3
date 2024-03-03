const Category = ({ categoryDetails }) => {
  const capitaliseWords = (option) => {
    let capitalizedWords = option
      .split(" ")
      .map((word) => word.charAt(0).toUpperCase() + word.slice(1));
    return capitalizedWords.join(" ");
  };
  return (
    <div
      id="category"
      className="text-xs font-semibold text-gray-500 border border-gray-300 rounded px-2 py-1 mb-2 block w-fit category"
    >
      {capitaliseWords(categoryDetails)}
    </div>
  );
};

export default Category;
