"""Youtube search provider."""
from cws.provider.searchprovider import SearchProvider


class Youtube(SearchProvider):
    """Youtube search provider.

    Extends the SearchProvider base class to handle Youtube results.
    """

    name = 'youtube'
    search_url = "https://youtube-search-results.p.rapidapi.com/youtube-search/"
    token_url = 'https://rapidapi.com/marindelija/api/youtube-search-results/'
    headers = {
        'x-rapidapi-host': "youtube-search-results.p.rapidapi.com"
    }
    param_search_key = 'q'
    result_key = 'items'
    description_key = 'duration'
    link_key = 'url'
    filter_key = 'type'
    filter = ['video']
