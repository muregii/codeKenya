import React from 'react';

import Navbar from '../pages/components/Navbar';
import UserProfile from './components/userinfo';
import AlumniDirectory from './components/directory';
import CommunityThreads from './components/communitythreads';
import EventsMeetups from './components/eventsandmeetups';
import Footer from '../pages/components/Footer';

function NetworkPage() {
  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />
      <main className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <div className="lg:col-span-1">
            <UserProfile />
          </div>
          <div className="lg:col-span-1">
            <AlumniDirectory />
          </div>
        </div>
        <div className="mt-12">
          <CommunityThreads />
        </div>
        <div className="mt-12">
          <EventsMeetups />
        </div>
      </main>
      <Footer />
    </div>
  );
}
export default NetworkPage;