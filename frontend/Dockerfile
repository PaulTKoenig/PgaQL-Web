# Stage 1: Build the Svelte app
FROM node:23 AS builder

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json, then install dependencies
COPY package.json package-lock.json ./
RUN npm ci

# Copy the rest of the application and build the Svelte app
COPY . .
RUN npm run build

# Stage 2: Set up Nginx to serve the built app
FROM nginx:alpine

# Copy custom Nginx configuration into the container
# COPY nginx.conf /etc/nginx/nginx.conf

# Copy the built Svelte app (from the builder stage if using multi-stage)
COPY --from=builder /app/dist /usr/share/nginx/html

# Expose port 80 for Nginx
EXPOSE 80

# Run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]