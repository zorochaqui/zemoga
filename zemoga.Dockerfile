FROM python:3.9.5-buster

# TODO do I need to start from here with non-root user if I use multi-stage builds

RUN set -eu \
    && apt-get update \
    && apt-get dist-upgrade -y \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
ENV VIRTUAL_ENV /env
RUN python -m venv ${VIRTUAL_ENV}

# Set virtual env's bin folder as part of PATH
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

# TODO here a new FROM could be declared

# Create non-root user and group
ARG APP_USER=app
ENV USER $APP_USER
ENV GROUP $APP_USER
# RUN groupadd -r ${APP_USER} && \
#     useradd --no-log-init -r -g ${APP_USER} ${APP_USER}
RUN groupadd -r ${GROUP} && \
    useradd --no-log-init -r -g ${GROUP} ${USER}

# Copy code inside container
WORKDIR /app

COPY . /app/



# Set important environment variables
ENV PYTHONPATH /app

RUN chown -R ${GROUP}:${USER} /app

# Use non-root user and group
# USER ${APP_USER}:${APP_USER}
USER ${USER}:${GROUP}

# unbuffer stdout and stderr
ENV PYTHONUNBUFFERED 1

# port to use for the web application
ENV PORT 8000
EXPOSE $PORT

# Up using django lightweight server
# ENTRYPOINT [ "python" ]
# CMD [ "main.py" ]
CMD [ "python", "main.py"]
# CMD [ "python", "main.py", "0.0.0.0:8000" ]
# ENTRYPOINT [ "django-admin", "runserver", "0.0.0.0:8000" ]


# SHELL ["/bin/bash", "-c"]
# SHELL ["django-admin", "runserver", "0.0.0.0:${PORT}"]
# ENTRYPOINT ["exec", "django-admin", "runserver", "0.0.0.0:${PORT}"]


# TODO allow to make it hot reloading through importing files
# TODO take into account https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
