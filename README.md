# Django Template Project

`app` contains the source code for the Django application.
`integration_tests` contains the source code for integration tests.

## Django Applications in `app`

### 1. Leads

The `leads` app provides endpoints to manage shopping leads. It includes the following functionalities:

- **Get all leads**: Retrieve a list of all leads.
- **Create a lead**: Add a new lead.
- **Checkout a lead**: Mark a lead as closed and create an outbox item for further processing.

Endpoints:
- `GET /leads`: Get all leads.
- `POST /leads`: Create a new lead.
- `PUT /leads/<lead_id>/checkout`: Checkout a lead.

### 4. Outbox

The `outbox` app handles the outbox pattern, ensuring reliable message delivery to external systems. It includes the following functionalities:

- **Create and publish outbox items**: Manage the creation and publishing of outbox items.

## Running the Project

### Prerequisites

- Docker
- Docker Compose

### Setup

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Set up environment variables**:
    Create a `.env` file in the `app` directory with the necessary environment variables.

3. **Build and run the Docker containers**:
    ```sh
    make run
    ```

### Running Integration Tests

The `integration_tests` directory contains a setup to make requests to the `app` to test its behavior.
It runs a isolated version of `app` in containers and executes tests using `pytest`.

1. **Run the integration tests**:
    ```sh
    make integration-tests
    ```

## Queue Handling

The `compose.yml` file includes configurations for publishers and consumers that are responsible for handling queue messages. These components ensure reliable message delivery and processing. Some apps contain callbacks that are used by these publishers and consumers to handle specific tasks.

## Additional Commands

- **Add a dependency**:
    ```sh
    make add-dependency dep=<dependency-name>
    ```

- **Rebuild the Docker containers**:
    ```sh
    make rebuild
    ```

- **Restart the Docker containers**:
    ```sh
    make restart
    ```

- **Restart the web service**:
    ```sh
    make restart-web
    ```

- **Stop and remove the Docker containers**:
    ```sh
    make down
    ```

- **Open a Django shell**:
    ```sh
    make shell
    ```

