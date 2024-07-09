/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './*/templates/**/*.html'
  ],
  theme: {
    extend: {
      colors: {
        'brand': '#ef4444',
        'brand-hv': '#f87171',
        'brand-light':'#F9DFFF',
        'brand-dark': '#201A34',
        'brand-dark-xl': '#161E22',
      },
    },
    fontFamily: {
      'poppins': ['Poppins'],
      'roboto': ['Roboto'],
      'handlee': ['Handlee'],
      'pangolin': ['Pangolin'],
   }
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

