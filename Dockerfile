


FROM cseelye/rpi-nginx-base
MAINTAINER Carl Seelye <cseelye@gmail.com>


RUN apt-get update && \
    apt-get --assume-yes upgrade && \
    apt-get --assume-yes install curl python python-dev build-essential&& \
    # download and install setuptools
	curl -O https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py\
	python3 ez_setup.py\
	# download and install pip
	curl -O https://bootstrap.pypa.io/get-pip.py\
	python3 get-pip.py \
    pip install uwsgi && \
    pip install flask_restplus Flask-BasicAuth flask-cors requests && \
    mkdir --parents /app && \
    apt-get autoremove && \
    apt-get clean && \
    rm --force --recursive /var/lib/apt/lists/* /tmp/* /var/tmp/*
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY uwsgi-common.ini /etc/uwsgi/uwsgi-common.ini
COPY app.conf /etc/nginx/conf.d/app.conf

#clone repo
RUN git clone https://github.com/Benjamin117/LootGen.git /home/LootGen

COPY /home/LootGen/api/systemd /etc/systemd
COPY /home/LootGen/api/nginx /etc/nginx/



# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log
EXPOSE 80
EXPOSE 81

WORKDIR /app
CMD ["/usr/bin/supervisord"]