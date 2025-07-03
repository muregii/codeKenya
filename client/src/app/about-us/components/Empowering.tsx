import React from "react";
import Image from "next/image";

const Empowering = () => {
  return (
    <div className="w-[90%] mx-auto py-8 md:py-16">
      <h1 className="text-primary-green-color text-2xl text-center md:text-left font-bold">
        Empowering potential
      </h1>

      <p className="mt-6 md:mt-8 w-full md:w-[60%] text-base">
        Code Kenya&apos;s story is a story about potential. Ours is a story
        about stretching the limits of what people believe they can do. And
        helping them get there. We mentor them, encourage them, get behind them,
        and believe in them, to stretch the limits of what they think they can
        do.
      </p>

      <div className="h-[3px] my-8 md:mt-8 bg-primary-green-color w-12"></div>

      <div className="flex flex-col md:flex-row gap-12 md:gap-16">
        <div className="space-y-4 md:space-y-6 md:pr-16 md:border-r-2">
          <h2 className="text-primary-green-color text-lg font-bold">
            We enable people with:
          </h2>
          <div className="space-y-3">
            <p className="text-base">Unique education and training</p>
            <p className="text-base">Valuable career-specific knowledge</p>
            <p className="text-base">Reputable internships</p>
            <p className="text-base">Strong alumni network</p>
            <p className="text-base">Practical skills</p>
            <p className="text-base">Transformative experience</p>
          </div>
        </div>

        <div className="w-full md:w-auto flex justify-center">
          <Image
            src="/images/empowerment-img.png"
            alt="Mobile phone"
            height={600}
            width={600}
            className="w-full max-w-[400px] md:max-w-[600px] h-auto object-contain"
          />
        </div>
      </div>
    </div>
  );
};

export default Empowering;
