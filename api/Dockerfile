FROM tiangolo/uwsgi-nginx-flask:flask-python3.5
RUN rm main.py
RUN rm uwsgi.ini
COPY  main.py /app/main.py
COPY  uwsgi.ini /app/uwsgi.ini

#clone repo
#RUN git clone https://github.com/Benjamin117/LootGen.git /app && cd /home/LootGen && git checkout a672098 

#EXPOSE 81
