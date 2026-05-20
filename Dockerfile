# syntax=docker/dockerfile:1.7

FROM golang:1.25-alpine AS builder

WORKDIR /src

RUN apk add --no-cache git ca-certificates

COPY go.mod go.sum ./
RUN go mod download

COPY . .

ARG BUILD_VERSION=docker
RUN CGO_ENABLED=0 GOOS=linux go build \
    -ldflags="-s -w -X main.buildString=${BUILD_VERSION}" \
    -o /out/server ./cmd/server


FROM alpine:3.20

RUN apk add --no-cache ca-certificates tzdata curl \
    && addgroup -S app && adduser -S -G app app

WORKDIR /app

COPY --from=builder /out/server /app/server

USER app

EXPOSE 8080

ENV ADDR=:8080 \
    BASE_URL=http://localhost:8080 \
    CONTENT_DIR=/data/content \
    GIT_DATA_PATH=/data/git

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
    CMD curl -fsS http://localhost:8080/health || exit 1

ENTRYPOINT ["/app/server"]
