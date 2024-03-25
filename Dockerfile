FROM python:3.9-slim

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["python", "run.py"]


FROM postgres:latest


ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=admin
ENV POSTGRES_DB=university_courses

EXPOSE 5432

CMD ["postgres"]