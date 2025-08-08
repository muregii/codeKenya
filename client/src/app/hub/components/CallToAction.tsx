import React from 'react';
import Link from "next/link";
import Button from "@/app/pages/components/Button";


const CallToAction = () => {
  return (
    <section className="py-20 px-6 bg-white relative overflow-hidden">
      <div className="max-w-7xl mx-auto text-center relative z-10">
        <div className="relative w-full max-w-4xl mx-auto mb-12">
            {/* Circles positioned absolutely */}
            <div className="absolute left-0 top-1/2 transform -translate-y-1/2 w-32 h-32 bg-green-700 rounded-full opacity-90"></div>
            <div className="absolute left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2 w-28 h-28 bg-gray-400 rounded-full opacity-90"></div>
            <div className="absolute right-0 top-1/2 transform -translate-y-1/2 w-32 h-32 bg-red-700 rounded-full opacity-90"></div>

            <h2 className="relative z-10 text-center text-3xl md:text-5xl font-bold leading-tight px-4">
              BE A PART OF KENYA’S TECH DRIVEN <span className="text-red-700">FUTURE.</span><br />
              <span className="text-green-700">START</span> CONNECTING NOW
            </h2>
          </div>


        <div className="flex justify-center">
            <Link href="/about-us">
              <Button
                type="button"
                title="Join the Community"
                variant="btn_red_rounded px-8 py-4"
              />
            </Link>
        </div>
        
      </div>
    </section>
  );
};

export default CallToAction;
