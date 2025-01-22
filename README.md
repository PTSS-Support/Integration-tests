# integration-tests
Integration tests for the PTSS-Support app microservices

## Setup

To set up the development environment for this project, follow these steps:

1. **Run the setup script**:
    ```sh
    python setup_vscode.py
    ```

2. **Activate the virtual environment**:
    - On Windows:
        ```sh
        .\.venv\Scripts\activate
        ```
    - On Unix/MacOS:
        ```sh
        source .venv/bin/activate
        ```

3. **Install required packages**:
    ```sh
    pip install -e .
    ```

4. **Restart VS Code** for changes to take effect.

## Configuration

The configuration for the integration tests is managed through YAML files and environment variables. The default configuration file is located at `configs/dev.yaml`.

### Environment Variables

You can override the default configuration by setting the following environment variables:

- `API_URL`: The base URL for the API.
- `TEST_USERNAME`: The username for test login.
- `TEST_PASSWORD`: The password for test login.
- `API_TIMEOUT`: The timeout for API requests.

### Example

To run the tests with custom configuration, you can set the environment variables before running the tests:

```sh
export API_URL="https://custom-api-url.com"
export TEST_USERNAME="custom_username"
export TEST_PASSWORD="custom_password"
export API_TIMEOUT=60
```

## Running Tests

To run the integration tests, use the following command:

```sh
pytest tests/integration -v
```

This will execute all the tests in the `tests/integration` directory and provide a verbose output.

## Test Reports

The test reports are generated in the `test-reports` directory with a timestamp. The reports include detailed information about the test execution and results.
