import pytest
import sys
from pathlib import Path
from datetime import datetime

def main():
    """
    Main entry point for running integration tests.
    Handles test execution, reporting, and exit codes.
    """
    # Set up the test environment
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_dir = Path("test-reports") / timestamp
    report_dir.mkdir(parents=True, exist_ok=True)

    # Build pytest arguments
    pytest_args = [
        "--verbose",
        "--capture=no",
        f"--html={report_dir}/report.html",
        "tests/integration"
    ]

    # Run the tests and return the exit code
    return pytest.main(pytest_args)

if __name__ == "__main__":
    sys.exit(main())