FROM python:3.8-slim
WORKDIR /app
ARG AZURE_SQL_URL
ENV AZURE_SQL_URL=${AZURE_SQL_URL}
COPY . /app
RUN pip install --no-cache-dir -r ./backend/requirements.txt
EXPOSE 8001
CMD ["uvicorn", "backend.api.newsAPI.main:app", "--host", "0.0.0.0", "--port", "8001"]