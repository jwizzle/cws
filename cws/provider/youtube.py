"""Youtube search provider."""
from cws.provider.searchprovider import SearchProvider
from cws.config import cfg


class Youtube(SearchProvider):
    """Youtube search provider.

    Extends the SearchProvider base class to handle Youtube results.
    """

    name = 'youtube'
    search_url = "https://youtube-search-results.p.rapidapi.com/youtube-search/"
    token_url = 'https://rapidapi.com/marindelija/api/youtube-search-results/'
    headers = {
        'x-rapidapi-key': cfg.tokens[name],
        'x-rapidapi-host': "youtube-search-results.p.rapidapi.com"
    }
    param_search_key = 'q'
    result_key = 'items'
    description_key = 'duration'
    link_key = 'url'
