FROM python:3.12-slim
RUN useradd --system --uid 10001 app
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && mkdir data && chown app data
COPY qa qa
USER 10001
ENV PYTHONDONTWRITEBYTECODE=1 QA_DB=/app/data/tickets.sqlite3 PORT=8080
CMD ["sh", "-c", "exec waitress-serve --listen=0.0.0.0:${PORT} --call qa.app:create_app"]
