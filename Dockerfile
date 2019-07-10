FROM python:3.6-slim
RUN mkdir -p /app
ENV APP_HOME /app
COPY ./ $APP_HOME
WORKDIR $APP_HOME
ENTRYPOINT ["python", "less_than_zero.py"]