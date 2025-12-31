import React from 'react'
import { Linkedin, Github, Mail, GraduationCap, Briefcase } from 'lucide-react'
import Image from 'next/image';
import Button from '@/app/pages/components/Button';

const UserProfile = () => {
  return (
    <div className="space-y-6">
      {/* Profile Card */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <div className="text-center">
          <div className="w-24 h-24 bg-gray-300 rounded-full mx-auto mb-4 flex items-center justify-center">
              <Image
                src="/images/profile-icon.png"
                alt="Green circle"
                height={250}
                width={250}
                className="object-contain"
              />
          </div>
          <h2 className="text-xl font-bold mb-1">USER NAME</h2>
          <p className="text-gray-600 mb-4">Class of 2025 (Cohort 1)</p>
            <Button
              type="button"
              title="Explore & Apply"
              variant="btn_green ml-32"
            />
        </div>
      </div>

      {/* Current Information */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <div className="relative w-full max-w-4xl mx-auto mb-12">
            {/* Red circle positioned absolutely */}
            <div className="absolute left-right top-1/2 transform -translate-y-1/4 transform -translate-x-1/5 w-28 h-28 bg-red-700 rounded-full opacity-70"></div>

            <h2 className="relative z-10 text-xl md:text-2xl font-extrabold leading-tight px-4 ml-10">
              CURRENT INFORMATION <br />
            </h2>
          </div>
        <div className="space-y-4 ml-8">
          <div className="flex items-center space-x-3">
            <Briefcase className="w-7 h-7 text-black-600" />
            <span className="font-bold text-xl">Software Engineer</span>
          </div>
          <div className="flex items-start space-x-3">
            <GraduationCap className="w-7 h-7 bg-black-200 text-black-600 mt-1" />
            <div>
              <div className="font-bold text-xl">University of Nairobi</div>
              <div className="text-m text-gray-600">B.S in Computer Science</div>
            </div>
          </div>
          <div>
          <div className="flex items-center space-x-12 pt-4 ml-20 hover:ml-16 transition-all duration-300">
            <Linkedin className="w-6 h-6 text-blue-600 cursor-pointer hover:text-blue-700" />
            <Github className="w-6 h-6 text-gray-800 cursor-pointer hover:text-gray-900" />
            <Mail className="w-6 h-6 text-gray-600 cursor-pointer hover:text-gray-700" />
          </div>
          </div>
        </div>
      </div>

      {/* About Me */}
      <div className="relative w-full max-w-4xl mx-auto mb-12">
        {/* Green circle positioned absolutely */}
      <div className="absolute left-right ml-6 mt-7 transform -translate-y-1/4 transform -translate-x-1/5 w-28 h-28 bg-green-700 rounded-full opacity-70"></div>
      
      <div className="bg-white rounded-lg shadow-md p-6">
        <h3 className="text-2xl font-bold mb-4 ml-20">ABOUT ME</h3>
        <div className="text-black p-4 rounded-lg mb-4">
          <p className="text-l font-bold leading-relaxed">
            Passionate Software Engineer specializing in full-stack development. Experienced in building scalable applications and working with small and large teams alike.
          </p>
        </div>
        <div className="flex flex-wrap gap-2 hover:gap-5 transition-all duration-300 ml-25">
          <span className="bg-red-600 text-white px-3 py-1 rounded text-sm">Next.js</span>
          <span className="bg-orange-600 text-white px-3 py-1 rounded text-sm">HTML</span>
          <span className="bg-blue-600 text-white px-3 py-1 rounded text-sm">Python</span>
        </div>
      </div>
      </div>
    </div>
  )
}

export default UserProfile
