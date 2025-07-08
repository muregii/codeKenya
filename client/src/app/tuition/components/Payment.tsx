import React from "react";

import Image from "next/image";

const Payment = () => {
  return (
    <div className="bg-primary-black-color text-white">
      <div className="max-w-[90%] mx-auto py-10 ">
        <h1 className="text-4xl font-black text-center">
          Your payment options
        </h1>
        <div className="flex justify-center items-center">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-12 mt-12 ">
            <div className="border border-white rounded-lg p-4 border">
              <Image
                src="/icons/payment-svg2.svg"
                alt="payment option 2 icon"
                height={30}
                width={30}
                loading="lazy"
                quality={80}
              />
              <div className="mt-6 space-y-1">
                <h2 className="font-semibold text-base">Once-Off Payments</h2>
                <p className="text-xs font-thin text-slate-100">
                  Pay the entire tuition upfront via Bank Transfer or Klarna.
                </p>
              </div>
            </div>

            <div className="border border-white rounded-lg p-4 border">
              <Image
                src="/icons/payment-svg3.svg"
                alt="payment option 3 icon"
                height={30}
                width={30}
                loading="lazy"
                quality={80}
              />
              <div className="mt-6 space-y-1">
                <h2 className="font-semibold text-base">
                  Installment Payments
                </h2>
                <p className="text-xs font-thin text-slate-100">
                  Spread payments across months leading up to the program start
                  date.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Payment;
