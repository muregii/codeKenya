"use client";

import Link from "next/link";
import Image from "next/image";
import { useState, useEffect } from "react";

const Navbar = () => {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 0);
    };
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const toggleMobileMenu = () => {
    setIsMobileMenuOpen(!isMobileMenuOpen);
  };

  useEffect(() => {
    const handleResize = () => {
      if (window.innerWidth >= 768) {
        setIsMobileMenuOpen(false);
      }
    };
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  const navLinks = ["ABOUT US", "BOOTCAMPS", "INTERNSHIPS", "BLOG", "CONTACT", "TUITION"];

  return (
    <nav
      className={`sticky top-0 z-50  bg-primary-black-color text-white transition-all duration-300 ${
        isScrolled ? "shadow-lg" : ""
      }`}
    >
      <div className="w-[90%] mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link href="/" className="shrink-0">
            <Image
              src="/images/code-kenya-logo.png"
              alt="Code Kenya Logo"
              height={100}
              width={100}
            />
          </Link>

          {/* Navigation Items */}
          <div className="hidden md:flex space-x-4">
            {navLinks.map((item) => (
              <Link
                key={item}
                href={`/${item.toLowerCase().replace(" ", "-")}`}
                className="text-white hover:text-gray-300 transition-colors duration-200 ease-in-out"
              >
                {item}
              </Link>
            ))}
          </div>

          {/* Buttons for Desktop */}
          <div className="hidden md:flex items-center space-x-4">
            <Link
              href="/sign-in"
              className="px-4 py-2 rounded-full border border-white text-white hover:bg-white hover:text-black transition-colors duration-200 ease-in-out"
            >
              Sign In
            </Link>
            <Link
              href="/apply"
              className="px-4 py-2 rounded-full bg-white text-primary-green-color hover:bg-gray-200 transition-colors duration-200 ease-in-out"
            >
              Apply Now
            </Link>
          </div>

          {/* Mobile menu button */}
          <button
            className="md:hidden p-2 rounded-md hover:bg-gray-800 transition-colors duration-200"
            onClick={toggleMobileMenu}
            aria-label="Toggle mobile menu"
          >
            {isMobileMenuOpen ? (
              <svg
                className="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
            ) : (
              <svg
                className="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M4 6h16M4 12h16M4 18h16"
                />
              </svg>
            )}
          </button>
        </div>
      </div>

      {/* Mobile menu */}
      <div
        className={`md:hidden transition-all duration-300 ease-in-out ${
          isMobileMenuOpen
            ? "max-h-96 opacity-100"
            : "max-h-0 opacity-0 overflow-hidden"
        }`}
      >
        <div className="px-2 pt-2 pb-3 space-y-3 sm:px-3">
          {navLinks.map((item) => (
            <Link
              key={item}
              href={`/${item.toLowerCase().replace(" ", "-")}`}
              className="block px-3 py-2 rounded-md text-base font-medium text-white hover:bg-gray-800 transition-colors duration-200 ease-in-out"
              onClick={() => setIsMobileMenuOpen(false)}
            >
              {item}
            </Link>
          ))}

          {/* Buttons for Mobile */}
          <div className="space-y-2 px-3 pt-2">
            <Link
              href="/sign-in"
              className="block w-full text-center px-4 py-2 rounded-full border border-white text-white hover:bg-white hover:text-black transition-colors duration-200 ease-in-out"
              onClick={() => setIsMobileMenuOpen(false)}
            >
              Sign In
            </Link>
            <Link
              href="/apply"
              className="block w-full text-center px-4 py-2 rounded-full bg-white text-primary-green-color hover:bg-gray-200 transition-colors duration-200 ease-in-out"
              onClick={() => setIsMobileMenuOpen(false)}
            >
              Apply Now
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
