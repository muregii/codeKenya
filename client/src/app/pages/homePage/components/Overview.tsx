import React from "react";
import Button from "../../components/Button";

import Link from "next/link";

const Overview = () => {
  return (
    <div
      id="overview"
      className="flex flex-col md:flex-row justify-between text-black w-[90%] mx-auto py-16"
    >
      <div className="space-y-8 w-full md:w-[40%] mb-12 md:mb-0 text-center md:text-left">
        <h1 className="text-4xl font-black">Overview of the 2025 Program</h1>
        <div className="space-y-4">
          <p className="text-sm">
            Apply early to enjoy exclusive benefits that give you a head start,
            including priority access and premium perks.
          </p>
          <p className="font-semibold">Regular 1 deadline: June 15th 2025.</p>
          <div className="flex justify-center md:justify-start">
            <Link href="/tuition">
              <Button
                type="button"
                title="Explore tuition & financial aid"
                variant="btn_green_rect"
              />
            </Link>
          </div>
        </div>
      </div>

      <div className="flex flex-col md:flex-row justify-between gap-4 items-center">
        <div className="py-16 px-8 space-y-4 bg-overview-bg-img1  md:rounded-b-full text-white bg-center bg-no-repeat flex flex-col items-center justify-center">
          <h2 className="font-bold text-xl">Nairobi Kenya</h2>
          <p className="text-sm">Applications are now open</p>
          <p className="text-xs">Starts from</p>
          <p>June 23rd to August 1st</p>
          <Link href="/bootcamps">
            <Button type="button" title="Learn more" variant="btn_green_rect" />
          </Link>
        </div>
        <div className="py-16 px-8 space-y-4 bg-overview-bg-img2  md:rounded-b-full text-white bg-center bg-no-repeat flex flex-col items-center justify-center">
          <h2 className="font-bold text-xl">Online Program</h2>
          <p className="text-sm">Applications are now open</p>
          <p className="text-xs">Starts from</p>
          <p> June 23rd to August 1st</p>
          <Link href="/bootcamps">
            <Button type="button" title="Learn more" variant="btn_green_rect" />
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Overview;
