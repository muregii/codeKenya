import React from "react";

import PricingSection from "./PricingSection";

const Pricing = () => {
  return (
    <div className="text-center md:max-w-[90%] mx-auto w-full py-20 ">
      <p className="bg-[#e1ede1ff] text-primary-green-color w-fit py-1 px-2 mx-auto text-xs rounded-md">
        Tuition Fee
      </p>
      <div className="w-full md:max-w-[50%] mx-auto space-y-1 my-6">
        <h1 className="text-3xl font-black">Pay once or in installments</h1>
        <p>
          We offer flexible and convenient tuition fee payment options to suit
          your needs. Choose to pay upfront, or spread the cost through
          manageable monthly installments.
        </p>
      </div>
      <PricingSection />
    </div>
  );
};

export default Pricing;
