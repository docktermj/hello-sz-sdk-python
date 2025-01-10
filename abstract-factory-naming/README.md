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

## Modes

1. **core:** Uses one instance of `senzing_core`.
1. **grpc:** Uses one instance of `senzing_grpc`.
1. **duo:** Uses one instance of either `senzing_core` or `senzing_grpc`.
1. **both:** Uses two instances comprised of both `senzing_core` and `senzing_grpc`.

## Use cases

1. Writing in either gRPC or Core. (**grpc** or **core**)
1. Writing in gRPC and migrating to Core. (**grpc** and **core**)
1. Writing a script that talks either to gRPC or Core (**duo**)
1. Writing a script that talks to both gRPC and Core (**both**)

## Styles

### Style 1

| package      | Variable            | AS |
| ------------ | ------------------- | -- |
| senzing      | `SzAbstractFactory` |    |
| senzing_core | `SzAbstractFactory` |    |
| senzing_grpc | `SzAbstractFactory` |    |

1. Currently testable.
1. Pros:
    1. Simplifies "diff-ing" files
1. Cons:
    1. This style falls apart when a `from senzing import SzAbstractFactory` is in the code.
    1. Can't use this style in "both" mode.
    1. Can cause confusion when using as there is no differentiation between interface and implementation.
    1. In "duo" mode, drives `pylance` crazy.

### Style 2

| package      | Variable            | AS                       |
|--------------|---------------------|--------------------------|
| senzing      | `SzAbstractFactory` |                          |
| senzing_core | `SzAbstractFactory` | `SzAbstractFactoryCore`  |
| senzing_grpc | `SzAbstractFactory` | `SzAbstractFactoryGrpc`  |

1. Currently testable.
1. Pros:
1. Cons:
    1. User can choose value of "AS", so searching on the web won't be easy.

### Style 3

| package      | Variable                | AS |
|--------------|-------------------------|----|
| senzing      | `SzAbstractFactory`     |    |
| senzing_core | `SzAbstractFactoryCore` |    |
| senzing_grpc | `SzAbstractFactoryGrpc` |    |

1. Currently not testable.
1. Pros:
    1. Very explicit class names. (No two classes have the same name)
    1. Reduces import complexity.
    1. Reduces ambiguity.
1. Cons:
    1. Makes migrating use-case a little more involved. AbstractFactory class changes.

### Style 4

| package      | Variable                | AS                   |
|--------------|-------------------------|----------------------|
| senzing      | `SzAbstractFactory`     |                      |
| senzing_core | `SzAbstractFactoryCore` | `SzAbstractFactory`  |
| senzing_grpc | `SzAbstractFactoryGrpc` | `SzAbstractFactory`  |

1. Currently not testable.
1. Pros:
    1. Simplifies the migration use-case.
1. Cons:
    1. This style falls apart when a `from senzing import SzAbstractFactory` is in the code.
    1. Can't use this style in "both" mode.
    1. User can choose value of "AS", so searching on the web won't be easy.

## Recommendation

1. Use style #3
