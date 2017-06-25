FROM python:3
RUN pip install gunicorn gevent flask flask-cors pandas xlsxwriter

ADD app/config.py /etc/gunicorn/config.py
ADD app /app 

EXPOSE 80
CMD  ["gunicorn","--config=/etc/gunicorn/config.py","wsgi:app"]
