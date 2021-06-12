"""Google search provider."""
from cws.provider.searchprovider import SearchProvider


class Google(SearchProvider):
    """Google search provider.

    Extends the SearchProvider base class to handle Google results.
    """

    search_url = "https://google-search3.p.rapidapi.com/api/v1/search/q={}k&num={}"
    name = 'google'
    token_url = 'https://rapidapi.com/apigeek/api/google-search3/'
    headers = {
        'x-rapidapi-host': "google-search3.p.rapidapi.com"
    }
