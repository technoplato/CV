# Use the official Node.js image as a base image
FROM node:14

# Set the working directory inside the container
WORKDIR /usr/src/tests

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install the dependencies and nodemon globally
RUN npm install
RUN npm install -g nodemon

# Copy the rest of the code to the working directory
COPY . .

# Start nodemon
CMD [ "nodemon" ]