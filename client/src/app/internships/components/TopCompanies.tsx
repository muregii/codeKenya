import React from "react";

import { FaMapPin } from "react-icons/fa6";

interface CompanyCardProps {
  companyName: string;
  location: string;
  openPositions: number;
  isFeatured: boolean;
}

const CompanyCard = ({
  companyName,
  location,
  openPositions,
  isFeatured,
}: CompanyCardProps) => {
  return (
    <div className="bg-white rounded-lg p-4 shadow-xs hover:shadow-md transition-all border border-gray-100">
      <div className="flex items-start gap-3">
        {/* Company Logo */}
        <div className="w-12 h-12 bg-pink-500 rounded-lg flex items-center justify-center">
          <svg
            className="w-8 h-8 text-white"
            viewBox="0 0 24 24"
            fill="currentColor"
          >
            <path d="M12 0C5.372 0 0 5.372 0 12s5.372 12 12 12 12-5.372 12-12S18.628 0 12 0zm5.885 14.615c-.113.237-.361.352-.598.238-2.126-1.031-4.706-1.27-7.082-.693-.246.062-.492-.1-.554-.346-.061-.246.101-.492.347-.554 2.724-.668 5.619-.393 8.027.808.238.114.353.361.239.598l-.379-.051zm1.558-3.467c-.141.285-.452.422-.737.281-2.432-1.181-6.142-1.524-9.026-.832-.375.088-.744-.146-.832-.518-.087-.375.146-.744.518-.832 3.274-.795 7.349-.433 10.16.949.285.141.422.452.281.737l-.364.215zm.134-3.622C16.53 6.048 9.625 5.894 5.676 6.703c-.446.092-.894-.192-.987-.638-.092-.446.192-.894.638-.987 4.469-.916 11.978-.741 16.71 1.134.361.153.532.562.379.923-.152.361-.562.532-.923.379l.084-.086z" />
          </svg>
        </div>

        <div className="flex-1">
          {/* Company Info */}
          <div className="flex items-start justify-between">
            <div>
              <h3 className="font-medium text-gray-900">{companyName}</h3>
              <div className="flex items-center gap-1 text-gray-500 text-sm mt-1">
                <FaMapPin size={14} />
                <span>{location}</span>
              </div>
            </div>
            {isFeatured && (
              <span className="text-xs px-2 py-1 rounded-full bg-red-100 text-red-600 font-medium">
                Featured
              </span>
            )}
          </div>

          {/* Open Positions */}
          <div className="mt-4">
            <div className="bg-green-50 text-green-700 py-2 px-3 rounded-md text-sm font-medium text-center">
              Open Position ({openPositions})
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

const TopCompanies = () => {
  const companies = [
    {
      companyName: "Google Inc.",
      location: "Nairobi, Kenya",
      openPositions: 3,
      isFeatured: true,
    },
    {
      companyName: "Microsoft Inc.",
      location: "Nairobi, Kenya",
      openPositions: 1,
      isFeatured: true,
    },
    {
      companyName: "Safaricom PLC",
      location: "Nairobi, Kenya",
      openPositions: 4,
      isFeatured: true,
    },
    {
      companyName: "Little Cab",
      location: "Nairobi, Kenya",
      openPositions: 2,
      isFeatured: true,
    },
    {
      companyName: "Bolt",
      location: "Nairobi, Kenya",
      openPositions: 3,
      isFeatured: true,
    },
    {
      companyName: "Zeraki",
      location: "Nairobi, Kenya",
      openPositions: 1,
      isFeatured: true,
    },
  ];
  return (
    <div className="w-[90%] mx-auto">
      <h1 className="text-2xl">Top Companies</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 my-8">
        {companies.map((company, index) => (
          <CompanyCard key={index} {...company} />
        ))}
      </div>
    </div>
  );
};

export default TopCompanies;
