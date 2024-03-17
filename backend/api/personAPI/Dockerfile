FROM python:3.8-slim
WORKDIR /app
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl gnupg2 apt-transport-https && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y unixodbc unixodbc-dev msodbcsql18 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
ARG AZURE_SQL_URL
ENV AZURE_SQL_URL=${AZURE_SQL_URL}
COPY . /app
RUN pip install --no-cache-dir -r ./backend/requirements.txt
EXPOSE 8001
CMD ["uvicorn", "backend.api.personAPI.main:app", "--host", "0.0.0.0", "--port", "8001"]