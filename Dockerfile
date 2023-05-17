FROM python
RuN pip install flask
COPY app.py /
EXPOSE 8000

CMD python /app.py
