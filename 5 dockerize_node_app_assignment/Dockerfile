FROM node:18-alpine

WORKDIR /app

# To optimize the image build process, first copy only the package.json and package-lock.json files
COPY package*.json /app/

# command to install dependencies
RUN npm install

# command to copy files from host to container

COPY . /app

# command to expose port 80
EXPOSE 3000

# RUN command to start the application

CMD ["node","server.js"]