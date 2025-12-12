FROM node:14-alpine

WORKDIR /app

#Entry point
#this helps when using the container as a utility container
#when we run the container, and let's say, we want to run the comman 'npm install', 
# we don't have to type the part specified in the below command
# ex: we have 'npm' specified in ENTRYPOINT, so when we run the container, we just have to type 'install' instead of 'npm install'
ENTRYPOINT [ "npm" ]