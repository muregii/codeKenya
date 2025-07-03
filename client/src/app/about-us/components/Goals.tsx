import React from "react";

import Image from "next/image";

import {
  FaHeart,
  FaNewspaper,
  FaStar,
  FaGlobe,
  FaClock,
  FaBookmark,
} from "react-icons/fa6";

const Goals = () => {
  return (
    <div className="bg-[#b3b4bdff] py-16">
      <div className="w-[90%] mx-auto">
        <div className="flex flex-col md:flex-row  gap-8 md:gap-80 justify-between">
          <div className="w-full md:w-[30%] space-y-6">
            <h2 className="text-4xl leading-2">The Code Kenya Journey</h2>
            <p>
              Code Kenya is a Kenyan bootcamp that would bridge the gap between
              academia and industry. It&apos;s aims to grow into a global
              operation that will help students accelerate their careers while
              exploring the world.{" "}
            </p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div className="flex items-center gap-4">
              <div className="bg-primary-black-color text-white rounded-md p-4">
                <FaHeart />
              </div>
              <div className="space-y-2">
                <h3 className="text-base font-semibold">First Arrivals</h3>
                <p className="text-xs">
                  The journey of innovation kicks off in 2025 as we welcome our
                  first cohort.
                </p>
              </div>
            </div>

            <div className="flex items-center gap-4">
              <div className="bg-primary-black-color text-white rounded-md p-4">
                <FaNewspaper />
              </div>
              <div className="space-y-2">
                <h3 className="text-base font-semibold">Courses offered</h3>
                <p className="text-xs">
                  We offer courses like data, software, business, banking,
                  design and marketing.
                </p>
              </div>
            </div>

            <div className="flex items-center gap-4">
              <div className="bg-primary-red-color text-white rounded-md p-4">
                <FaStar />
              </div>
              <div className="space-y-2">
                <h3 className="text-base font-semibold">Life Connections</h3>
                <p className="text-xs">
                  We thrive on the close connections between students and
                  mentors.
                </p>
              </div>
            </div>

            <div className="flex items-center gap-4">
              <div className="bg-primary-red-color text-white rounded-md p-4">
                <FaGlobe />
              </div>
              <div className="space-y-2">
                <h3 className="text-base font-semibold">Go global</h3>
                <p className="text-xs">
                  Code Kenya intents to expand its reach, inspired by global
                  successes.
                </p>
              </div>
            </div>

            <div className="flex items-center gap-4">
              <div className="bg-primary-green-color text-white rounded-md p-4">
                <FaClock />
              </div>
              <div className="space-y-2">
                <h3 className="text-base font-semibold">Thrive online</h3>
                <p className="text-xs">
                  We embraces innovation with remote and hybrid programs.
                </p>
              </div>
            </div>

            <div className="flex items-center gap-4">
              <div className="bg-primary-green-color text-white rounded-md p-4">
                <FaBookmark />
              </div>
              <div className="space-y-2">
                <h3 className="text-base font-semibold">Future investment</h3>
                <p className="text-xs">
                  A strategic future investment program, creating pathways for
                  learners to thrive globally.
                </p>
              </div>
            </div>
          </div>
        </div>
        <div className="my-20">
          <h1 className="text-2xl text-center md:text-left">Our goals</h1>
          <div className="my-8 flex flex-col md:flex-row items-stretch w-full">
            <div className="bg-our-goals-bg1 h-48 md:h-auto md:flex-1 md:rounded-l-lg text-white bg-center   bg-no-repeat flex items-end">
              <p className="w-full text-center mx-auto mb-4 text-3xl">
                Travel far
              </p>
            </div>

            <div className="bg-our-goals-bg2 h-48  md:flex-1 text-black bg-center  bg-no-repeat flex items-end">
              <p className="w-full text-center mx-auto mb-4 text-3xl">
                Learn deeply
              </p>
            </div>

            <div className="bg-our-goals-bg3 h-48  md:flex-1 text-white bg-center  bg-no-repeat flex items-end">
              <p className="w-full text-center mx-auto mb-4 text-3xl">
                Connect widely
              </p>
            </div>

            <div className="bg-our-goals-bg4 h-48  md:flex-1  md:rounded-r-lg text-white bg-center  bg-no-repeat flex items-end">
              <p className="w-full text-center mx-auto mb-4 text-3xl">
                Impact widely
              </p>
            </div>
          </div>
        </div>
        <div className="flex flex-col md:flex-row py-8 items-center justify-between">
          <Image
            src="/images/our-purpose-img.JPG"
            alt="Group testing virtual reality"
            width={500}
            height={500}
            className="rounded-md"
            loading="lazy"
            quality={80}
          />
          <div className="space-y-5 w-full my-8 md:w-[50%]">
            <h2 className="text-3xl text-center md:text-left">Our purpose</h2>
            <div className="space-y-4">
              <p className="text-lg">
                Our focus has always been on creating authentic connections
                within our community. We go to great lengths to get to know our
                students, teachers, and partner companies, which we believe has
                been instrumental to our success.
              </p>
              <p className="text-lg">
                Our purpose is brought to life by a dedicated team that embodies
                both the competence and cultural values essential to our
                mission. Over the years, we&apos;ve prioritized building a
                collective of driven individuals who not only excel in their
                fields but also share a deep commitment to pushing boundaries
                and delivering on our promise – to help people go further.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Goals;
