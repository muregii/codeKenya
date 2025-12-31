"use client"

import React, { useState } from "react"
import { Search } from "lucide-react"
import Image from "next/image"

interface Alumni {
  id: number
  name: string
  title: string
  company: string
  university: string
  cohort?: string
  image?: string
}

const AlumniDirectory = () => {
  const [searchTerm, setSearchTerm] = useState("")
  const [selectedCohort, setSelectedCohort] = useState("")
  const [selectedUniversity, setSelectedUniversity] = useState("")
  const [selectedJobTitle, setSelectedJobTitle] = useState("")
  const [selectedCompany, setSelectedCompany] = useState("")

  const alumni: Alumni[] = [
    { id: 1, image: "/images/CEO-img.webp", name: "RAYDON MUREGI", title: "CEO", company: "codeKenya", university: "Duke University", cohort: "2018" },
    { id: 2, image: "/images/testimonial_kendi.webp", name: "KENDI MIRITI", title: "Alumni", company: "", university: "Duke Kunshan University", cohort: "2019" },
    { id: 3, image: "/images/testimonial_godwin.webp", name: "GODWIN KANGOR", title: "Alumni", company: "", university: "Dartmouth College", cohort: "2019" },
    { id: 4, image: "/images/testimonial_francis.webp", name: "FRANCIS IBOKO", title: "Alumni", company: "", university: "Northwestern University", cohort: "2020" },
    { id: 5, image: "/images/kelvinkemboi.jpg", name: "KELVIN KEMBOI", title: "Student", company: "", university: "Colgate University", cohort: "2023" },
    { id: 6, image: "/images/Okemwa-profile.jpg", name: "GABRIEL OKEMWA", title: "Lead Software Engineer", company: "CodeKenya", university: "Jomo Kenyatta University of Agriculture and Technology", cohort: "2017" },
    { id: 7, image: "/images/profile-icon.png", name: "JEAN FINBAR", title: "Student", company: "", university: "University of Pennsylvania", cohort: "2023" },
    { id: 8, image: "/images/profile-icon.png", name: "DIANA", title: "UX Designer", company: "CodeKenya", university: "", cohort: "2021" },
    { id: 9, image: "/images/profile-icon.png", name: "ANUNDA MORGAN", title: "Student", company: "", university: "Johns Hopkins University", cohort: "2022" },
    { id: 10, image: "/images/profile-icon.png", name: "SYDNEY KARIUKI", title: "Coding Instructor", company: "CodeKenya", university: "", cohort: "2020" },
  ]

  // Get unique filter options
  const cohorts = Array.from(new Set(alumni.map(a => a.cohort).filter(Boolean)))
  const universities = Array.from(new Set(alumni.map(a => a.university).filter(Boolean)))
  const jobTitles = Array.from(new Set(alumni.map(a => a.title).filter(Boolean)))
  const companies = Array.from(new Set(alumni.map(a => a.company).filter(Boolean)))

  // Apply filters
  const filteredAlumni = alumni.filter(person =>
    person.name.toLowerCase().includes(searchTerm.toLowerCase()) &&
    (selectedCohort ? person.cohort === selectedCohort : true) &&
    (selectedUniversity ? person.university === selectedUniversity : true) &&
    (selectedJobTitle ? person.title === selectedJobTitle : true) &&
    (selectedCompany ? person.company === selectedCompany : true)
  )

  return (
    <div className="bg-white rounded-lg shadow-md p-6 h-[148vh] flex flex-col">
      <h2 className="text-2xl font-bold mb-6">ALUMNI DIRECTORY</h2>

      {/* Search and Filters */}
      <div className="mb-6 flex-shrink-0">
        {/* Search Bar */}
        <div className="relative mb-4">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
          <input
            type="text"
            placeholder="Search Alumni"
            className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-code-kenya-green"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>

        {/* Filters - keeping original design */}
        <div className="flex flex-wrap gap-2">
          <select
            className="px-3 py-2 border border-gray-300 rounded bg-white text-sm"
            value={selectedCohort}
            onChange={(e) => setSelectedCohort(e.target.value)}
          >
            <option value="">Cohort</option>
            {cohorts.map((c) => (
              <option key={c} value={c}>{c}</option>
            ))}
          </select>

          <select
            className="px-3 py-2 border border-gray-300 rounded bg-white text-sm"
            value={selectedUniversity}
            onChange={(e) => setSelectedUniversity(e.target.value)}
          >
            <option value="">University</option>
            {universities.map((u) => (
              <option key={u} value={u}>{u}</option>
            ))}
          </select>

          <select
            className="px-3 py-2 border border-gray-300 rounded bg-white text-sm"
            value={selectedJobTitle}
            onChange={(e) => setSelectedJobTitle(e.target.value)}
          >
            <option value="">Job Title</option>
            {jobTitles.map((j) => (
              <option key={j} value={j}>{j}</option>
            ))}
          </select>

          <select
            className="px-3 py-2 border border-gray-300 rounded bg-white text-sm"
            value={selectedCompany}
            onChange={(e) => setSelectedCompany(e.target.value)}
          >
            <option value="">Company</option>
            {companies.map((c) => (
              <option key={c} value={c}>{c}</option>
            ))}
          </select>
        </div>
      </div>

      {/* Alumni List */}
      <div className="space-y-4 overflow-y-auto flex-1 pr-2">
        {filteredAlumni.map((person) => (
          <div
            key={person.id}
            className="flex items-center justify-between p-4 border border-gray-200 rounded-lg hover:bg-gray-50"
          >
            <div className="flex items-center space-x-4">
              <Image
                src={person.image || "/images/profile-icon.png"}
                alt={person.name}
                width={64}
                height={64}
                className="w-16 h-16 rounded-full object-cover"
              />
              <div>
                <h3 className="font-bold text-lg">{person.name}</h3>
                <p className="text-gray-600">
                  {person.title} {person.company && `@ ${person.company}`}
                </p>
                <p className="text-gray-500 text-sm">{person.university}</p>
              </div>
            </div>
            <button className="bg-code-kenya-red text-white px-4 py-2 rounded hover:bg-red-700 transition-colors">
              Connect
            </button>
          </div>
        ))}
        {filteredAlumni.length === 0 && (
          <p className="text-gray-500 text-center">No alumni match your filters.</p>
        )}
      </div>
    </div>
  )
}

export default AlumniDirectory
