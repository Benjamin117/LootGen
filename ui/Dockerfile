FROM nginx

RUN rm -v /etc/nginx/conf.d/default.conf
RUN rm -v /etc/nginx/nginx.conf

COPY html/nginx.conf /etc/nginx
COPY html /usr/share/nginx/html
