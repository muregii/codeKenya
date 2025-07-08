import React from "react";
import Image from "next/image";
import Button from "@/app/pages/components/Button";

const BootcampClass = () => {
  return (
    <div className="w-[90%] mx-auto flex flex-col md:flex-row gap-10 py-12">
      {/* Text Section */}
      <div className="w-full md:w-[50%] order-1 md:order-2">
        <h1 className="text-3xl font-bold text-center md:text-left text-primary-green-color py-8">
          Bootcamp skills class
        </h1>
        <p className="mb-6 text-center md:text-left">
          Intensive, personalized training designed to prepare you for
          real-world success in a 4-week internship.
        </p>
        <div className="flex justify-center md:justify-start mb-8">
          <Button type="button" title="Explore" variant="btn_red" />
        </div>
        <div className="space-y-6">
          <div className="flex flex-col items-start">
            <h2 className="font-bold text-3xl text-[#b3b4bdff] mr-4">01</h2>
            <p>
              Your classes are capped at 40 students to maximize individual
              attention.
            </p>
          </div>
          <div className="flex flex-col items-start">
            <h2 className="font-bold text-3xl text-[#b3b4bdff] mr-4">02</h2>
            <p>45+ hours of live taught classes and homework.</p>
          </div>
          <div className="flex flex-col items-start">
            <h2 className="font-bold text-3xl text-[#b3b4bdff] mr-4">03</h2>
            <p>
              This sets each student up for success in your 4-week internship.
            </p>
          </div>
        </div>
      </div>

      {/* Image Section */}
      <div className="w-full md:w-[50%] order-2 md:order-1 flex justify-center">
        <Image
          src="/images/bootcamp-class.png"
          alt="Ongoing Bootcamp Class"
          height={500}
          width={500}
          className="object-contain rounded-lg shadow-lg"
        />
      </div>
    </div>
  );
};

export default BootcampClass;
