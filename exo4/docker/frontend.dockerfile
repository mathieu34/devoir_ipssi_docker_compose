FROM nginx:alpine

COPY frontend/src/index.html /usr/share/nginx/html/index.htm

EXPOSE 80




