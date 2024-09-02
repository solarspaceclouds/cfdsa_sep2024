FROM python:3.10.14-bookworm

# ARG NODE_VERSION=22
# FROM node:${NODE_VERSION}

# HOW to build

# Create a directory /app and cd /app
WORKDIR /app

COPY main.py .
COPY requirements.txt .
COPY utils.py .
COPY run.sh . 

# COPY package*.json . # can handle regex
COPY public public 
COPY templates templates

# install node modules # use ci or i
RUN pip3 install  --no-cache-dir -r requirements.txt

# HOW to run
ENV PORT=5000 INSTANCE_NAME="dov_bear" INSTANCE_HASH="dov_bear_hash"
# env variables: PORT, INSTANCE_NAME, INSTANCE_HASH

# The exposed port(s) # /tcp/udp
EXPOSE ${PORT}

# Run the app 
# note: main must be found in /app;
ENTRYPOINT python3 main.py