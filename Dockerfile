FROM node:20
WORKDIR /app
ARG SEARCH_DNS
ENV SEARCH_DNS=${SEARCH_DNS}
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]