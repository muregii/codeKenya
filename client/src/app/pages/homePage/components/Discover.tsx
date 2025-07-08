import React from "react";

import Image from "next/image";
import Link from "next/link";

import Button from "../../components/Button";

const Discover = () => {
  return (
    <div className="flex w-[90%] mx-auto py-16">
      <div>
        <div className="flex flex-col md:flex-row">
          <div className="space-y-4 md:w-[20%] w-full mb-12 md:mb-0 ">
            <p className="text-primary-green-color text-base">
              ✦ Travel . Discover
            </p>
            <h2 className="text-3xl font-semibold leading-8">
              Find your perfect place to experience the city{" "}
            </h2>
            <p className="text-lg">
              We are thrilled to offer our students a unique chance to
              experience the vibrant charm and iconic landmarks of Nairobi City and Kenya at large.
            </p>
            <div className="flex justify-center md:justify-start">
              <Link href='/apply'>
                <Button type="button" title="Apply now" variant="btn_green" />
              </Link>
            </div>
          </div>
          <Image
            src="/images/discover-img.png"
            alt="Giraffe"
            height={500}
            width={500}
          />
        </div>
        {/* <Image
          src="/images/discover-cards.png"
          alt="Information cards"
          className="py-12 pl-12 md:block hidden"
          height={700}
          width={700}
        /> */}
      </div>
      <Image
        src="/images/discover-images-right.png"
        alt="Places to visit in Nairobi"
        className="md:block hidden"
        height={200}
        width={200}
      />
    </div>
  );
};

export default Discover;
