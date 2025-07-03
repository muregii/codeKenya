"use client";
import React, { useState } from "react";
import Image from "next/image"; // Importing Next.js Image component

function NavBar() {
  // State for managing the mobile menu
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  // Toggle function for the mobile menu
  const toggleMobileMenu = () => {
    setIsMobileMenuOpen(!isMobileMenuOpen);
  };

  return (
    <div>
      <nav className="bg-black text-white  relative w-full z-20 top-0 start-0 border-b border-gray-200">
        <div className="max-w-(--breakpoint-xl) flex flex-wrap items-center justify-between mx-auto p-4">
          <a className="flex items-center space-x-3 rtl:space-x-reverse">
            <Image
              src="/images/nobg-logo.svg"
              alt="Flowbite Logo"
              className="h-8"
              width={200} // You can adjust the width as necessary
              height={200} // Adjust the height as necessary
            />
          </a>
          <div className="flex md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse">
            <button
              type="button"
              className="text-white border border-white focus:ring-4 focus:outline-hidden focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 text-center hover:border-blue-500 hover:bg-white hover:text-black mx-4"
            >
              Sign In
            </button>

            <button
              type="button"
              className="text-green-500 border border-green-500 bg-white hover:bg-transparent focus:ring-4 focus:outline-hidden focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 text-center mx-4"
            >
              Apply now
            </button>

            {/* Hamburger icon to toggle mobile menu */}
            <button
              type="button"
              className="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-white rounded-lg md:hidden hover:bg-gray-100 focus:outline-hidden focus:ring-2 focus:ring-gray-200"
              onClick={toggleMobileMenu}
            >
              <span className="sr-only">Open main menu</span>
              <svg
                className="w-5 h-5"
                aria-hidden="true"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 17 14"
              >
                <path
                  stroke="currentColor"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M1 1h15M1 7h15M1 13h15"
                />
              </svg>
            </button>
          </div>

          {/* Mobile menu toggle */}
          <div
            className={`md:flex items-center justify-between hidden w-full md:w-auto md:order-1 ${
              isMobileMenuOpen ? "block" : "hidden"
            }`} // Show or hide nav items based on mobile menu state
            id="navbar-sticky"
          >
            <ul className="flex flex-col p-4 md:p-0 mt-4 font-medium border border-gray-100 rounded-lg bg-black md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-black">
              <li>
                <a
                  href="#"
                  className="block py-2 px-3 text-white bg-blue-700 rounded-sm md:bg-transparent md:text-blue-700 md:p-0"
                  aria-current="page"
                >
                  Home
                </a>
              </li>
              <li>
                <a
                  href="#"
                  className="block py-2 px-3 text-white rounded-sm hover:bg-gray-700 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:text-white"
                >
                  About
                </a>
              </li>
              <li>
                <a
                  href="#"
                  className="block py-2 px-3 text-white rounded-sm hover:bg-gray-700 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:text-white"
                >
                  Services
                </a>
              </li>
              <li>
                <a
                  href="#"
                  className="block py-2 px-3 text-white rounded-sm hover:bg-gray-700 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:text-white"
                >
                  Contact
                </a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  );
}

export default NavBar;
