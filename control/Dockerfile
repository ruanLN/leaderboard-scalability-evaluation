FROM python:3

EXPOSE 8000

COPY ./ /app
WORKDIR /app
RUN pip install -r app/requirements.txt


ENTRYPOINT ["/app/app/scripts/start.sh"]
