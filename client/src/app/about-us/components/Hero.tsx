import React from "react";

import Navbar from "@/app/pages/components/Navbar";
import Button from "@/app/pages/components/Button";
import Link from "next/link";

const Hero = () => {
  return (
    <div className="bg-about-sect-hero-bg-img h-screen bg-cover bg-no-repeat bg-center">
      <Navbar />
      <div className="w-[90%] mx-auto flex items-start h-full">
        <div className="w-full md:w-[30%] bg-linear-to-b from-primary-black-color to-transparent text-white rounded-lg mt-16 space-y-6 p-7 shadow-lg">
          <p>✦ About us</p>
          <h1 className="text-5xl font-bold">Who we are</h1>
          <p>
            codeKenya is a student organization that seeks to promote learning,
            professional experience, adventure, cultural exchange, connection
            building and impact in colleges around the world through a
            distinctive, experiential 7-week summer program in SWE, Data
            Science, Data Analytics, Entrepreneurship & other in-demand skills
            that launch the careers of our clients.
          </p>
          <div>
            <Link href="/apply">
              <Button type="button" title="Enroll now" variant="btn_green" />
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Hero;
