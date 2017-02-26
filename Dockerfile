FROM ioft/armhf-ubuntu
RUN apt-get update && apt-get install -y git python3 python3-pip python3-dev nginx
RUN pip3 install flask flask-cors uwsgi


#clone repo
RUN git clone https://github.com/Benjamin117/LootGen.git /home/LootGen && cd /home/LootGen && git checkout  661aa49

RUN cp  /home/LootGen/api/nginx/sites-available/LootGen /etc/nginx/sites-available
RUN rm /etc/nginx/sites-available/default
RUN cp /home/LootGen/api/nginx/sites-available/default /etc/nginx/sites-available
#RUN rm /etc/nginx/nginx.conf
#RUN cp  /home/LootGen/api/nginx/nginx.conf /etc/nginx/

RUN ln -s /etc/nginx/sites-available/LootGen /etc/nginx/sites-enabled


EXPOSE 80
EXPOSE 81


#ENTRYPOINT nginx
#ENTRYPOINT uwsgi --ini /home/LootGen/api/LootGen.ini
