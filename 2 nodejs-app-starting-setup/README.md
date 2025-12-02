# Build a Docker image and run a container — quick steps

## Prerequisites
- Docker installed and running.
- A Dockerfile in your project root (or note its path).

## Build the image
1. From the directory containing the Dockerfile:
    ```bash
    docker build -t myapp:1.0 .
    ```
2. If Dockerfile is elsewhere or has a different name:
    ```bash
    docker build -f path/to/Dockerfile -t myorg/myapp:1.0 path/to/context
    ```
3. Common build options:
    - Use build args: `--build-arg NAME=value`
    - Force fresh build: `--no-cache`
    - Multi-stage target: `--target builder`
    - Pull latest base images: `--pull`

4. Verify the image:
    ```bash
    docker image ls
    ```

5. (Optional) Tag for registry and push:
    ```bash
    docker tag myapp:1.0 myrepo/myapp:1.0
    docker push myrepo/myapp:1.0
    ```

## Run the container
1. Quick run (foreground, remove when exit):
    ```bash
    docker run --rm -p 3000:3000 myapp:1.0
    ```
    - Format `-p <hostPort>:<containerPort>`. Ensure the Dockerfile `EXPOSE` matches the container port.

2. Run detached with a name:
    ```bash
    docker run -d --name myapp -p 80:3000 myapp:1.0
    ```

3. Common run options:
    - Environment variables: `-e KEY=value`
    - Mount volume: `-v /host/path:/container/path`
    - Restart policy: `--restart unless-stopped`
    - Interactive shell: `docker run -it --rm myapp:1.0 /bin/sh`

4. Manage running containers:
    - View logs: `docker logs -f myapp`
    - Exec into running container: `docker exec -it myapp /bin/sh`
    - Stop and remove:
      ```bash
      docker stop myapp
      docker rm myapp
      ```

## Troubleshooting tips
- If build fails, run with increased verbosity: `docker build --progress=plain ...`
- If port conflict: change host port (left side of `-p`).
- If files not updated in container, use a bind mount (`-v`) for development.

That's it — build with `docker build`, run with `docker run`, and use `docker logs` / `docker exec` to inspect and manage the container.