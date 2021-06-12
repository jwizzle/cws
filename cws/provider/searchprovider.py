"""Base search provider."""
import json
import requests
from abc import ABC
from cws.searchresponse import SearchResponse
from cws.searchresult import SearchResult
from cws.config import cfg


class SearchProvider(ABC):
    """Abstract base for searchproviders."""

    search_url = ''
    headers = {}
    params = {}
    name = ''
    token_url = 'https://rapidapi.com/'
    param_search_key = False
    result_key = ''
    title_key = 'title'
    description_key = 'description'
    link_key = 'link'
    filter_key = False
    filter = []

    def __init__(self, number, *args, **kwargs):
        """Construct the searchprovider."""
        self.number = number
        try:
            self.default_action = cfg.userconfig['provider'][self.name]['default_action']
        except KeyError:
            pass

    def fetch_request(self, search):
        """Fetch a request from the API.

        Args:
            search: The search to perform

        Returns:
            str: An API response as a string
        """
        if cfg.env == 'prod':
            if self.param_search_key:
                self.params = {self.param_search_key: search}
            else:
                self.search_url = self.search_url.format(
                    search, self.number
                )

            return requests.get(
                        self.search_url,
                        headers=self.headers,
                        params=self.params
                    ).text
        else:
            with open(cfg.sample_path / f"{self.name}.json", 'r') as file:
                return file.read()

    def parse_request(self, js, search):
        """Generate searchresults from response json.

        Args:
            js: The json object to parse

        Yields:
            SearchResult: A searchresult object
        """
        itemcount = 0
        for item in js[self.result_key]:
            if itemcount >= self.number:
                continue

            if self.filter_key and len(self.filter) > 0:
                if not item[self.filter_key] in self.filter:
                    continue

            itemcount += 1
            yield SearchResult(
                search,
                title=item[self.title_key],
                description=item[self.description_key],
                link=item[self.link_key]
            )

    def search(self, search, url_only):
        """Get results from the provider.

        Calls the internal scrape() to generate a response.

        Args:
            search: The search query to perform.
            url_only: Bool indicating to return urls only.

        Returns:
            SearchResponse: A SearchResponse object with results.
        """
        request = self.fetch_request(search)

        js = json.loads(request)

        try:
            result_list = [SearchResult(search, **i) for i in js['results']]
        except TypeError:
            result_list = [i for i in self.parse_request(js, search)]

        return SearchResponse(result_list, url_only)
