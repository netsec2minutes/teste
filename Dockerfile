FROM node:alpine

WORKDIR /home/lab/dso/devsecops-teste/app1

COPY package*.json ./

RUN npm install

COPY . .

COPY --chown=node:node . .
ADD file1 file2
USER node

EXPOSE 3000

CMD [ "node", "index.js" ]
