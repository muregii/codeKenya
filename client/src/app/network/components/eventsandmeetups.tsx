import React from 'react'
import Button from '@/app/pages/components/Button'

interface Event {
  id: number
  title: string
  venue: string
  date: string
  time: string
  status: 'upcoming' | 'past'
  type: 'networking' | 'briefing' | 'welcome' | 'ceremony'
}

const EventsMeetups = () => {
  const events: Event[] = [
    {
      id: 1,
      title: "NETWORKING SESSION",
      venue: "NAIROBI ARBORETUM",
      date: "August 13",
      time: "8am-12noon",
      status: "upcoming",
      type: "networking"
    },
    {
      id: 2,
      title: "CRUCIAL BRIEFING SESSION",
      venue: "ONLINE ZOOM MEET",
      date: "August 5",
      time: "9pm-10pm",
      status: "upcoming",
      type: "briefing"
    },
    {
      id: 3,
      title: "COHORT 2 WELCOME",
      venue: "ONLINE ZOOM MEET",
      date: "July 20",
      time: "8pm-10pm",
      status: "past",
      type: "welcome"
    },
    {
      id: 4,
      title: "COHORT 1 CEREMONY",
      venue: "NAIROBI ARBORETUM",
      date: "July 10",
      time: "8am-2pm",
      status: "past",
      type: "ceremony"
    }
  ]

  const upcomingEvents = events.filter(event => event.status === 'upcoming')
  const pastEvents = events.filter(event => event.status === 'past')

  return (
    <section>
      <h2 className="text-2xl font-bold mb-8">EVENTS AND MEETUPS</h2>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {upcomingEvents.map((event) => (
          <div key={event.id} className="bg-white rounded-lg shadow-md p-6 border-l-4 border-code-kenya-green">
            <div className="bg-code-kenya-green text-white px-3 py-1 rounded-full text-sm font-medium mb-4 inline-block">
              <Button
                type="button"
                title="Upcoming"
                variant="btn_green ml-4"
              />

            </div>
            <h3 className="font-bold text-lg mb-2">{event.title}</h3>
            <p className="text-gray-600 text-sm mb-1">VENUE: {event.venue}</p>
            <p className="text-gray-600 text-sm mb-4">{event.date} {event.time}</p>
            <button className="text-code-kenya-red font-medium hover:underline">
              Register
            </button>
          </div>
        ))}

        {pastEvents.map((event) => (
          <div key={event.id} className="bg-white rounded-lg shadow-md p-6 border-l-4 border-gray-400">
            <div className="text-white px-3 py-1 rounded-full text-sm font-medium mb-4 inline-block">
              <Button
                type="button"
                title="Past"
                variant="btn_red ml-6"
              />
            </div>
            <h3 className="font-bold text-lg mb-2">{event.title}</h3>
            <p className="text-gray-600 text-sm mb-1">VENUE: {event.venue}</p>
            <p className="text-gray-600 text-sm mb-4">{event.date} {event.time}</p>
            <button className="text-code-kenya-red font-medium hover:underline">
              View Details
            </button>
          </div>
        ))}
      </div>
    </section>
  )
}

export default EventsMeetups
