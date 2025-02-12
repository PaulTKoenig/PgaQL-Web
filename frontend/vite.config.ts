import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vite.dev/config/
export default defineConfig({
  plugins: [svelte()],
  server: {
    host: '0.0.0.0', // This ensures Vite listens on all network interfaces
    port: 5173,       // The port Vite will be running on
  },
})
