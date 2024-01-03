module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./node_modules/flowbite/**/*.js"
  ],
  darkMode: 'class',
  
  theme: {
    extend: {
      colors: {
        'bg-app': '#2E0249',
        'custom-red': '#ff0000',
        'custom-green': '#00ff00',
      },
      backgroundColor:{
        'dark': '#333',
      },
      textColor:{
        'dark': '#fff',
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}