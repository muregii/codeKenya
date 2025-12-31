import React from "react";

import Hero from "./components/Hero";
import CommunityHighlights from "./components/community-highlights";
import Footer from "../pages/components/Footer";
import Navbar from "../pages/components/Navbar";
import StatsSection from "./components/stats-section";
import CallToAction from "./components/CallToAction";

function Page() {
  return (
    <div>
      <Navbar/>
      <Hero />
      <CommunityHighlights/>
      <StatsSection/>
      <CallToAction/>
      <Footer />
    </div>
  );
}

export default Page;
