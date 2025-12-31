"use client";

import React from 'react';
import Image from "next/image";
import Link from "next/link";
import Button from "@/app/pages/components/Button";
import { motion } from "framer-motion";

const HeroSection = () => {
  return (
    <div className="min-h-screen bg-primary-black-color text-white relative overflow-hidden">

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

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 py-20">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
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
              className="text-5xl md:text-6xl font-bold leading-tight mb-6"
            >
              STAY CONNECTED.<br />
              GROW TOGETHER.
            </motion.h1>

            <motion.p
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.4 }}
              className="text-lg text-gray-300 mb-8 max-w-lg"
            >
              Alumni and students of CodeKenya's Innovation Exchange (IX) program networking across generations
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
                    title="Learn More"
                    variant="btn_green"
                  />
                </motion.div>
              </Link>
            </motion.div>
          </motion.div>

          {/* Right Image Circles */}
          <motion.div
            initial={{ opacity: 0, x: 50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8, ease: "easeOut" }}
            className="flex justify-center"
          >
            {/* image part */ }
              <Image
                src="/images/community1.png"
                alt="Community"
                height={600}
                width={600}
                className="w-full max-w-2xl object-contain"
                priority
              />
          </motion.div>
        </div>
      </div>
    </div>
  );
};

export default HeroSection;
