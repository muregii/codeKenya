"use client";

import React from 'react';
import Link from 'next/link';
import { motion } from 'framer-motion';
import { CheckCircle } from 'lucide-react';

const SuccessPage = () => {
  return (
    <div className="h-screen bg-linear-to-b from-primary-green-color/10 to-white flex flex-col justify-between p-6">
      {/* Header */}
      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
        className="text-center max-w-2xl mx-auto mt-12"
      >
        <CheckCircle className="w-16 h-16 text-primary-green-color mx-auto mb-4" />
        <h1 className="text-3xl font-bold text-gray-900 mb-3">
          Application Submitted Successfully!
        </h1>
        <p className="text-lg text-gray-600">
          Thank you for applying to Code Kenya. We&apos;ve received your application and will review it shortly.
        </p>
      </motion.div>

      {/* Footer Buttons */}
      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
        className="flex justify-center gap-4 mb-12"
      >
        {/* <Link 
          href="/dashboard" 
          className="px-6 py-3 text-base font-medium rounded-md text-white bg-primary-green-color hover:bg-green-700 transition-colors"
        >
          Go to Dashboard
        </Link> */}
        <Link 
          href="/" 
          className="px-6 py-3 text-base font-medium rounded-md text-gray-700 bg-white border border-gray-300 hover:bg-gray-50 transition-colors"
        >
          Return Home
        </Link>
      </motion.div>

      {/* Confetti Effect */}
      <div className="fixed top-0 left-0 w-full h-full pointer-events-none">
        {[...Array(20)].map((_, i) => (
          <motion.div
            key={i}
            initial={{
              top: -10,
              left: Math.random() * 100 + '%',
              opacity: 1,
              scale: Math.random() * 0.3 + 0.2,
            }}
            animate={{
              top: '100%',
              opacity: 0,
              transition: {
                duration: Math.random() * 2 + 1,
                delay: Math.random() * 0.5,
                repeat: Infinity,
                repeatDelay: Math.random() * 3,
              }
            }}
            className="absolute w-2 h-2 rounded-full"
            style={{
              background: i % 2 === 0 ? '#34D399' : '#EF4444',
              transform: `rotate(${Math.random() * 360}deg)`,
            }}
          />
        ))}
      </div>
    </div>
  );
};

export default SuccessPage;