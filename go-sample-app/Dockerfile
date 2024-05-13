FROM golang:1.19 as build

WORKDIR /app

COPY go.mod ./
COPY go.sum ./

RUN go mod download && go mod verify

COPY main.go ./

RUN CGO_ENABLED=0 go build -o /my-app
FROM gcr.io/distroless/static-debian12

COPY --from=build /my-app /my-app

EXPOSE 5000 8081

ENTRYPOINT ["/my-app"]