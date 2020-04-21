FROM python:3-alpine

COPY . /app
# Create and change to the app directory.
WORKDIR /app

RUN pip install -r requirements.txt
# Service must listen to $PORT environment variable.
# This default value facilitates local development.
ENV PORT 8080

# Run the web service on container startup.
CMD [ "python", "app.py" ]
