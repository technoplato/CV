FROM node:14

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install
RUN npm install -g ts-node nodemon

COPY . .

EXPOSE 4000

CMD [ "npm", "start" ]
