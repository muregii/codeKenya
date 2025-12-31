"use client";

import React, { useState } from "react";
import Image from "next/image";

const CommunityThreads = () => {
  const [currentSlide, setCurrentSlide] = useState(0);

  const threads = [
    {
      id: 1,
      title: "Tech Career Fair",
      date: "Aug 30, 2025",
      image: "/images/summit.jpg",
      description:
        "Join us for the upcoming tech career fair with leading companies in Kenya and beyond. Network and explore opportunities.",
    },
    {
      id: 2,
      title: "AI & Machine Learning Meetup",
      date: "Sept 10, 2025",
      image: "/images/AI-img.jpg",
      description:
        "An exciting session for AI enthusiasts. Speakers from top universities and startups will be sharing insights.",
    },
    {
      id: 3,
      title: "Community Spotlight: Kelvin Kemboi",
      date: "August 15, 2025",
      image: "/images/me.jpg",
      description:
        "Kelvin Kemboi, one of our alumni, just started his degree in Computer Science at Colgate University in Hamilton, New York. Read his story.",
    },
    {
      id: 4,
      title: "Hackathon 2025",
      date: "Sept 20, 2025",
      image: "/images/hackathon.jpg",
      description:
        "Code Kenya will host its largest hackathon yet! Register now and be part of 48 hours of coding, innovation, and fun.",
    },
  ];

  const nextSlide = () => {
    setCurrentSlide((prev) => (prev + 1) % threads.length);
  };

  const previousSlide = () => {
    setCurrentSlide((prev) => (prev - 1 + threads.length) % threads.length);
  };

  return (
    <div className="w-full md:max-w-[95%] mx-auto py-8">
      <h2 className="text-2xl font-bold mb-4 text-center text-primary-red-color">
        Community Threads & Events
      </h2>

      <div className="relative overflow-hidden">
        {/* Carousel Wrapper */}
        <div
          className="flex transition-transform duration-500 ease-in-out"
          style={{
            transform: `translateX(-${currentSlide * 100}%)`,
          }}
        >
          {threads.map((item) => (
            <div
              key={item.id}
              className="w-full flex-shrink-0 px-4"
              style={{ flex: "0 0 100%" }} // 👈 ensures each slide takes 100%
            >
              <div className="bg-white rounded-2xl shadow-lg overflow-hidden hover:shadow-xl transition duration-300 max-w-2xl mx-auto">
                <Image
                  src={item.image}
                  alt={item.title}
                  width={800}
                  height={400}
                  className="w-full h-64 object-cover"
                />
                <div className="p-4">
                  <span className="text-sm text-gray-500">{item.date}</span>
                  <h3 className="text-lg font-semibold mt-2 text-primary-green-color">
                    {item.title}
                  </h3>
                  <p className="text-gray-700 mt-2 text-sm">
                    {item.description}
                  </p>
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* Navigation Arrows */}
        <button
          onClick={previousSlide}
          className="absolute left-2 top-1/2 -translate-y-1/2 bg-primary-red-color text-white p-2 rounded-full hover:bg-red-600"
        >
          ◀
        </button>
        <button
          onClick={nextSlide}
          className="absolute right-2 top-1/2 -translate-y-1/2 bg-primary-red-color text-white p-2 rounded-full hover:bg-red-600"
        >
          ▶
        </button>
      </div>

      {/* Dots Navigation */}
      <div className="flex justify-center mt-4 space-x-2">
        {threads.map((_, index) => (
          <button
            key={index}
            onClick={() => setCurrentSlide(index)}
            className={`w-3 h-3 rounded-full ${
              currentSlide === index ? "bg-primary-red-color" : "bg-gray-300"
            }`}
          />
        ))}
      </div>
    </div>
  );
};

export default CommunityThreads;
