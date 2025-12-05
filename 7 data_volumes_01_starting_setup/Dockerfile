
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package.json /app/

# Install dependencies
RUN npm install

# Copy application code
COPY . .

# Expose port
EXPOSE 80

# Define a volume for persistent feedback storage
# The feedback folder will be stored outside the container on the host machine
# This is an annonymous volume and it will be created automatically by Docker. But this volume, gets deleted when the container is removed.
# If the container was stopped and started again, the data will not persist.
# To have more control over the volume, we can create named volumes or bind mounts.
# Named volumes are created during docker run command using --volume or -v flag with a specific name.
# Bind mounts are created by specifying the host path along with the container path.
# Bind mounts are useful during development when you want to sync code between host and container.
# We as developers have more control over bind mounts as we can see and manage the files directly on the host machine.
# bind are created using absolute path on the host machine during docker run command.
# Example of named volume: VOLUME ["feedback_data:/app/feedback"]
# ex: docker run -d -p 3000:80  --name data_volumes_01 -v feedback:/app/feedback -v "D:\learn\docker&kub\learning\docker-kub\7 data_volumes_01_starting_setup:/app" sha256:ea7d6c4d36878d08514c4716975618bed9022b6a5ec8f646a92815372216444a
# the above example creates a bound mount but there is an issue. When the volumne is created, it overrides the existing files in the container path (/app) with the files from the host path. If the host path is empty, it will make the container path empty as well.
# in this case, the node_modules folder (which got created from npm install) will be missing in the container as it is not present on the host machine.
# To avoid this issue, we can use anonymous volume to retain the existing files in the container.
# ex: docker run -d -p 3000:80  --name data_volumes_01 -v feedback:/app/feedback -v "D:\learn\docker&kub\learning\docker-kub\7 data_volumes_01_starting_setup:/app" -v /app/node_modules sha256:ea7d6c4d36878d08514c4716975618bed9022b6a5ec8f646a92815372216444a
# note that in the above example, we have added another volume for /app/node_modules to retain the node_modules folder in the container.
# by creating bind mount, we are sharing our project folders. so, any change we make in our source will be immediatley deployed to container
VOLUME ["/app/feedback"]

# Start the Node.js application server
CMD ["node","server.js"]


