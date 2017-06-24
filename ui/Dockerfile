FROM nginx

RUN rm -v /etc/nginx/conf.d/default.conf
RUN rm -v /etc/nginx/nginx.conf

COPY /home/benjamin/Documents/LootGen/ui/html/nginx.conf /etc/nginx
VOLUME /home/benjamin/Documents/LootGen/ui/html /usr/share/nginx/html

EXPOSE 80

CMD service nginx start