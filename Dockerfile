# 
FROM python:3.9.0-slim as requirements-stage

# 
WORKDIR /temp

# 
RUN pip install --upgrade pip
RUN pip install poetry

# 
COPY pyproject.toml poetry.lock* /temp/

# 
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# 
FROM python:3.9.0-slim

# 
WORKDIR /code

# 
COPY --from=requirements-stage /temp/requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir -r /code/requirements.txt

# 
COPY ./api /code/api
COPY ./core /code/core
COPY ./schemes /code/schemes
COPY ./main.py /code
COPY ./pyproject.toml /code
COPY ./setup.cfg /code

RUN mkdir -p /code/static

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

EXPOSE 8000