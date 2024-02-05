import Image from "next/image";

const Profile = ({ profileDetails }) => {
  return (
    <div className="col-span-1 bg-beige p-8">
      <div className="grid grid-cols-2 gap-5 ">
        <div className="w-48 h-96">
          <Image
            src={profileDetails.img_url}
            alt="Profile image"
            width={150}
            height={300}
            className="object-cover w-full h-full"
          />
        </div>
        <div>
          <h2 className="text-xl font-bold text-gray-900 my-1">
            {profileDetails.name}
          </h2>
          <p className="text-gray-500 text-sm">
            {profileDetails.occupation}, at {profileDetails.company}
          </p>
          {profileDetails.dob !== "" && (
            <p className="text-gray-500 text-sm">Born: {profileDetails.dob}</p>
          )}
          {profileDetails.nationality !== "" && (
            <p className="text-gray-500 text-sm">
              Nationality: {profileDetails.nationality}
            </p>
          )}
        </div>
      </div>
      <div className="text-sm mt-5">{profileDetails.description}</div>
    </div>
  );
};

export default Profile;
