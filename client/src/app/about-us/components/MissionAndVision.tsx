import React from "react";
import Image from "next/image";

const MissionAndVision = () => {
  return (
    <div className="flex flex-col-reverse md:flex-row justify-between items-center w-[90%] mx-auto gap-8 py-8">
      <div className="w-full md:w-[50%] flex justify-center">
        <Image
          src="/images/mission-and-vision-img.png"
          alt="Website mockup"
          height={500}
          width={500}
          className="w-full max-w-[500px] h-auto"
        />
      </div>

      <div className="w-full md:w-[40%] space-y-8">
        <div className="space-y-4">
          <h1 className="text-primary-green-color text-center md:text-left text-xl font-bold">
            Our Mission
          </h1>
          <p className="text-sm">
            To equip individuals with in-demand coding skills through hands-on
            learning, personalized mentorship, and industry-relevant training,
            while bridging the gap between education and employment through
            strategic partnerships and placement opportunities.
          </p>
        </div>

        <div className="space-y-4">
          <h1 className="text-primary-green-color text-center md:text-left text-xl font-bold">
            Our Vision
          </h1>
          <p className="text-sm">
            To empower aspiring tech professionals across Kenya by providing
            transformative education, fostering innovation, and creating
            pathways to impactful careers in the global tech industry.
          </p>
        </div>
      </div>
    </div>
  );
};

export default MissionAndVision;
