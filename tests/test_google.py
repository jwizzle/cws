# TODO Make tests more flexible and things
"""Test the Google provider."""
import pytest
from .clitools import setup_args
from cws.cws import Cws
from cws.config import cfg


class TestCLI():

    def test_search(self):
        """Test searching in dev env."""
        args = setup_args()
        cfg.env = args.env
        cws = Cws(args.url, args.provider, args.search, args.number)

        results = cws.start_search()
        print(results)

        # TODO Test something useful
        assert results
