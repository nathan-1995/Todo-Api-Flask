# Get the base image
FROM node:20-alpine as build

# Set the working dir and 
WORKDIR /app
COPY package.json package-lock.json* ./

# Install the dependencies
RUN npm install

# Copy the entire dir
COPY . .

#Set arg and env variables
ARG VITE_BACKEND_URL
ENV VITE_BACKEND_URL=${VITE_BACKEND_URL}

# Build the application
RUN npm run build 

# Get the base image. Setup the nginx server
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

# Start the nginx server
CMD ["nginx", "-g", "daemon off;"]
