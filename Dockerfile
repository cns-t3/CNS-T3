FROM node:20
WORKDIR /app
ARG NEXT_PUBLIC_SEARCH_DNS
ARG NEXT_PUBLIC_PERSON_DNS
ENV NEXT_PUBLIC_SEARCH_DNS=${NEXT_PUBLIC_SEARCH_DNS}
ENV NEXT_PUBLIC_PERSON_DNS=${NEXT_PUBLIC_PERSON_DNS}
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]