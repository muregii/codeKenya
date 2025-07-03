import React from "react";

import Button from "../../components/Button";
import Link from "next/link";

const HowCKWorks = () => {
  return (
    <div className="bg-how-CK-works-bg-img  bg-no-repeat bg-center h-full pt-16">
      <div className="w-[90%] mx-auto space-y-8 py-12">
        <h1 className="text-5xl text-center md:text-left font-black text-primary-green-color">
          How Code Kenya Works
        </h1>
        <p className="text-base md:w-[40%] w-full  text-white text-center md:text-left">
          Discover the easy steps and support that make your Code Kenya journey
          a trans-formative experience. From personalized guidance to networking
          opportunities, learn how we set you up for success.
        </p>
        <div className="flex justify-center md:justify-start">
          <Link href='/about-us'>
            <Button type="button" title="Learn more" variant="btn_green" />
          </Link>
        </div>
        <div className="flex flex-col md:flex-row justify-between gap-6">
          <div className="rounded-md p-8 bg-white text-black space-y-3">
            <h2 className="font-bold text-3xl">01</h2>
            <p className="text-normal">
              You are guaranteed an internship placement to showcase your skills
              on real-world projects, present to managers, receive feedback and
              give a final presentation.
            </p>
          </div>

          <div className="rounded-md p-8 bg-primary-red-color text-white space-y-3">
            <h2 className="font-bold text-3xl">02</h2>
            <p className="text-normal">
              You&apos;ll not be alone on your Code Kenya journey, with daily
              support from instructors and 24/7 assistance from on-the-ground
              staff you will succeed
            </p>
          </div>

          <div className="rounded-md p-8 bg-primary-green-color text-white space-y-3">
            <h2 className="font-bold text-3xl">03</h2>
            <p className="text-normal">
              Enhance your Linked-In with Code Kenya experience, earn
              recommendations, and connect with successful alumni through the
              Alumni Network.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HowCKWorks;
