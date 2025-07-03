"use client";

import React from "react";
import Navbar from "@/app/pages/components/Navbar";
import Button from "@/app/pages/components/Button";
import Image from "next/image";
import Link from "next/link";
import { motion } from "framer-motion";

const Hero = () => {
  const careerOptions = [
    { title: "Management Consulting", color: "bg-primary-red-color" },
    { title: "Software Development", color: "bg-[#b3b4bdff]" },
    { title: "Investment Banking", color: "bg-[#b3b4bdff]" },
    { title: "Data Science", color: "bg-[#b3b4bdff]" },
  ];

  return (
    <div className="bg-primary-black-color h-full md:h-screen text-white">
      <Navbar />
      <div className="w-[90%] mx-auto py-10 pb-32 md:py-20">
        <div className="flex flex-col justify-between md:flex-row">
          {/* LEFT-TEXT */}
          <motion.div
            initial={{ opacity: 0, x: -50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8, ease: "easeOut" }}
            className="space-y-10 w-full md:w-[50%] mb-12 md:mb-0 text-center md:text-left"
          >
            <motion.h1
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.2 }}
              className="text-5xl font-black"
            >
              Launch Your Tech Career with Code Kenya&apos;s Bootcamp
            </motion.h1>

            <motion.p
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.4 }}
              className="text-base"
            >
              At Code Kenya, we offer an immersive, hands-on bootcamp experience
              designed to equip you with the skills you need to succeed in the
              tech industry both for complete beginners and experts.
            </motion.p>

            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.6 }}
              className="flex justify-center md:justify-start"
            >
              <Link href="/about-us">
                <motion.div
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                >
                  <Button
                    type="button"
                    title="Explore & Apply"
                    variant="btn_green"
                  />
                </motion.div>
              </Link>
            </motion.div>
          </motion.div>

          {/* RIGHT-IMAGE */}
          <motion.div
            initial={{ opacity: 0, x: 50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8, ease: "easeOut" }}
            className="flex justify-center md:justify-end"
          >
            <motion.div
              animate={{
                y: [0, -15, 0],
              }}
              transition={{
                duration: 3,
                repeat: Infinity,
                ease: "easeInOut",
              }}
            >
              <Image
                src="/images/bootcamps-hero-img.png"
                alt="Student"
                height={400}
                width={400}
                className="w-full max-w-[400px] h-auto"
              />
            </motion.div>
          </motion.div>
        </div>

        {/* Career Options */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.8 }}
          className="flex flex-col space-y-4 md:space-y-0 md:flex-row md:justify-between mt-10"
        >
          {careerOptions.map((career, index) => (
            <motion.div
              key={career.title}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.5, delay: 1 + index * 0.1 }}
              whileHover={{ scale: 1.05, x: 10 }}
              className={`${career.color} rounded-l-full py-6 px-10 cursor-pointer`}
            >
              <p>{career.title}</p>
            </motion.div>
          ))}
        </motion.div>
      </div>
    </div>
  );
};

export default Hero;
