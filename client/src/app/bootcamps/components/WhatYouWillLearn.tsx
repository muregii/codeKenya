import React from "react";
import {
  FaCalendar,
  FaChartBar,
  FaFileLines,
  FaEnvelope,
} from "react-icons/fa6";

import Button from "@/app/pages/components/Button";

const WhatYouWillLearn = () => {
  return (
    <div className="bg-primary-black-color text-white py-8">
      <div className="w-[90%] mx-auto space-y-10">
        <h1 className="text-3xl font-bold text-center md:text-left">
          What You Will Learn
        </h1>
        <p className="text-center md:text-left leading-relaxed">
          In our Management Consulting program, you&apos;ll gain a deep
          understanding of the consulting industry and develop the essential
          skills to excel as a consultant. You&apos;ll learn to apply a proven
          problem-solving approach across various industries and business
          contexts, mastering both hard skills like problem definition,
          PowerPoint, and Excel, as well as soft skills like client counseling
          and teamwork. By working in collaborative teams and interacting with
          diverse colleagues, you&apos;ll develop the interpersonal and cultural
          skills necessary to thrive in a global business environment.
        </p>
        <div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Card 1 */}
            <div className="flex gap-4 items-start">
              <FaCalendar className="w-12 h-12" />
              <div className="space-y-4">
                <h2 className="text-2xl font-bold">
                  Understand the consulting landscape
                </h2>
                <p>
                  Define Management Consulting: Grasp what management consulting
                  is and why organizations rely on consultants.
                </p>
                <p>
                  Consulting Firm Operations: Learn how consulting companies
                  function and manage diverse projects.
                </p>
                <p>
                  Industry Trends: Stay ahead with insights into the latest
                  trends shaping the consulting industry.
                </p>
              </div>
            </div>
            {/* Card 2 */}
            <div className="flex gap-4 items-start">
              <FaChartBar className="w-12 h-12" />
              <div className="space-y-4">
                <h2 className="text-2xl font-bold">
                  Enhance communication and presentation skills
                </h2>
                <p>
                  Pyramid Principle Application: Communicate ideas effectively
                  using structured thinking.
                </p>
                <p>
                  Storytelling and Storyboarding: Craft compelling narratives
                  and presentations that resonate with clients.
                </p>
                <p>
                  Professional Presentation Design: Create impactful slides and
                  visuals to support your message.
                </p>
              </div>
            </div>
            {/* Card 3 */}
            <div className="flex gap-4 items-start">
              <FaFileLines className="w-12 h-12" />
              <div className="space-y-4">
                <h2 className="text-2xl font-bold">
                  Develop analytical and problem-solving skills
                </h2>
                <p>
                  Business Model Analysis: Understand industries, business
                  models, and value chains.
                </p>
                <p>
                  Financial Acumen: Interpret key financial statements to assess
                  company performance.
                </p>
                <p>
                  Structured Problem Definition: Formulate SMART problem
                  statements and use MECE principles to structure complex
                  issues.
                </p>
              </div>
            </div>
            {/* Card 4 */}
            <div className="flex gap-4 items-start">
              <FaEnvelope className="w-12 h-12" />
              <div className="space-y-4">
                <h2 className="text-2xl font-bold">
                  Understand the consulting landscape
                </h2>
                <p>
                  Define Management Consulting: Grasp what management consulting
                  is and why organizations rely on consultants.
                </p>
                <p>
                  Consulting Firm Operations: Learn how consulting companies
                  function and manage diverse projects.
                </p>
                <p>
                  Industry Trends: Stay ahead with insights into the latest
                  trends shaping the consulting industry.
                </p>
              </div>
            </div>
          </div>
        </div>
        <div className="flex justify-center md:justify-start">
          <Button type="button" title="Download Syllabus" variant="btn_green" />
        </div>
      </div>
    </div>
  );
};

export default WhatYouWillLearn;
