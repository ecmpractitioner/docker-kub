FROM node:15

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 80

ENV MOMNGODB_USERNAME=manju
ENV MONGODB_PASSWORD=secret

CMD ["npm", "start"]

