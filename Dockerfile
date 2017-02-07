
FROM cseelye/rpi-nginx-base
MAINTAINER Carl Seelye <cseelye@gmail.com>
RUN apt-get update && apt-get install -y git
RUN mkdir -p  /home/pi/docker/
#clone repo
RUN git clone https://github.com/Benjamin117/LootGen.git /home/pi/docker/LootGen

RUN cp  /home/pi/docker/LootGen/api/systemd/system/LootGen.service /etc/systemd/system/
RUN mkdir /etc/nginx/sites-available/
RUN cp  /home/pi/docker/LootGen/api/nginx/sites-available/LootGen /etc/nginx/sites-available/
RUN rm /home/pi/docker/LootGen/api/nginx/sites-available/default 
RUN cp /home/pi/docker/LootGen/api/nginx/sites-available/default /etc/nginx/sites-available/
RUN mkdir /etc/nginx/sites-enabled/
RUN ln -s /etc/nginx/sites-available/LootGen /etc/nginx/sites-enabled
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled



# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
        && ln -sf /dev/stderr /var/log/nginx/error.log
EXPOSE 80
EXPOSE 81
