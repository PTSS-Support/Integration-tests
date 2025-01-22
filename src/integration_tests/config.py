import os
import yaml
from pathlib import Path
import uuid
import getpass

class Config:
    """
    Handles configuration loading and environment-specific settings for integration tests.
    Supports both YAML config files and environment variable overrides.
    
    This class provides a consistent way to manage test configuration across different
    operating systems and environments. It handles:
    - Loading environment-specific YAML configurations
    - Environment variable overrides for flexibility
    - Cross-platform user identification
    - Secure default test credentials
    """
    def __init__(self, env="dev"):
        # Get the root project directory
        project_root = Path(__file__).parent.parent.parent
        config_path = project_root / "configs" / f"{env}.yaml"
        
        # Load the environment-specific configuration
        with open(config_path) as f:
            self._config = yaml.safe_load(f)

        # Allow environment variables to override configuration
        self.base_url = os.getenv("API_URL", self._config["api"]["base_url"])
        self.test_email = os.getenv("TEST_EMAIL", "test123@example.com")
        self.test_password = os.getenv("TEST_PASSWORD", "TestPass123!")
        
        # Additional configuration properties
        self.timeout = int(os.getenv("API_TIMEOUT", self._config["api"].get("timeout", 30)))
        self.environment = env

    @property
    def api_endpoints(self):
        """
        Provides access to configured API endpoints.
        Returns a dictionary of endpoint configurations from the YAML file.
        """
        return self._config["api"]["endpoints"]
    
    @property
    def test_data(self):
        """
        Provides access to test-specific data configurations.
        Returns the test_data section from the YAML file.
        """
        return self._config.get("test_data", {})