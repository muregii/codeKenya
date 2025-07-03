"use client";

import React, { useState } from "react";
import axios from "axios";

import Link from "next/link";
import Image from "next/image";

import {
  FaYoutube,
  FaLinkedin,
  FaMedium,
  FaInstagram,
  FaGithub,
} from "react-icons/fa6";

import SubscriptionModal from "@/app/pages/components/SubscriptionModal";
const Footer = () => {
  const [email, setEmail] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [showSubscribedPopup, setShowSubscribedPopup] = useState(false);
  const [modalMessage, setModalMessage] = useState("");
  const [isError, setIsError] = useState(false);
  const currentYear = new Date().getFullYear();
  const footerLinks = {
    general: {
      title: "General",
      links: [
        { name: "Internships", path: "/internships" },
        { name: "Tuition", path: "/tuition" },
        { name: "FAQs", path: "/" },
        { name: "Contact us", path: "/contact" },
      ],
    },
    bootcamps: {
      title: "Bootcamps",
      links: [
        { name: "Software Engineering", path: "/" },
        { name: "Entrepreneurship", path: "/" },
        { name: "Our SWE with AI", path: "/" },
      ],
    },
    resources: {
      title: "Resources",
      links: [{ name: "Code Kenya Blog", path: "/blog" }],
    },
    about: {
      title: "About",
      links: [
        { name: "Who we are", path: "/about-us" },
        { name: "Internship partners", path: "/internships" },
      ],
    },
  };

  const legalLinks = [{ name: "Deposit policy", path: "/tuition" }];

  const subscribeHandler = async () => {
    const base_url = process.env.NEXT_PUBLIC_BASE_API_URL;
    setIsLoading(true);
    try {
      if (email) {
        const response = await axios.post(`${base_url}/api/subscribe`, {
          email,
        });
        if (response.status === 200) {
          setModalMessage(
            "Thank you for subscribing to our newsletter. We'll keep you updated with the latest news and updates🥳."
          );
          setIsError(false);
        }
      }
    } catch (error) {
      if (axios.isAxiosError(error) && error.response?.status === 400) {
        setModalMessage(
          "This email has already been used. Please use a different email😥"
        );
      } else {
        setModalMessage(
          "An error occurred. Please try again later or check your internet connection😥."
        );
      }
      setIsError(true);
    }
    setIsLoading(false);
    setShowSubscribedPopup(true);
    setEmail("");
  };

  return (
    <footer className="bg-primary-black-color text-white px-8 py-12">
      {showSubscribedPopup && (
        <SubscriptionModal
          isOpen={showSubscribedPopup}
          onClose={() => setShowSubscribedPopup(false)}
          message={modalMessage}
          isError={isError}
        />
      )}
      {/* Main footer content */}
      <div className="w-full md:w-[90%] mx-auto">
        {/* Logo and navigation links */}
        <div className="grid grid-cols-1 md:grid-cols-5 gap-8 mb-12">
          {/* Logo */}
          <div className="md:col-span-1">
            <Link href="/" className="shrink-0">
              <Image
                src="/images/code-kenya-logo.png"
                alt="Code Kenya Logo"
                height={100}
                width={100}
              />
            </Link>
          </div>

          {/* Navigation Links */}
          {Object.values(footerLinks).map((section) => (
            <div key={section.title}>
              <h3 className="font-semibold mb-4">{section.title}</h3>
              <ul className="space-y-2">
                {section.links.map((link) => (
                  <li key={link.name}>
                    <a
                      href={link.path}
                      className="text-gray-400 hover:text-white text-sm"
                    >
                      {link.name}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        {/* Subscribe section */}
        <div className="flex flex-col md:flex-row justify-between items-center border-t border-b border-gray-800 py-8 mb-8">
          <div className="mb-4 md:mb-0">
            <h3 className="font-semibold">Subscribe</h3>
          </div>
          <div className="flex-1 max-w-md mx-4">
            <div className="flex">
              <input
                type="email"
                name="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Enter your email Address"
                className="w-full px-4 py-2 rounded-l bg-gray-800 text-white"
              />
              <button
                className="bg-white text-black px-6 py-2 rounded-r font-semibold flex items-center justify-center whitespace-nowrap h-auto"
                onClick={subscribeHandler}
                disabled={isLoading}
              >
                {isLoading ? "Subscribing..." : "Subscribe"}
              </button>
            </div>
          </div>
          <div className="flex space-x-4 mt-4 md:mt-0">
            <Link
              href="https://youtube.com/@codekenya-h1v?si=cCMZ-nFJU25NymhN"
              target="_blank"
            >
              <FaYoutube />
            </Link>
            <Link
              href="https://www.linkedin.com/company/codekenya/"
              target="_blank"
            >
              <FaLinkedin />
            </Link>
            <Link href="https://medium.com/@raydon.mbehero" target="_blank">
              <FaMedium />
            </Link>
            <Link
              href="https://www.instagram.com/codekenya2025?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="
              target="_blank"
            >
              <FaInstagram />
            </Link>
            <Link href="https://github.com/muregii/codeKenya" target="_blank">
              <FaGithub />
            </Link>
          </div>
        </div>

        {/* Legal links and copyright */}
        <div className="text-center text-sm text-gray-400">
          <div className="flex flex-wrap justify-center gap-4 mb-4">
            {legalLinks.map((link) => (
              <a key={link.name} href={link.path} className="hover:text-white">
                {link.name}
              </a>
            ))}
          </div>
          <div>{`© ${currentYear} All Rights Reserved`}</div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
