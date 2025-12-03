# Dockerize Python Application

## Overview
This project demonstrates how to dockerize a Python application. It provides a step-by-step guide to create a Docker image and run the application in a container.

## Prerequisites
- Docker installed on your machine
- Basic knowledge of Python and Docker

## Getting Started

### Clone the Repository
```bash
git clone <repository-url>
cd docker-kub
```

### Build the Docker Image
```bash
docker build -t python-app .
```

### Run the Docker Container
```bash
docker run -d -p 5000:5000 python-app
```

## Usage
Access the application at `http://localhost:5000`.

## Contributing
Feel free to submit issues and pull requests.

## License
This project is licensed under the FREE License.  
