import React from "react";
import Image from "next/image";
import Link from "next/link";
import Button from "@/app/pages/components/Button";

const SummerInternship = () => {
  return (
    <div className="w-[90%] mx-auto py-16 flex flex-col lg:flex-row gap-12 lg:gap-16 justify-between items-center">
      {/* Left Image */}
      <div className="shrink-0">
        <Image
          src="/images/your-internship-headline.png"
          alt="Your summer internship"
          height={400}
          width={400}
          className="max-w-full h-auto"
        />
      </div>

      {/* Center Section */}
      <div className="flex flex-col gap-8 items-center lg:items-start">
        <Image
          src="/images/shape-decor.png"
          alt="Decor"
          height={150}
          width={150}
          className="max-w-full h-auto"
        />
        <Link href='/apply'>
          <Button type="button" title="Get started" variant="btn_red" />
        </Link>
      </div>

      {/* Right Content Section */}
      <div className="flex flex-col items-start gap-6 lg:w-[40%]">
        <div className="space-y-6">
          {/* Item 1 */}
          <div className="flex gap-4 items-center">
            <h1 className="font-bold text-3xl text-[#b3b4bdff]">01</h1>
            <div>
              <h2 className="font-bold text-lg">Guaranteed Placement</h2>
              <p>
                You get a guaranteed internship placement for the summer at one
                of our global partner companies.
              </p>
            </div>
          </div>
          {/* Item 2 */}
          <div className="flex gap-4 items-center">
            <h1 className="font-bold text-3xl text-[#b3b4bdff]">02</h1>
            <div>
              <h2 className="font-bold text-lg">Work Experience</h2>
              <p>115+ hours of internship work to add to your resume.</p>
            </div>
          </div>
          {/* Item 3 */}
          <div className="flex gap-4 items-center">
            <h1 className="font-bold text-3xl text-[#b3b4bdff]">03</h1>
            <div>
              <h2 className="font-bold text-lg">Continuous Support</h2>
              <p>
                Your internship is balanced with hands-on work experience
                supported by additional class sessions to cover advanced
                material.
              </p>
            </div>
          </div>
        </div>
        {/* Bottom Image */}
        <div className="self-center lg:self-start">
          <Image
            src="/images/number-card.png"
            alt="Statistics"
            width={200}
            height={200}
            className="max-w-full h-auto"
          />
        </div>
      </div>
    </div>
  );
};

export default SummerInternship;
