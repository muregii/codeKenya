import React from "react";

import Image from "next/image";
import Link from "next/link";

import Button from "../../components/Button";

const HowToApply = () => {
  return (
    <div className="w-[90%] mx-auto">
      <h1 className="text-4xl font-semibold text-center md:text-left text-primary-green-color">
        How to apply to Code Kenya
      </h1>
      <div className="flex flex-col md:flex-row justify-between items-center">
        <div className="flex items-start gap-4 md:max-w-[60%]">
          <div className="bg-primary-green-color w-[8px] h-40"></div>
          <div className="space-y-8">
            <p className="text-base">
              To apply, start by signing up on our website and filling out a
              short form. Complete your application and upload any required
              financial aid documents. If eligible, you&apos;ll be invited for a
              1:1 interview. Within two weeks of the interview, you&apos;ll
              receive your admissions decision.
            </p>
            <div className="flex justify-center md:justify-start">
              <Link href="/apply">
                <Button type="button" title="Apply here" variant="btn_green" />
              </Link>
            </div>
          </div>
        </div>
        <Image
          src="/images/how-to-apply-img.png"
          alt="Lady going through admission papers"
          height={500}
          width={500}
        />
      </div>
      <div className="flex flex-col md:flex-row justify-between gap-3 pt-12">
        <div className="p-8 flex-1 bg-primary-black-color text-white space-y-3">
          <h2 className="font-bold text-2xl">Sign-up to start application</h2>
          <p className="text-sm">
            Click the &quot;apply now&quot; button on our website to start the
            process. You&apos;ll be directed to fill out a short form to receive
            more information.
          </p>
        </div>

        <div className="p-8 flex-1 bg-white text-primary-green-color space-y-3">
          <h2 className="font-bold text-2xl">Complete your application</h2>
          <p className="text-sm">
            Fully complete your application and ensure it submits.
          </p>
        </div>

        <div className="p-8 flex-1 bg-primary-red-color text-white space-y-3">
          <h2 className="font-bold text-2xl">Interview invitation</h2>
          <p className="text-sm">
            Based on your application and evaluation, you&apos;ll receive an
            invitation for an interview. The interview will be conducted in a
            1:1 setting.
          </p>
        </div>

        <div className="p-8 flex-1 bg-primary-green-color text-white space-y-3">
          <h2 className="font-bold text-2xl">Admissions outcome</h2>
          <p className="text-sm">
            Once your interview is complete, you will receive your admissions
            decision within 2 weeks.
          </p>
        </div>
      </div>
    </div>
  );
};

export default HowToApply;
