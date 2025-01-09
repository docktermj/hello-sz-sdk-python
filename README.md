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

## Styles

### Style 1

| package      | Variable            | AS |
| ------------ | ------------------- | -- |
| senzing      | `SzAbstractFactory` |    |
| senzing_core | `SzAbstractFactory` |    |
| senzing_grpc | `SzAbstractFactory` |    |

1. This style falls apart when a `from senzing import SzAbstractFactory` is in the code.

### Style 2

|--------------|---------------------|--------------------------|
| senzing      | `SzAbstractFactory` |                          |
| senzing_core | `SzAbstractFactory` | as SzAbstractFactoryCore |
| senzing_grpc | `SzAbstractFactory` | as SzAbstractFactoryGrpc |

### Style 3

|--------------|-------------------------|--|
| senzing      | `SzAbstractFactory`     |  |
| senzing_core | `SzAbstractFactoryCore` |  |
| senzing_grpc | `SzAbstractFactoryGrpc` |  |

### Style 4

|--------------|-------------------------|----------------------|
| senzing      | `SzAbstractFactory`     |                      |
| senzing_core | `SzAbstractFactoryCore` | as SzAbstractFactory |
| senzing_grpc | `SzAbstractFactoryGrpc` | as SzAbstractFactory |
