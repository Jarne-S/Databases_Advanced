FROM python:latest

RUN pip install bs4
RUN pip install pymongo
RUN pip install redis
RUN pip install requests
RUN pip install datetime

COPY webscraper.py ./webscraper.py

CMD [ "python", "./webscraper.py" ]