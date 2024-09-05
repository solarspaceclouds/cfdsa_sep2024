# example for compiled languages (e.g. golab;java)

FROM golang:1.23-bookworm AS builder
# container name set to 'builder'

LABEL maintainer="solarspace"

WORKDIR /src 

COPY /go.* . 
COPY main.go . 

RUN go build -o main. main.go 

# container to run the app 
FROM bookworm
LABEL maintainer="solarspace" 
WORKDIR /app 

RUN apt update && apk add curl -y

# copy the binary from the build container
COPY --from=builder /src/main . 
COPY public public 
COPY templates templates   

# TO RUN: 
ENV PORT=3000 INSTANCE_NAME=dov_bear_1234 INSTANCE_HASH=dov_bear_hash_1234

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \ 
    # CMD ["executable"]
    CMD curl -s localhost:${PORT}/healthz || exit 1
    #curl: 0 successful; 1,2,3, etc.==> unsuccessful

EXPOSE ${PORT}

SHELL ["bin/sh", "-c"]
ENTRYPOINT app/main/