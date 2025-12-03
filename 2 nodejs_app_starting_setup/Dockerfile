# Use the official Node.js 14 image based on Alpine Linux as a base image
FROM node:14-alpine 

# Before we run or perform any other action, it is a good habit to set the working directory
# All our cmmands and actions will be done in the working directory we set here
WORKDIR /app

# To optimize the image build process, first copy only the package.json and package-lock.json files
COPY package*.json /app/

# To further optimize, install dependencies before copying the rest of the application files

RUN npm install

# Next tell the docker which files from our local machine we want to copy into the image
# Here we copy all files from the current directory into the /app directory in the image

COPY . /app

# Next we need to expose the port on which our application will run inside the container
# This will allow us to map this port to a port on the host machine when we run a container based on this image

EXPOSE 80

# Next we need to start the application i.e. node application.
# The way to start a node application is to run the command 'node server.js'
# but we do not want to run this command during the build time of the image instead we want to run this command
# when a container is started based on this image. For that we use the CMD instruction as shown below
# Also, as a good prctice, CMD should be the last command in the Dockerfile

CMD ["node","server.js"]

# Now we have created the Dockerfile for our node application.
# How to build the image? explained in the main readme file.


