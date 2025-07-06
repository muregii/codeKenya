"use client";

import React, { useState } from "react";
import Image from "next/image";

const SuccessStoriesCarousel = () => {
  const [currentSlide, setCurrentSlide] = useState(0);

  const testimonials = [
    {
      id: 1,
      name: "Francis Iboko Eyanae",
      role: "Northwestern University",
      image: "/images/testimonial_francis.webp",
      testimonial:
        "Joining the work experience support program at Code Kenya was a game-changer for my career. I gained practical skills, valuable mentorship, and the confidence to tackle real-world challenges. The support I received helped me transition smoothly into the professional world.",
    },
    {
      id: 2,
      name: "Godwin Kangor",
      role: "Dartmouth College",
      image: "/images/testimonial_godwin.webp",
      testimonial:
        "The program provided me with invaluable hands-on experience and mentorship that helped launch my career in tech.",
    },
    {
      id: 3,
      name: "Kendi Miriti",
      role: "Duke Kunshan University",
      image: "/images/testimonial_kendi.webp",
      testimonial:
        "Thanks to the comprehensive training and support, I was able to land my dream job in web development.",
    },
  ];

  const nextSlide = () => {
    setCurrentSlide((prev) => (prev + 1) % testimonials.length);
  };

  const previousSlide = () => {
    setCurrentSlide(
      (prev) => (prev - 1 + testimonials.length) % testimonials.length
    );
  };

  return (
    <div className="w-full md:max-w-[90%] mx-auto  pt-6">
      <div className="relative flex items-center justify-center">
        {/* Previous Student Shadow */}
        <div className="hidden md:block absolute left-0 w-64 h-96 bg-primary-green-color opacity-50 rounded-lg transform -translate-x-32 scale-75">
          <Image
            src={
              testimonials[
                (currentSlide - 1 + testimonials.length) % testimonials.length
              ].image
            }
            alt="Previous student"
            className="w-full h-full object-cover rounded-lg opacity-50"
            width={200}
            height={200}
          />
        </div>

        {/* Current Student */}
        <div className="relative w-64 md:w-96 z-10">
          <div className="relative">
            <Image
              src={testimonials[currentSlide].image}
              alt={testimonials[currentSlide].name}
              className="w-full rounded-lg shadow-xl"
              width={200}
              height={200}
            />
            <div className="absolute top-4 right-4">
              <span className="bg-primary-red-color text-white px-3 py-1 rounded-full text-sm">
                Testimonial
              </span>
            </div>
          </div>

          <div className="mt-6 max-w-xl mx-auto text-center">
            <p className="text-gray-800 mb-4 italic">
              &quot;{testimonials[currentSlide].testimonial}&quot;
            </p>
            <h3 className="text-primary-red-color text-2xl font-bold">
              {testimonials[currentSlide].name}
            </h3>
            <p className="text-gray-600">{testimonials[currentSlide].role}</p>
          </div>
        </div>

        {/* Next Student Shadow */}
        <div className="hidden md:block absolute right-0 w-64 h-96 bg-primary-green-color opacity-50 rounded-lg transform translate-x-32 scale-75">
          <Image
            src={testimonials[(currentSlide + 1) % testimonials.length].image}
            alt="Next student"
            className="w-full h-full object-cover rounded-lg opacity-50"
            width={200}
            height={200}
          />
        </div>

        {/* Navigation Buttons */}
        <button
          onClick={previousSlide}
          className="absolute left-0 md:-left-4 top-1/2 transform -translate-y-1/2 bg-primary-red-color text-white p-2 rounded-full hover:bg-red-600 transition-colors duration-200"
          aria-label="Previous slide"
        >
          <svg
            className="w-6 h-6"
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
        </button>

        <button
          onClick={nextSlide}
          className="absolute right-0 md:-right-4 top-1/2 transform -translate-y-1/2 bg-primary-red-color text-white p-2 rounded-full hover:bg-red-600 transition-colors duration-200"
          aria-label="Next slide"
        >
          <svg
            className="w-6 h-6"
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
    </div>
  );
};

export default SuccessStoriesCarousel;
