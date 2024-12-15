FROM python:3.12.1-slim-bullseye


ENV GECKODRIVER_BASE_URL="https://github.com/mozilla/geckodriver/releases/download"
ENV GECKODRIVER_VERSION="v0.35.0"


RUN apt update -y \
    && apt install -y firefox-esr wget \
    && wget $GECKODRIVER_BASE_URL/$GECKODRIVER_VERSION/geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz \
    && tar -xvzf geckodriver* \
    && mv geckodriver /usr/local/bin \
    && python3.12 -m pip install -U pip setuptools wheel \
    && python3.12 -m pip install selenium beautifulsoup4 \
    && apt remove -y wget g++ \
    && apt autoremove -y \
    && rm -rf geckodriver* /var/lib/apt/lists/deb.debian.*



# ### DEBUG
# RUN firefox --version
# RUN python3.12 -m pip freeze
