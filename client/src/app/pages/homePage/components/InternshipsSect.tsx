import React from "react";

import Image from "next/image";
import Link from "next/link";
import { FaArrowRight } from "react-icons/fa6";

const InternshipsSect = () => {
  const students = [
    {
      id: 1,
      name: "Kevin Limo",
      role: "Software Engineering Intern",
      type: "Intern",
      image: "/images/SE-intern.png",
    },
    {
      id: 2,
      name: "Sylvia Muli",
      role: "Artificial Intelligence Intern",
      type: "Student",
      image: "/images/AI-intern.png",
    },
  ];

  interface StudentCardProps {
    name: string;
    role: string;
    type: string;
    image: string;
  }

  const StudentCard = ({ name, role, type, image }: StudentCardProps) => {
    return (
      <div className="relative max-w-sm rounded-lg overflow-hidden group">
        {/* Image Container with Overlay */}
        <div className="relative h-64 w-full overflow-hidden">
          <div className="absolute inset-0 bg-green-900/60 z-10"></div>
          <Image
            src={image}
            alt={name}
            className="w-full h-full object-cover"
            width={200}
            height={200}
          />
        </div>

        {/* Content */}
        <div className="absolute bottom-0 left-0 right-0 py-4 z-20">
          <h3 className="text-xl font-semibold md:text-black text-white mb-1">
            {name}
          </h3>
          <p className="md:text-black text-white text-sm mb-3">{role}</p>

          {/* Tags */}
          <div className="flex items-center justify-between">
            <span className="bg-white/20 rounded-full text-white md:text-black text-sm">
              {type}
            </span>
            <button className="px-3 py-1 bg-primary-green-color hover:bg-green-700 transition-colors rounded-full text-white text-sm flex items-center gap-2">
              Connect
            </button>
          </div>
        </div>
      </div>
    );
  };

  return (
    <div className="py-24">
      <div className="flex flex-col md:flex-row justify-between w-[90%] mx-auto">
        <div className="w-full md:max-w-[30%] space-y-6">
          <Image
            src="/images/internship-project-img.JPG"
            alt="Internship video"
            className="rounded-lg"
            height={400}
            width={400}
          />
          <div>
            <h3 className="font-bold text-xl">Internship takeaways</h3>
            <p className="text-base">
              As part of your experience at Code Kenya, you&apos;ll work on a
              real-world project with a group of other students, guided by your
              instructor and project manager.
            </p>
          </div>
          <div className="flex justify-center md:justify-start">
            <Link href='/internships'>
              <button className="flex items-center gap-3 rounded-md bg-primary-green-color hover:bg-green-600 px-8 py-3 text-white">
                Learn more about internships <FaArrowRight />
              </button>
            </Link>
          </div>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-6">
          {students.map((student) => (
            <StudentCard
              key={student.id}
              name={student.name}
              role={student.role}
              type={student.type}
              image={student.image}
            />
          ))}
        </div>
      </div>
    </div>
  );
};

export default InternshipsSect;
