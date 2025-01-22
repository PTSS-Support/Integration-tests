import requests
from urllib.parse import urljoin
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)

class ApiClient:
    """
    HTTP client for making API requests to the microservices.
    Handles authentication, request formatting, and response processing.
    """
    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
        self.token: Optional[str] = None

    def set_token(self, token: str) -> None:
        """Set the authentication token for subsequent requests."""
        self.token = token
        if token:
            self.session.headers.update({"Authorization": f"Bearer {token}"})

    def request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """
        Make an HTTP request to the API.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            **kwargs: Additional request parameters
            
        Returns:
            Response object from the request
        """
        url = urljoin(self.base_url, endpoint)
        kwargs.setdefault("timeout", self.timeout)
        
        # Log request details at debug level
        logger.debug(f"Making {method} request to {url}")
        
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        
        return response

    def close(self) -> None:
        """Close the session and clean up resources."""
        self.session.close()