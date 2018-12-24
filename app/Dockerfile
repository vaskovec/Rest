FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

##########################################################################################################
#
#   Installing GOSU
#
##########################################################################################################
ENV GOSU_VERSION 1.10
RUN set -x \
    && apt-get update && apt-get install -y --no-install-recommends ca-certificates wget && rm -rf /var/lib/apt/lists/* \
    && dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \
    && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" \
    && wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
    && rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
    && chmod +xs /usr/local/bin/gosu \
    && gosu nobody true \
    && apt-get purge -y --auto-remove ca-certificates wget
##########################################################################################################
#
#   Installing SSHD in order to be able debug
#
##########################################################################################################
RUN apt-get update \
    && apt-get install -y openssh-server \
    && mkdir /var/run/sshd \
    && sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd \
    && /usr/bin/ssh-keygen -A

# ???
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

##########################################################################################################
#
#   Creating User Home directory and project folders
#
##########################################################################################################
# Create a dev user to use as the directory owner
ENV DJANGO_USER_GID 1000
ENV DJANGO_USER_UID 1000
ENV DJANGO_USER 'lab'
ENV DJANGO_USER_PASSWORD '8a388d6e-6d3a-4e14-bd0e-7e50c4da8ae9'
ENV DJANGO_USER_GROUP $DJANGO_USER
ENV PROJECT_PATH ./
ENV DJANGO_USER_SHELL '/bin/bash'

RUN set -x \
    && addgroup --gid ${DJANGO_USER_GID} ${DJANGO_USER_GROUP} \
    && adduser --system \
            --uid ${DJANGO_USER_UID} \
            --gid ${DJANGO_USER_GID} \
            --shell ${DJANGO_USER_SHELL} \
            ${DJANGO_USER} \
    && echo "${DJANGO_USER}:${DJANGO_USER_PASSWORD}" | chpasswd