"""Test general searchprovider functionality."""
from cws.cws import Cws


class TestProvider():
    """Test searchproviders."""

    def test_fetch(self, provider_string):
        """Test if fetching requests works."""
        provider = Cws.providers[provider_string](25)
        result = provider.fetch_request('henk')

        assert isinstance(result, str)
