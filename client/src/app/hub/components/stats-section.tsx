"use client";

import React, { useState, useEffect, useRef } from "react";

const useOnScreen = (ref: React.RefObject<Element>): boolean => {
  const [isIntersecting, setIntersecting] = useState(false);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => setIntersecting(entry.isIntersecting),
      { threshold: 0.5 }
    );

    if (ref.current) observer.observe(ref.current);
    return () => {
      if (ref.current) observer.unobserve(ref.current);
    };
  }, [ref]);

  return isIntersecting;
};

interface CountUpProps {
  target: number;
  trigger: boolean;
}

const CountUp: React.FC<CountUpProps> = ({ target, trigger }) => {
  const [count, setCount] = useState(0);
  const increment = target / 100;

  useEffect(() => {
    if (!trigger) {
      setCount(0);
      return;
    }

    let start = 0;
    const duration = 1500;
    const stepTime = duration / 100;
    const timer = setInterval(() => {
      start += increment;
      if (start >= target) {
        setCount(target);
        clearInterval(timer);
      } else {
        setCount(Math.floor(start));
      }
    }, stepTime);

    return () => clearInterval(timer);
  }, [target, trigger, increment]);

  return <>{count >= target ? target : count}</>;
};

interface Stat {
  number: number;
  label: string;
  color: string;
  suffix?: string;
}

const StatsSection: React.FC = () => {
  const stats: Stat[] = [
    { number: 20, label: "ALUMNI", color: "text-red-600", suffix: "+" },
    { number: 40, label: "SCHOLARS", color: "text-gray-400", suffix: "+" },
    { number: 12, label: "COUNTRIES REPRESENTED", color: "text-green-700", suffix: "+" },
  ];

  return (
    <section className="py-20 px-6 bg-gray-300">
      <div className="max-w-7xl mx-auto">
        <div className="grid md:grid-cols-3 gap-8 text-center">
          {stats.map(({ number, label, color, suffix }, index) => {
            const ref = useRef<HTMLDivElement>(null);
            const isVisible = useOnScreen(ref);

            return (
              <div key={index} ref={ref}>
                <div className={`text-8xl font-bold ${color} mb-4`}>
                  <CountUp target={number} trigger={isVisible} />
                  {suffix}
                </div>
                <div className="text-black font-semibold text-lg">{label}</div>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
};

export default StatsSection;
