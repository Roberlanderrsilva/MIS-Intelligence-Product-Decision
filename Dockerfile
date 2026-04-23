FROM python:3.9-slim
LABEL maintainer="Roberlander MIS Specialist"
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir pandas openpyxl
COPY . .
CMD ["python", "processamento_full_stack.py"]
