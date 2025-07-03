import React from "react";

interface PricingFeature {
  text: string;
}

interface PricingPlan {
  label?: string;
  planThemeColor?: string;
  checkIconColor?: string;
  cycle?: string;
  iconBgColor?: string;
  textColor?: string;
  price: number;
  title: string;
  description: string;
  features: PricingFeature[];
  buttonColor: string;
  buttonShadow?: string;
  expandIcon?: boolean;
  paymentLink?: string;
}

const plans: PricingPlan[] = [
  {
    title: "Access Fee",
    planThemeColor: "primaryBlackColor",
    checkIconColor: "#000000ff",
    price: 8,
    cycle: "",
    iconBgColor: "bg-[#e0e0e0ff]",
    textColor: "text-primary-black-color",
    description:
      "Enjoy full access to the course with a flexible learning schedule designed for your convenience.",
    buttonColor: "bg-primary-black-color",
    buttonShadow: "shadow-[0_2px_10px_rgba(0,0,0,0.3)]",
    expandIcon: true,
    paymentLink:
      "https://payment.intasend.com/pay/08797697-634b-4158-9e97-bc3a60bf90e4/",
    features: [
      { text: "Access fee" },
      { text: "No Internship." },
      { text: "7 weeks online." },
    ],
  },
  {
    label: "Best value",
    title: "Pay Once – Save More",
    planThemeColor: "primaryRedColor",
    checkIconColor: "#ba0000ff",
    price: 500,
    cycle: "",
    iconBgColor: "bg-[#f7e1e1ff]",
    textColor: "text-primary-red-color",
    description:
      "Make a one-time payment and unlock the full benefits of your program.",
    buttonColor: "bg-primary-red-color",
    expandIcon: true,
    paymentLink:
      "https://payment.intasend.com/pay/c40406fd-3b36-447d-a566-806cfb9aef60/",
    features: [
      { text: "Guaranteed Internship." },
      { text: "Unlimited projects." },
      { text: "Free program resources." },
      { text: "Online or In-person." },
      { text: "One-time payment." },
      { text: "No Accommodation." },
      { text: "No Excursions + Safari." },
    ],
  },
  {
    title: "Buy Now, Pay Later",
    planThemeColor: "primaryGreenColor",
    checkIconColor: "#006600ff",
    price: 7000,
    iconBgColor: "bg-[#e1ede1ff]",
    textColor: "text-primary-green-color",
    cycle: "",
    description:
      "Start learning now and pay over time, with flexible repayment terms.",
    buttonColor: "bg-primary-green-color",
    expandIcon: true,
    paymentLink:
      "https://payment.intasend.com/pay/c40406fd-3b36-447d-a566-806cfb9aef60/",
    features: [
      { text: "No upfront costs." },
      { text: "Guaranteed Internship." },
      { text: "Instant course access." },
      { text: "4-star Accommodation." },
      { text: "Excursions + Safari." },
      { text: "In-Person Attendance." },
      { text: "Easy repayment tracking." },
      { text: "Automated reminders." },
    ],
  },
];

const PricingSection: React.FC = () => {
  return (
    <section className="py-16 bg-white">
      <div className="max-w-7xl mx-auto px-4">
        <h2 className="text-3xl font-bold text-center mb-10">Our Plans</h2>
        <div className="grid md:grid-cols-3 gap-8">
          {plans.map((plan, idx) => (
            <div
              key={idx}
              className="border rounded-xl p-6 shadow-md flex flex-col justify-between"
            >
              {plan.label && (
                <div className="mb-2 text-sm font-semibold text-red-600 uppercase">
                  {plan.label}
                </div>
              )}

              <div>
                <h3
                  className={`text-xl font-bold mb-2 ${
                    plan.textColor || "text-black"
                  }`}
                >
                  {plan.title}
                </h3>
                <p className="text-gray-600 mb-4">{plan.description}</p>
                <div className="text-4xl font-bold mb-2">${plan.price}</div>
              </div>

              <ul className="mb-6 mt-4 space-y-2">
                {plan.features.map((feature, index) => (
                  <li key={index} className="flex items-center text-gray-700">
                    <svg
                      className="w-5 h-5 mr-2 text-green-600"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth={2}
                      viewBox="0 0 24 24"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        d="M5 13l4 4L19 7"
                      />
                    </svg>
                    {feature.text}
                  </li>
                ))}
              </ul>

              {plan.paymentLink ? (
                <a
                  href={plan.paymentLink}
                  target="_blank"
                  rel="noopener noreferrer"
                  className={`block w-full ${plan.buttonColor} text-white rounded-full py-3 font-medium
                    ${plan.buttonShadow || ""} flex items-center justify-center gap-2 mb-2 hover:bg-opacity-90`}
                >
                  Pay Now
                  <svg
                    className="w-5 h-5"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M17 8l4 4m0 0l-4 4m4-4H3"
                    />
                  </svg>
                </a>
              ) : (
                <button
                  className={`w-full ${plan.buttonColor} text-white rounded-full py-3 font-medium
                    ${plan.buttonShadow || ""} flex items-center justify-center gap-2 mb-2 hover:bg-opacity-90`}
                >
                  Enroll Now
                  <svg
                    className="w-5 h-5"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M17 8l4 4m0 0l-4 4m4-4H3"
                    />
                  </svg>
                </button>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default PricingSection;
