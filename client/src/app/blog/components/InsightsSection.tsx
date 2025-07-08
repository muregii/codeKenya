"use client";

import React, { useState } from "react";
import Image from "next/image";
import Button from "@/app/pages/components/Button";
import { Search, Menu, X } from "lucide-react";

const InsightsBlogSection = () => {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  const blogTopics = [
    { id: 1, name: "Corporate" },
    { id: 2, name: "Energy" },
    { id: 3, name: "Technology" },
    { id: 4, name: "Stock" },
    { id: 5, name: "Artificial Intelligence" },
  ];

  const sidebarLinks = [
    { id: 1, name: "Tools" },
    { id: 2, name: "Statistics" },
    { id: 3, name: "Membership" },
    { id: 4, name: "Tutorial" },
    { id: 5, name: "Privacy" },
    { id: 6, name: "Career" },
    { id: 7, name: "Get Care" },
  ];

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Mobile Menu Overlay */}
      {isMobileMenuOpen && (
        <div className="fixed inset-0 bg-gray-800 bg-opacity-75 z-40 lg:hidden">
          <div className="fixed inset-y-0 left-0 w-64 bg-white p-6">
            <div className="flex justify-between items-center mb-6">
              <h2 className="text-lg text-black font-medium">Menu</h2>
              <button onClick={() => setIsMobileMenuOpen(false)}>
                <X className="h-6 w-6" />
              </button>
            </div>
            {/* Mobile Sidebar Content */}
            <div className="space-y-6">
              <div>
                <h3 className="text-sm font-medium mb-3 text-primary-green-color">
                  Blog Topics
                </h3>
                <div className="space-y-2">
                  {blogTopics.map((topic) => (
                    <button
                      key={topic.id}
                      className="block text-sm text-gray-600 hover:text-green-600 w-full text-left"
                    >
                      {topic.name}
                    </button>
                  ))}
                </div>
              </div>
              <div>
                <h3 className="text-sm font-medium mb-3 text-primary-green-color">
                  Guide and Tools
                </h3>
                <div className="space-y-2">
                  {sidebarLinks.map((link) => (
                    <button
                      key={link.id}
                      className="block text-sm text-gray-600 hover:text-green-600 w-full text-left"
                    >
                      {link.name}
                    </button>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      <div className="p-4 sm:p-6 lg:p-8">
        <div className="max-w-[90%] mx-auto">
          <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-6">
            <div className="flex items-center gap-4">
              <button
                className="lg:hidden"
                onClick={() => setIsMobileMenuOpen(true)}
              >
                <Menu className="h-6 w-6" />
              </button>
              <h1 className="text-3xl font-bold text-center md:text-left text-primary-green-color">
                Insights from our team
              </h1>
            </div>
            <div className="relative w-full sm:w-auto">
              <input
                type="text"
                placeholder="Search..."
                className="w-full sm:w-64 pl-8 pr-4 py-1 rounded-full border border-gray-300 focus:outline-hidden focus:border-green-500 text-sm"
              />
              <Search className="absolute left-2.5 top-1/2 transform -translate-y-1/2 text-gray-400 h-4 w-4" />
            </div>
          </div>

          <p className="text-sm text-gray-600 mb-6">
            Powerful Trading Tools and Features for Experienced Investors
          </p>

          {/* Main Content Grid */}
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
            {/* Sidebar - Hidden on mobile, shown on lg screens */}
            <div className="hidden lg:block lg:col-span-3">
              {/* Blog Topics */}
              <div className="mb-8">
                <h2 className="text-sm font-medium mb-3">Blog Topics</h2>
                <div className="space-y-2">
                  {blogTopics.map((topic) => (
                    <button
                      key={topic.id}
                      className="block text-sm text-gray-600 hover:text-green-600"
                    >
                      {topic.name}
                    </button>
                  ))}
                </div>
              </div>

              {/* Quick Links */}
              <div>
                <h2 className="text-sm font-medium mb-3">Guide and Tools</h2>
                <div className="space-y-2">
                  {sidebarLinks.map((link) => (
                    <button
                      key={link.id}
                      className="block text-sm text-gray-600 hover:text-green-600"
                    >
                      {link.name}
                    </button>
                  ))}
                </div>
              </div>
            </div>

            {/* Main Content */}
            <div className="lg:col-span-9 space-y-6">
              {/* Trending Topics*/}
              <div className="overflow-x-auto pb-2">
                <div className="flex gap-2 mb-6 whitespace-nowrap">
                  {[
                    "Media Release",
                    "Technology",
                    "Energy",
                    "Financial Data",
                    "AI",
                  ].map((tag) => (
                    <span
                      key={tag}
                      className="px-3 py-1 text-xs rounded-full border border-gray-300 text-gray-600 hover:bg-gray-50 cursor-pointer"
                    >
                      {tag}
                    </span>
                  ))}
                </div>
              </div>

              {/* Blog Posts */}
              <div className="space-y-6">
                {/* Post 1 */}
                <article className="bg-white rounded-lg overflow-hidden shadow-xs">
                  <div className="p-4 sm:p-6">
                    <div className="flex flex-col sm:flex-row gap-4 sm:gap-6">
                      <div className="flex-1">
                        <h2 className="text-lg font-medium mb-3">
                          Powerful Trading Tools and Features for Experienced
                          Investors
                        </h2>
                        <p className="text-gray-600 text-sm mb-4">
                          Discover our latest trading tools and analytics
                          designed for experienced traders...
                        </p>
                        <div className="flex items-center gap-4 text-sm text-gray-500">
                          <span>By John Smith</span>
                          <span>•</span>
                          <span>7 min read</span>
                        </div>
                      </div>
                      <div className="relative w-full sm:w-48 h-48 sm:h-32">
                        <Image
                          src="/images/blog-post-img1.png"
                          alt="Trading Tools"
                          className="object-cover rounded-lg"
                          height={200}
                          width={200}
                        />
                      </div>
                    </div>
                  </div>
                </article>

                {/* Post 2 */}
                <article className="bg-white rounded-lg overflow-hidden shadow-xs">
                  <div className="p-4 sm:p-6">
                    <div className="flex flex-col sm:flex-row gap-4 sm:gap-6">
                      <div className="flex-1">
                        <h2 className="text-lg font-medium mb-3">
                          We are Implementing AI and Technology
                        </h2>
                        <p className="text-gray-600 text-sm mb-4">
                          Learn about our latest AI implementations and
                          technological advancements...
                        </p>
                        <div className="flex items-center gap-4 text-sm text-gray-500">
                          <span>By Mary Johnson</span>
                          <span>•</span>
                          <span>5 min read</span>
                        </div>
                      </div>
                      <div className="relative w-full sm:w-48 h-48 sm:h-32">
                        <Image
                          src="/images/blog-post-img2.png"
                          alt="AI Technology"
                          className="object-cover rounded-lg"
                          height={200}
                          width={200}
                        />
                      </div>
                    </div>
                  </div>
                </article>
              </div>

              {/* Newsletter */}
              <div className="bg-white rounded-lg p-4 sm:p-6 mt-8">
                <h3 className="text-lg font-medium mb-4">
                  Join Our Newsletter
                </h3>
                <div className="flex flex-col sm:flex-row gap-4">
                  <input
                    type="email"
                    placeholder="Type your email..."
                    className="flex-1 px-4 py-2 border border-gray-300 rounded-md focus:outline-hidden focus:border-green-500"
                  />
                  {/* <button className="px-6 py-2 bg-red-600 text-white rounded-md hover:bg-red-700 transition-colors">
                    Subscribe
                  </button> */}
                  <Button type="button" title="Explore" variant="btn_red" />
                </div>
                <p className="text-xs text-gray-500 mt-2">
                  *You can unsubscribe anytime
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default InsightsBlogSection;
