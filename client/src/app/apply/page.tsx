"use client";

import Image from "next/image";
import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import { useRouter } from "next/navigation";
import useDebounce from "@/hooks/useDebounce";

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
  // Email verification state
  const [emailVerificationStatus, setEmailVerificationStatus] = useState({
    loading: false,
    valid: null as boolean | null,
    message: "",
  });

  // Refs
  const lastVerifiedEmail = useRef<string>("");
  const emailCache = useRef<Record<string, boolean>>({});

  const totalSlides = 3;

  const router = useRouter();

  // Initialize debounced verify function
  const debouncedVerify = useDebounce(async (...args: unknown[]) => {
    const email = args[0] as string;
    if (emailCache.current[email] !== undefined) {
      setEmailVerificationStatus({
        loading: false,
        valid: emailCache.current[email],
        message: emailCache.current[email]
          ? "Email is valid"
          : "Email is invalid",
      });
      return;
    }

    setEmailVerificationStatus((prev) => ({
      ...prev,
      loading: true,
      message: "Verifying...",
    }));

    try {
      const response = await fetch("/api/verify-email", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email }),
      });

      const data = await response.json();
      const isValid = data.success === "true" && data.result === "valid";

      emailCache.current[email] = isValid;
      lastVerifiedEmail.current = email;

      setEmailVerificationStatus({
        loading: false,
        valid: isValid,
        message: isValid
          ? "Email is valid"
          : `Invalid email. Please enter a valid work or personal email address`,
      });
    } catch (error) {
      console.error("Email verification error:", error);
      setEmailVerificationStatus({
        loading: false,
        valid: false,
        message: "Verification service unavailable",
      });
    }
  }, 500);

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentSlide((prev) => (prev === totalSlides - 1 ? 0 : prev + 1));
    }, 5000);

    return () => clearInterval(timer);
  }, []);

  // Handle email blur event to trigger verification when one leaves the input
  const handleEmailBlur = () => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const email = formData.email_phone.trim();

    if (
      email &&
      emailRegex.test(email) &&
      email !== lastVerifiedEmail.current
    ) {
      debouncedVerify(email);
    }
  };

  const validateForm = () => {
    const newErrors: Record<string, string> = {};
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

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
    if (!formData.email_phone.trim()) {
      newErrors.email_phone = "Email is required";
    } else if (!emailRegex.test(formData.email_phone)) {
      newErrors.email_phone = "Please enter a valid email";
    } else if (emailVerificationStatus.valid === false) {
      newErrors.email_phone = emailVerificationStatus.message;
    } else if (
      emailVerificationStatus.valid === null &&
      formData.email_phone === lastVerifiedEmail.current
    ) {
      // Only show validation message if we haven't verified yet
      newErrors.email_phone = "Please wait for email verification";
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

    // Course validation
    if (!formData.course_id) {
      newErrors.course_id = "Please select a course";
    }

    // University validation
    if (!formData.university_name.trim()) {
      newErrors.university_name = "University is required";
    }

    // Essay validation
    if (!formData.essay.trim()) {
      newErrors.essay = "Essay is required";
    } else if (formData.essay.trim().length < 100) {
      newErrors.essay = "Essay must be at least 100 characters";
    } else if (formData.essay.trim().length > 500) {
      newErrors.essay = "Essay must not exceed 500 characters";
    }

    return newErrors;
  };

  const handleChange = (
    e: React.ChangeEvent<
      HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement
    >
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
    const base_url = process.env.NEXT_PUBLIC_BASE_API_URL;
    // console.log("Api base url::", base_url);
    e.preventDefault();
    const newErrors = validateForm();
    setErrors(newErrors);

    if (Object.keys(newErrors).length === 0) {
      setIsSubmitting(true);
      try {
        // Convert course_id to number before sending
        const submissionData = {
          ...formData,
          course_id: parseInt(formData.course_id, 10),
        };

        const response = await axios.post(
          `${base_url}/api/applications`,
          submissionData
        );
        const data = response.data;
        if (response.status === 200) {
          router.push("/application-success-page");
        }
        console.log("Form submitted:", data);
        // alert("Form submitted successfully!");
      } catch (error) {
        console.error("Submission error:", error);
        alert(
          "Oopsie! an error may have occured on our end, please try again later or check your internet connection 😥"
        );
      } finally {
        setIsSubmitting(false);
      }
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-4 sm:p-6 lg:p-8 flex items-center justify-center">
      <div className="w-full max-w-6xl">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {/* Carousel Section */}
          <div className="relative bg-primary-red-color rounded-2xl p-8 flex flex-col">
            <h2 className="text-white text-xl md:text-2xl text-center mb-8">
              Start your application at Code Kenya to unlock exclusive features
              and start your career journey
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
          <div className="bg-white rounded-lg p-6 shadow-lg overflow-y-auto max-h-[800px]">
            <form onSubmit={handleSubmit} className="flex flex-col">
              <div className="flex flex-col space-y-4 mb-8">
                <Image
                  src="/images/code-kenya-logo-black.png"
                  alt="Code Kenya Logo"
                  height={200}
                  width={200}
                />
                <div>
                  <h2 className="text-2xl font-semibold">Apply now</h2>
                  <p>Begin your application at Code Kenya</p>
                </div>
              </div>

              <div>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
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

                  {/* <div className="flex flex-col">
                    <label className="mb-1 text-sm font-medium text-gray-700">
                      Email or Phone
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
                      placeholder="Enter your email or phone"
                    />
                    {errors.email_phone && (
                      <span className="text-red-500 text-xs mt-1">
                        {errors.email_phone}
                      </span>
                    )}
                  </div> */}

                  <div className="flex flex-col">
                    <label className="mb-1 text-sm font-medium text-gray-700">
                      Email or Phone
                    </label>
                    <input
                      type="email"
                      name="email_phone"
                      value={formData.email_phone}
                      onChange={handleChange}
                      onBlur={handleEmailBlur}
                      className={`px-3 py-2 border rounded-md focus:outline-none focus:ring-2 ${
                        errors.email_phone
                          ? "border-red-500 focus:ring-red-200"
                          : emailVerificationStatus.valid === true
                          ? "border-green-500 focus:ring-green-200"
                          : "border-gray-300 focus:ring-green-200"
                      }`}
                      placeholder="Enter your email or phone"
                    />
                    {errors.email_phone && (
                      <span className="text-red-500 text-xs mt-1">
                        {errors.email_phone}
                      </span>
                    )}
                    {emailVerificationStatus.loading && (
                      <span className="text-blue-500 text-xs mt-1">
                        {emailVerificationStatus.message}
                      </span>
                    )}
                    {emailVerificationStatus.valid === true &&
                      !errors.email_phone && (
                        <span className="text-green-500 text-xs mt-1">
                          {emailVerificationStatus.message}
                        </span>
                      )}
                  </div>

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
                      <option value="1">Software Engineering</option>
                      <option value="2">Entrepreneurship</option>
                    </select>
                    {errors.course_id && (
                      <span className="text-red-500 text-xs mt-1">
                        {errors.course_id}
                      </span>
                    )}
                  </div>

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

                {/* Essay Section */}
                <div className="mt-4 flex flex-col col-span-2">
                  <label className="mb-1 text-sm font-medium text-gray-700">
                    Why do you want to join this program? (100-500 characters)
                  </label>
                  <textarea
                    name="essay"
                    value={formData.essay}
                    onChange={handleChange}
                    rows={4}
                    className={`px-3 py-2 border rounded-md focus:outline-hidden focus:ring-2 resize-none ${
                      errors.essay
                        ? "border-red-500 focus:ring-red-200"
                        : "border-gray-300 focus:ring-green-200"
                    }`}
                    placeholder="Write your essay here..."
                  />
                  <div className="flex justify-between mt-1">
                    <span className="text-red-500 text-xs">{errors.essay}</span>
                    <span className="text-gray-500 text-xs">
                      {formData.essay.length}/500 characters
                    </span>
                  </div>
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
                {isSubmitting ? "Submitting..." : "Submit Application"}
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ApplicationForm;
