import React from "react";

import Image from "next/image";

const Ongoing = () => {
  return (
    <div className="bg-[#b3b4bdff]">
      <div className="w-[90%] mx-auto py-16">
        <div className="flex flex-col md:flex-row justify-between">
          <Image
            src="/images/ongoing-bootcamps-img.jpg"
            alt="Virtual Reality testing"
            className="rounded"
            height={400}
            width={400}
          />
          <div className="space-y-4">
            <div className="h-[3px] mt-8 md:mt-0 bg-primary-green-color w-12 justify-left"></div>
            <div className="space-y-6 md:space-y-12">
              <div className="">
                <h2 className="text-primary-green-color text-2xl font-bold">
                  Software Engineering (AI)
                </h2>
                <p className="text-base">
                  Build intelligent systems, develop machine learning models,
                  and create AI-driven solutions.
                </p>
              </div>
              <div className="">
                <h2 className="text-primary-green-color text-2xl font-bold">
                  Entrepreneurship
                </h2>
                <p className="text-base">
                  Turn ideas into businesses, develop innovative strategies, and
                  drive startup success.
                </p>
              </div>
            </div>
          </div>
        </div>
        <h1 className="text-4xl font-bold text-center md:text-left text-primary-green-color py-12">
          Ongoing Bootcamps & internships
        </h1>
        <div className="flex flex-col md:flex-row gap-12  justify-between">
          <div className="bg-SE-bootcamp-img h-48  md:flex-1 bg-center bg-cover rounded-lg  bg-no-repeat flex items-end">
            <p className="w-full text-center bg-white mx-auto rounded-b-lg p-2 font-bold  text-xl">
              Software Engineering
            </p>
          </div>

          <div className="bg-entrepreneurship-bootcamp-img h-48  md:flex-1 bg-center bg-cover rounded-lg  bg-no-repeat flex items-end">
            <p className="w-full text-center bg-primary-red-color text-white mx-auto rounded-b-lg p-2 font-bold  text-xl">
              Entrepreneurship
            </p>
          </div>

          <div className="bg-AI-bootcamp-img h-48  md:flex-1 bg-center bg-cover rounded-lg  bg-no-repeat flex items-end">
            <p className="w-full text-center bg-primary-green-color text-white mx-auto rounded-b-lg p-2 font-bold  text-xl">
              Artificial Intelligence
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Ongoing;
