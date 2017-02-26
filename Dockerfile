FROM ioft/armhf-ubuntu
RUN apt-get update && apt-get install -y git python3 python3-pip python3-dev ng$
RUN pip3 install flask flask-cors


#clone repo
RUN git clone https://github.com/Benjamin117/LootGen.git /home/LootGen

RUN cp  /home/LootGen/api/nginx/sites-available/LootGen /etc/nginx/sites-availa$
RUN rm /etc/nginx/sites-available/default
RUN cp /home/LootGen/api/nginx/sites-available/default /etc/nginx/sites-availab$
RUN rm /etc/nginx/nginx.conf
RUN cp  /home/LootGen/api/nginx/nginx.conf /etc/nginx/

RUN ln -s /etc/nginx/sites-available/LootGen /etc/nginx/sites-enabled


EXPOSE 80
EXPOSE 81


CMD nginx
CMD uwsgi --ini /home/LootGen/api/LootGen.ini
