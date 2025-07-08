import React from "react";

import Image from "next/image";

const Partners = () => {
  return (
    <div className="w-[90%] mx-auto">
      <h1 className="text-4xl font-bold">Our Major Partners</h1>
      <div className="py-8 flex flex-col md:flex-row justify-between gap-4 items-center">
        <div className="rounded-lg border-solid border border-black flex gap-2 items-center p-6">
          <Image
            src="/images/mastercard-logo.png"
            alt="Mastercard Logo"
            height={100}
            width={100}
          />
          <p>
            MasterCard’s expertise supports our mission to empower students
            worldwide.
          </p>
        </div>

        <div className="rounded-lg border-solid border border-black flex  gap-2 items-center p-6">
          <Image
            src="/images/microsoft-logo.png"
            alt="Microsoft Logo"
            height={100}
            width={100}
          />
          <p>
            Microsoft’s expertise supports our mission to empower students
            worldwide.
          </p>
        </div>

        <div className="rounded-lg border-solid border border-black flex gap-2 items-center p-6">
          <Image
            src="/images/visa-logo.png"
            alt="Visa Logo"
            height={100}
            width={100}
          />
          <p>
            Visa’s expertise supports our mission to empower students worldwide.
          </p>
        </div>
      </div>
    </div>
  );
};

export default Partners;
