FROM python
RUN pip install flask
RUN pip install requests
RUN mkdir /data
COPY httpSenderServiceCustom.py /data
ENV FLASK_APP httpSenderServiceCustom.py
CMD flask run --host=0.0.0.0 --port=80