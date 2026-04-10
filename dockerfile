package com.example;
Dockerfile
FROM eclipse-temurin:17-jdk
WORKDIR /app
COPY target/app.jar app.jar
ENTRYPOINT ["java","-jar","app.jar"]
docker build -t springboot-app .
docker run -p 8080:8080 springboot-app