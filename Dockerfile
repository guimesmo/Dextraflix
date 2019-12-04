FROM python:3.7-alpine

COPY ./requirements ./requirements
RUN pip3 install -r ./requirements/requirements.txt
COPY ./setup.py ./README.md ./
COPY ./dextraflix ./dextraflix 
RUN python3 ./setup.py sdist install
ENV FLASK_ENV="development"
ENTRYPOINT [ "python3", "-m", "dextraflix.app" ]
EXPOSE 5000