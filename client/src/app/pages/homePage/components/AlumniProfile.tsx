"use client";

import React, { useState, useEffect } from "react";

import Image from "next/image";

interface Company {
  name: string;
  role: string;
  duration: string;
  location: string;
}

const CareerTimeline = ({ companies }: { companies: Company[] }) => {
  return (
    <div className="space-y-6">
      {companies.map((company, index) => (
        <div key={index} className="flex flex-col">
          <div className="flex justify-between items-start">
            <div>
              <h3 className="text-white text-xl font-semibold">
                {company.name}
              </h3>
              <p className="text-gray-300">{company.role}</p>
            </div>
          </div>
          <div className="text-gray-400 text-sm mt-1">
            <p>{company.duration}</p>
            <p>{company.location}</p>
          </div>
        </div>
      ))}
    </div>
  );
};

const AlumniProfile = () => {
  const [currentSlide, setCurrentSlide] = useState(0);
  const [isAnimating, setIsAnimating] = useState(false);
  const [, setDirection] = useState("next");

  const alumni = [
    {
      id: 1,
      name: "Gabriel Okemwa",
      role: "Software Engineer",
      image: "/images/Okemwa-profile.jpg",
      testimonial:
        "Code Kenya is an amazing opportunity to meet new people, enjoy life in a new area of the world, learn and develop new skills, and try your hand in an industry you did not think you would have the chance to work in.",
      career: [
        {
          name: "Code Kenya",
          role: "Lead Software Engineer",
          duration: "2024 - present",
          location: "Nairobi, Kenya",
        },
        {
          name: "Authelio",
          role: "Software Engineer",
          duration: "2023 - 2024",
          location: "Nairobi, Kenya",
        },
        {
          name: "Apextech",
          role: "Software Engineer", 
          duration: "2021 - 2023",
          location: "Nairobi, Kenya",
        },  
      ],
    },
    {
      id: 2,
      name: "Caleb Kiprono",
      role: "Software Engineer",
      image: "/images/Caleb-profile.jpg",
      testimonial:
        "The program provided me with invaluable hands-on experience and mentorship that helped launch my career in tech.",
      career: [
        {
          name: "Meta",
          role: "Software Engineer",
          duration: "2025 - present",
          location: "Seattle, Washington, United States",
        },
        {
          name: "Meta",
          role: "Software Engineer Intern",
          duration: "2024 - 2024",
          location: "Seattle, Washington, United States",
        },
        {
          name: "Duke University Code+ Program",
          role: "Software Engineer Intern",
          duration: "2023 - 2023",
          location: "United States",
        },
        {
          name: "Equity Bank Limited",
          role: "Relationship Officer",
          duration: "2020 - 2020",
          location: "Nairobi, Kenya",
        },
      ],
    },
  ];

  const nextSlide = () => {
    if (!isAnimating) {
      setIsAnimating(true);
      setDirection("next");
      setCurrentSlide((prev) => (prev + 1) % alumni.length);
    }
  };

  const previousSlide = () => {
    if (!isAnimating) {
      setIsAnimating(true);
      setDirection("prev");
      setCurrentSlide((prev) => (prev - 1 + alumni.length) % alumni.length);
    }
  };

  useEffect(() => {
    const timer = setInterval(() => {
      nextSlide();
    }, 5000);

    return () => clearInterval(timer);
  }, [currentSlide]);

  // Reset animation flag after transition
  useEffect(() => {
    const timer = setTimeout(() => {
      setIsAnimating(false);
    }, 500);

    return () => clearTimeout(timer);
  }, [currentSlide]);

  useEffect(() => {
    const handleKeyDown = (e: { key: string }) => {
      if (e.key === "ArrowLeft") {
        previousSlide();
      } else if (e.key === "ArrowRight") {
        nextSlide();
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, []);

  return (
    <div className="w-full min-h-full my-12 w-full md:w-[90%] mx-auto bg-primary-black-color">
      <div className="max-w-6xl mx-auto p-6">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {/* Left Side - Carousel */}
          <div className="relative bg-primary-black-color/50 rounded-lg p-8 overflow-hidden">
            {/* Pattern Overlay */}
            <div className="absolute top-0 left-0 w-32 h-32 opacity-50">
              <div className="grid grid-cols-8 gap-1">
                {[...Array(64)].map((_, i) => (
                  <div key={i} className="w-1 h-1 bg-white rounded-full" />
                ))}
              </div>
            </div>

            {/* Profile Content */}
            <div
              className={`text-center mt-12 transition-opacity duration-500 ${
                isAnimating ? "opacity-0" : "opacity-100"
              }`}
            >
              <div className="relative w-32 h-32 mx-auto mb-6">
                <div className="absolute inset-0  opacity-20"></div>
                <Image
                  src={alumni[currentSlide].image}
                  alt={alumni[currentSlide].name}
                  className="w-24 h-24 mx-auto object-cover relative z-10"
                  height={100}
                  width={100}
                />
              </div>

              <h2 className="text-white text-2xl font-bold mb-2">
                {alumni[currentSlide].name}
              </h2>
              <p className="text-gray-400 mb-4">{alumni[currentSlide].role}</p>

              <p className="text-gray-300 italic mb-8">
                &quot;{alumni[currentSlide].testimonial}&quot;
              </p>

              <button className="bg-primary-green-color text-white px-6 py-2 rounded-full hover:bg-green-700 transition-colors">
                Connect with Alumni
              </button>

              {/* Navigation */}
              <div className="flex justify-center gap-4 mt-8">
                <button
                  onClick={previousSlide}
                  disabled={isAnimating}
                  className="bg-primary-red-color text-white px-4 py-1 rounded-sm hover:bg-red-600 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
                >
                  <svg
                    className="w-4 h-4"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M15 19l-7-7 7-7"
                    />
                  </svg>
                  Previous
                </button>
                <button
                  onClick={nextSlide}
                  disabled={isAnimating}
                  className="bg-primary-red-color text-white px-4 py-1 rounded-sm hover:bg-red-600 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
                >
                  Next
                  <svg
                    className="w-4 h-4"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M9 5l7 7-7 7"
                    />
                  </svg>
                </button>
              </div>

              {/* Slide Indicators */}
              <div className="flex justify-center gap-2 mt-4">
                {alumni.map((_, index) => (
                  <button
                    key={index}
                    onClick={() => {
                      if (!isAnimating) {
                        setIsAnimating(true);
                        setDirection(index > currentSlide ? "next" : "prev");
                        setCurrentSlide(index);
                      }
                    }}
                    className={`w-2 h-2 rounded-full transition-all ${
                      currentSlide === index
                        ? "bg-primary-red-color w-4"
                        : "bg-gray-400"
                    }`}
                    aria-label={`Go to slide ${index + 1}`}
                  />
                ))}
              </div>
            </div>
          </div>

          {/* Right Side - Career Progress */}
          <div className="bg-linear-to-b from-primary-red-color to-primary-green-color rounded-lg p-8">
            <h2 className="text-white text-3xl font-bold mb-8">
              From campus to career
            </h2>
            <CareerTimeline companies={alumni[currentSlide].career} />
          </div>
        </div>
      </div>
    </div>
  );
};

export default AlumniProfile;
