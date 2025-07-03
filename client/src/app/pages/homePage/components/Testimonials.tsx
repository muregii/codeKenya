import React from "react";

import SuccessStoriesCarousel from "../../components/SuccessStoriesCarousel";

const Testimonials = () => {
  return (
    <div className="w-full md:w-[90%] mx-auto py-16">
      <h2 className="text-4xl font-bold text-center md:text-left text-primary-green-color">
        Student Success Stories
      </h2>
      <SuccessStoriesCarousel/>
    </div>
  );
};

export default Testimonials;
