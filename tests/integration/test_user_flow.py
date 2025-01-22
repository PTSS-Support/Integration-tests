import pytest
from integration_tests.utils.http_client import ApiClient
from integration_tests.config import Config

class TestUserFlow:
    @pytest.fixture(scope="class")
    def config(self):
        """Load test configuration"""
        return Config(env="dev")
    
    @pytest.fixture(scope="class")
    def api_client(self, config):
        """Create and configure API client"""
        client = ApiClient(config.base_url)
        yield client
        client.close()
    
    def test_complete_user_flow(self, api_client, config):
        """
        Test the complete user flow:
        1. Login through the gateway
        2. Send a message in the groupchat
        3. Get all tools
        """
        # Step 1: Login
        login_payload = {
            "email": config.test_email,
            "password": config.test_password
        }
        login_response = api_client.request(
            "POST",
            config.api_endpoints["login"],
            json=login_payload
        )
        
        # Extract the access token from cookies
        cookies = login_response.cookies
        assert 'access_token' in cookies, "Login failed: No access token received"
        
        # Update session cookies for subsequent requests
        api_client.session.cookies.update(cookies)
        
        # Step 2: Send message in groupchat
        message_payload = {
            "content": "Kees heeft volgende week weer een afspraak bij de therapeut. "
                      "Wie gaat er dit keer met hem mee? Hij zei dat hij liever niet alleen wil gaan."
        }
        message_response = api_client.request(
            "POST",
            config.api_endpoints["message"],
            json=message_payload
        )
        assert message_response.status_code == 200, "Failed to send message"
        
        # Step 3: Get all tools
        tools_response = api_client.request("GET", config.api_endpoints["tools"])
        assert tools_response.status_code == 200, "Failed to retrieve tools"
        tools_data = tools_response.json()
        assert isinstance(tools_data, list), "Tools response should be a list"