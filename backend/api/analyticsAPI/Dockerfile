FROM python:3.10-slim
WORKDIR /app
ARG OPENAI_API_KEY
ENV OPENAI_API_KEY=${OPENAI_API_KEY}
COPY . /app
RUN pip install --no-cache-dir -r ./backend/requirements.txt
EXPOSE 8004
CMD ["uvicorn", "backend.api.analytics.main:app", "--host", "0.0.0.0", "--port", "8004"]