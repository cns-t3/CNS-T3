/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
      colors: {
        beige: "#F9F9F7",
        red: "#E60000",
        cream: "#F4F3ED",
        grey: "#CDCDCC",
        darkgrey: "#ABABAB",
        textgrey: "#5B5D5C",
        green: "#2ecc71",
        orange: "#f39c12",
        lightestRed: "#fca5a5",
        lighterRed: "#f87171",
        lightRed: "#ef4444",
        mediumRed: "#dc2626",
        darkRed: "#b91c1c",
        darkerRed: "#991b1b",
        darkestRed: "#7f1d1d",
        lightestGrey: "#6B7280",
        lighterGrey: "#4B5563",
        midGrey: "#374151",
        darkerGrey: "#1F2937",
        darkestGrey: "#111827",
      },
    },
  },
  plugins: [],
};
