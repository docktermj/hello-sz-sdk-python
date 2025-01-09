# hello-sz-sdk-python

## Development

1. Identify git repository.

    ```console
    export GIT_ACCOUNT=docktermj
    export GIT_REPOSITORY=hello-sz-sdk-python
    export GIT_ACCOUNT_DIR=~/${GIT_ACCOUNT}.git
    export GIT_REPOSITORY_DIR="${GIT_ACCOUNT_DIR}/${GIT_REPOSITORY}"
    ```

1. Make virtual environment.

    ```console
    python3 -m venv ${GIT_REPOSITORY_DIR}/.venv
    ```

1. Activate virtual environment.

    ```console
    source ${GIT_REPOSITORY_DIR}/.venv/bin/activate
    ````

1. Install senzing packages.

    ```console
    python3 -m pip install senzing-grpc senzing-core mypy
    ```

1. Start Senzing gRPC service.

    ```console
    docker run -it --name senzing-serve-grpc -p 8261:8261 --read-only --rm senzing/serve-grpc:latest
    ```
