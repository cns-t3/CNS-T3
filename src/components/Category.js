const Category = ({ categoryDetails }) => {
  return (
    <div className="text-xs font-semibold text-gray-500 border border-gray-300 rounded px-2 py-1 mb-2 block w-fit">
      {categoryDetails}
    </div>
  );
};

export default Category;
