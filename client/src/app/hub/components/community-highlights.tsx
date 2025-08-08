import React from 'react';
import { FiUsers, FiCheckCircle, FiThumbsUp } from "react-icons/fi";


const CommunityHighlights = () => {
  const highlights =[
    {
      icon: <FiUsers size={28} className="text-green-500" />,
      title: "Alumni Mentors",
      description:
        "Connect with experienced alumni mentors who provide personalized guidance, share invaluable career insights, and help you navigate your academic and professional journey with confidence."
    },
    {
      icon: <FiCheckCircle size={28} className="text-green-500" />,
      title: "Peer Collaborations",
      description:
        "Engage in dynamic peer-to-peer collaborations that foster teamwork, innovation, and mutual growth. Work on real projects, exchange knowledge, and build lasting professional relationships."
    },
    {
      icon: <FiThumbsUp size={28} className="text-green-500" />,
      title: "Future Referrals",
      description:
        "Gain access to exclusive referral opportunities and endorsements that accelerate your career path. Leverage our network to unlock internships, job offers, and other career-boosting advantages."
    }
  ];

  return (
    <section className="py-20 px-6 bg-white">
      <div className="max-w-7xl mx-auto">
        <h2 className="text-4xl font-bold text-black mb-16">Community Highlights</h2>
        
        <div className="grid md:grid-cols-3 gap-8">
          {highlights.map((highlight, index) => (
            <div key={index} className="bg-gray-200 p-8 rounded-lg">
              <div className="text-4xl mb-4">{highlight.icon}</div>
              <h3 className="text-xl font-bold mb-4 text-black">{highlight.title}</h3>
              <p className="text-gray-700">{highlight.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default CommunityHighlights;
