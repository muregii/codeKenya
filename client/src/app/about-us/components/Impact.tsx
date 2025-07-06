import React from "react";

import Image from "next/image";

const Impact = () => {
  return (
    <div className="w-[90%] mx-auto">
      <h1 className="text-primary-green-color text-2xl text-center mb-4 font-bold">
        Our Impact
      </h1>
      <Image
        src="/images/our_impact_img.webp"
        alt="Learners in a bootcamp session"
        className="my-12 mx-auto rounded-lg border border-black border-4"
        height={800}
        width={800}
      />
    </div>
  );
};

export default Impact;
