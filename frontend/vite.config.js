import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'//added this 

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss(),],//added the tailwindcss() as one of the plungins here
  
})
