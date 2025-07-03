import React from "react";
import Button from "@/app/pages/components/Button";
import Image from "next/image";

const MCBootcamp = () => {
  return (
    <div className="flex flex-col md:flex-row">
      {/* Left Section */}
      <div className="bg-[#b3b4bdff] space-y-8 w-full md:w-[50%] px-[5%] py-[5%] flex flex-col items-center md:items-start text-center md:text-left">
        <h2 className="text-3xl leading-8">Management Consulting Bootcamp</h2>
        <p>
          We know that students need more than just academic knowledge. You
          require practical skills and real-world business experience that
          builds a stand-out resume. This is the perfect opportunity for you to
          gain valuable industry-relevant skills and internship experience in
          Management Consulting either online or while travelling to some of the
          most beautiful destinations in the world.
        </p>
        <Button
          type="button"
          title="Get Started"
          variant="btn_black"
        />
      </div>

      {/* Right Section */}
      <div className="bg-primary-black-color text-white flex flex-col gap-8 px-[5%] py-[5%] w-full md:w-[50%]">
        {/* Card 1 */}
        <div className="space-y-4 flex flex-col items-center md:flex-row md:items-center md:justify-between text-center md:text-left">
          <div className="flex-1">
            <h3 className="text-xl font-semibold">Weeks 1-2</h3>
            <p className="mt-2">
              The first two weeks of the program are dedicated entirely to class
              contact time, allowing you to fully immerse yourself in the course
              material and build a strong foundation for the hands-on
              experiences that follow.
            </p>
          </div>
          <Image
            src="/images/MC-img1.png"
            alt="Laptop"
            height={200}
            width={200}
            className="mt-4 md:mt-0 md:ml-4"
          />
        </div>

        {/* Card 2 */}
        <div className="space-y-4 flex flex-col items-center md:flex-row md:items-center md:justify-between text-center md:text-left">
          <div className="flex-1">
            <h3 className="text-xl font-semibold">Weeks 3-6</h3>
            <p className="mt-2">
              The next four weeks of the program are a dynamic blend of
              internship and class time, giving you the opportunity to apply
              what you&apos;ve learned in real-world settings while continuing
              to enhance your knowledge through ongoing coursework.
            </p>
          </div>
          <Image
            src="/images/MC-img2.png"
            alt="Laptop"
            height={200}
            width={200}
            className="mt-4 md:mt-0 md:ml-4"
          />
        </div>
      </div>
    </div>
  );
};

export default MCBootcamp;
