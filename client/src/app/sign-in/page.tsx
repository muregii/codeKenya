"use client";

import Image from "next/image";
import React, { useState, useEffect } from "react";

const ApplicationForm: React.FC = () => {
  const [currentSlide, setCurrentSlide] = useState(0);
  const [formData, setFormData] = useState({
    first_name: "",
    last_name: "",
    email_phone: "",
    dob: "",
    course_id: "",
    university_name: "",
    essay: "",
  });
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  const totalSlides = 3;

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentSlide((prev) => (prev === totalSlides - 1 ? 0 : prev + 1));
    }, 5000);

    return () => clearInterval(timer);
  }, []);

  const validateForm = () => {
    const newErrors: Record<string, string> = {};

    // First Name validation
    if (!formData.first_name.trim()) {
      newErrors.first_name = "First name is required";
    } else if (formData.first_name.length < 2) {
      newErrors.first_name = "First name must be at least 2 characters";
    }

    // Last Name validation
    if (!formData.last_name.trim()) {
      newErrors.last_name = "Last name is required";
    } else if (formData.last_name.length < 2) {
      newErrors.last_name = "Last name must be at least 2 characters";
    }

    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email_phone.trim()) {
      newErrors.email_phone = "Email is required";
    } else if (!emailRegex.test(formData.email_phone)) {
      newErrors.email_phone = "Please enter a valid email";
    }

    // Date of Birth validation
    if (!formData.dob) {
      newErrors.dob = "Date of birth is required";
    } else {
      const birthDate = new Date(formData.dob);
      const today = new Date();
      const age = today.getFullYear() - birthDate.getFullYear();
      if (age < 16) {
        newErrors.dob = "You must be at least 16 years old";
      }
    }

    // course_id validation
    if (!formData.course_id) {
      newErrors.course_id = "Please select a course";
    }

    // University validation
    if (!formData.university_name.trim()) {
      newErrors.university_name = "University is required";
    }

    return newErrors;
  };

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>
  ) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
    // Clear error when user starts typing
    if (errors[name]) {
      setErrors((prev) => ({
        ...prev,
        [name]: "",
      }));
    }
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const newErrors = validateForm();
    setErrors(newErrors);

    if (Object.keys(newErrors).length === 0) {
      setIsSubmitting(true);
      try {
        console.log("Form submitted:", formData);
        alert("Form submitted successfully!");
      } catch (error) {
        console.error("Submission error:", error);
        alert("An error occurred while submitting the form");
      } finally {
        setIsSubmitting(false);
      }
    }
  };

  return (
    <div className="h-screen bg-gray-100 p-4 sm:p-6 lg:p-8 flex items-center justify-center">
      <div className="w-full max-w-6xl">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 h-full">
          {/* Carousel Section */}
          <div className="relative bg-primary-red-color rounded-2xl p-8 flex flex-col">
            <h2 className="text-white text-xl md:text-2xl text-center mb-8">
              Welcome Back! Please log in to access your account.
            </h2>

            <div className="relative flex-1 flex items-center justify-center">
              <div className="absolute inset-0 bg-primary-green-color rounded-full"></div>
              <div className="relative w-full max-w-sm aspect-3/4 overflow-hidden">
                <div
                  className="flex transition-transform duration-500 ease-out h-full"
                  style={{ transform: `translateX(-${currentSlide * 100}%)` }}
                >
                  {[...Array(totalSlides)].map((_, index) => (
                    <div key={index} className="w-full shrink-0">
                      <Image
                        src="/images/application-carousel-img.png"
                        alt={`Application feature ${index + 1}`}
                        className="w-full h-full object-cover"
                        height={200}
                        width={200}
                      />
                    </div>
                  ))}
                </div>
              </div>

              <div className="absolute bottom-4 left-1/2 -translate-x-1/2 flex space-x-2">
                {[...Array(totalSlides)].map((_, index) => (
                  <button
                    key={index}
                    onClick={() => setCurrentSlide(index)}
                    className={`w-2 h-2 rounded-full transition-all ${
                      currentSlide === index ? "bg-white w-4" : "bg-white/50"
                    }`}
                  />
                ))}
              </div>
            </div>
          </div>

          {/* Form Section */}
          <div className="bg-white rounded-lg p-6 shadow-lg">
            <form onSubmit={handleSubmit} className="h-full flex flex-col">
              <div className="flex flex-col space-y-4 mb-8">
                <Image
                  src="/images/code-kenya-logo-black.png"
                  alt="Code Kenya Logo"
                  //   className="h-12 w-16"
                  height={200}
                  width={200}
                />
                <div>
                  <h2 className="text-2xl font-semibold">Login now</h2>
                  <p>Login to your student account</p>
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 flex-1 overflow-y-auto">
                {/* First Name */}
                <div className="flex flex-col">
                  <label className="mb-1 text-sm font-medium text-gray-700">
                    First name
                  </label>
                  <input
                    type="text"
                    name="first_name"
                    value={formData.first_name}
                    onChange={handleChange}
                    className={`px-3 py-2 border rounded-md focus:outline-hidden focus:ring-2 ${
                      errors.first_name
                        ? "border-red-500 focus:ring-red-200"
                        : "border-gray-300 focus:ring-green-200"
                    }`}
                    placeholder="Enter your first name"
                  />
                  {errors.first_name && (
                    <span className="text-red-500 text-xs mt-1">
                      {errors.first_name}
                    </span>
                  )}
                </div>

                {/* Last Name */}
                <div className="flex flex-col">
                  <label className="mb-1 text-sm font-medium text-gray-700">
                    Last name
                  </label>
                  <input
                    type="text"
                    name="last_name"
                    value={formData.last_name}
                    onChange={handleChange}
                    className={`px-3 py-2 border rounded-md focus:outline-hidden focus:ring-2 ${
                      errors.last_name
                        ? "border-red-500 focus:ring-red-200"
                        : "border-gray-300 focus:ring-green-200"
                    }`}
                    placeholder="Enter your last name"
                  />
                  {errors.last_name && (
                    <span className="text-red-500 text-xs mt-1">
                      {errors.last_name}
                    </span>
                  )}
                </div>

                {/* Email */}
                <div className="flex flex-col">
                  <label className="mb-1 text-sm font-medium text-gray-700">
                    Email
                  </label>
                  <input
                    type="email"
                    name="email_phone"
                    value={formData.email_phone}
                    onChange={handleChange}
                    className={`px-3 py-2 border rounded-md focus:outline-hidden focus:ring-2 ${
                      errors.email_phone
                        ? "border-red-500 focus:ring-red-200"
                        : "border-gray-300 focus:ring-green-200"
                    }`}
                    placeholder="Enter your email"
                  />
                  {errors.email_phone && (
                    <span className="text-red-500 text-xs mt-1">
                      {errors.email_phone}
                    </span>
                  )}
                </div>

                {/* Date of Birth */}
                <div className="flex flex-col">
                  <label className="mb-1 text-sm font-medium text-gray-700">
                    Date of birth
                  </label>
                  <input
                    type="date"
                    name="dob"
                    value={formData.dob}
                    onChange={handleChange}
                    className={`px-3 py-2 border rounded-md focus:outline-hidden focus:ring-2 ${
                      errors.dob
                        ? "border-red-500 focus:ring-red-200"
                        : "border-gray-300 focus:ring-green-200"
                    }`}
                  />
                  {errors.dob && (
                    <span className="text-red-500 text-xs mt-1">
                      {errors.dob}
                    </span>
                  )}
                </div>

                {/* Course Selection */}
                <div className="flex flex-col">
                  <label className="mb-1 text-sm font-medium text-gray-700">
                    What course are you most interested in?
                  </label>
                  <select
                    name="course_id"
                    value={formData.course_id}
                    onChange={handleChange}
                    className={`px-3 py-2 border rounded-md focus:outline-hidden focus:ring-2 ${
                      errors.course_id
                        ? "border-red-500 focus:ring-red-200"
                        : "border-gray-300 focus:ring-green-200"
                    }`}
                  >
                    <option value="">Select a course</option>
                    <option value="software-dev">Software Development</option>
                    <option value="data-science">Data Science</option>
                    <option value="management">Management Consulting</option>
                    <option value="investment">Investment Banking</option>
                  </select>
                  {errors.course_id && (
                    <span className="text-red-500 text-xs mt-1">
                      {errors.course_id}
                    </span>
                  )}
                </div>

                {/* University */}
                <div className="flex flex-col">
                  <label className="mb-1 text-sm font-medium text-gray-700">
                    University
                  </label>
                  <input
                    type="text"
                    name="university_name"
                    value={formData.university_name}
                    onChange={handleChange}
                    className={`px-3 py-2 border rounded-md focus:outline-hidden focus:ring-2 ${
                      errors.university_name
                        ? "border-red-500 focus:ring-red-200"
                        : "border-gray-300 focus:ring-green-200"
                    }`}
                    placeholder="Enter your university"
                  />
                  {errors.university_name && (
                    <span className="text-red-500 text-xs mt-1">
                      {errors.university_name}
                    </span>
                  )}
                </div>
              </div>

              <button
                type="submit"
                disabled={isSubmitting}
                className={`w-full py-2 px-4 rounded-md text-white mt-6 ${
                  isSubmitting
                    ? "bg-gray-400 cursor-not-allowed"
                    : "bg-primary-green-color hover:bg-green-700 transition-colors"
                }`}
              >
                {isSubmitting ? "Logging you in..." : "Login"}
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ApplicationForm;
