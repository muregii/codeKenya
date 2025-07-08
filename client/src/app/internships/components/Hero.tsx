"use client";

import React from "react";
import Image from "next/image";
import Link from "next/link";
import Button from "@/app/pages/components/Button";
import Navbar from "@/app/pages/components/Navbar";
import { FaStar } from "react-icons/fa6";
import { motion } from "framer-motion";

const Hero = () => {
  const features = [
    {
      icon: <FaStar className="text-2xl text-primary-red-color" />,
      title: "Your preferences",
      description:
        "When you begin your bootcamp, your instructors will introduce you to the available companies and project briefs.",
      className:
        "bg-primary-black-color text-white border border-gray-800 hover:border-gray-700",
      textColor: "text-gray-300",
    },
    {
      icon: <FaStar className="text-2xl text-primary-red-color" />,
      title: "Company matching",
      description:
        "Instructors will match you based on preferences, engagement, performance, collaboration skills, and client industry needs.",
      className: "bg-white text-black hover:shadow-lg",
      textColor: "text-gray-600",
    },
    {
      icon: <FaStar className="text-2xl text-white" />,
      title: "Continuous support",
      description:
        "Teaching Assistants available to support you 24/7 on your internship program. To ensure success in your career.",
      className: "bg-primary-red-color text-white hover:bg-red-600",
    },
    {
      icon: <FaStar className="text-2xl text-white" />,
      title: "Job placement",
      description:
        "Our commitment extends beyond internships – we help you land a job that matches your skills. We support you to the end.",
      className: "bg-primary-green-color text-white hover:bg-green-600",
    },
  ];

  return (
    <div className="min-h-screen bg-primary-black-color text-white relative overflow-hidden">
      <Navbar />

      {/* Background Circle */}
      <motion.div
        initial={{ opacity: 0, scale: 0.8 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 1, ease: "easeOut" }}
        className="absolute top-0 left-0 z-0"
      >
        <motion.div
          animate={{
            rotate: 360,
          }}
          transition={{
            duration: 30,
            repeat: Infinity,
            ease: "linear",
          }}
        >
          <Image
            src="/images/circle-bg.png"
            alt="Green circle"
            height={250}
            width={250}
            className="object-contain"
          />
        </motion.div>
      </motion.div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        {/* Main Hero Section */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 items-center pt-16 md:pt-24">
          {/* Left Text Content */}
          <motion.div
            initial={{ opacity: 0, x: -50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8, ease: "easeOut" }}
            className="space-y-8 max-w-xl mb-12 md:mb-0 text-center md:text-left"
          >
            <motion.h1
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.2 }}
              className="text-4xl md:text-5xl lg:text-6xl font-black leading-tight"
            >
              Explore our internship opportunities
            </motion.h1>

            <motion.p
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.4 }}
              className="text-base md:text-lg text-gray-300"
            >
              Gain invaluable hands-on experience with a secured 4-week
              internship. You&apos;ll work closely with industry professionals,
              collaborate with fellow students, and solve real-world problems.
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
                    title="Get started"
                    variant="btn_red_rounded"
                  />
                </motion.div>
              </Link>
            </motion.div>
          </motion.div>

          {/* Right Image */}
          <motion.div
            initial={{ opacity: 0, x: 50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8, ease: "easeOut" }}
            className="flex justify-end"
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
                src="/images/internships-hero-img.png"
                alt="Student"
                height={600}
                width={600}
                className="w-full max-w-2xl object-contain"
                priority
              />
            </motion.div>
          </motion.div>
        </div>

        {/* Features Grid */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.8 }}
          className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 py-12 md:py-16"
        >
          {features.map((feature, index) => (
            <motion.div
              key={feature.title}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5, delay: 1 + index * 0.1 }}
              whileHover={{ y: -10 }}
              className={`space-y-4 rounded-lg p-6 transition-all ${feature.className}`}
            >
              {feature.icon}
              <h2 className="text-xl font-bold">{feature.title}</h2>
              <p className={feature.textColor || ""}>{feature.description}</p>
            </motion.div>
          ))}
        </motion.div>
      </div>
    </div>
  );
};

export default Hero;
