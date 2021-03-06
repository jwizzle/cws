# Cws

CLI web search is a CLI search tool that shows the first N results from select search engines.

This started out because I wanted a way to play youtube video's in mpv without needing to open a browser first, because then why not watch it in my browser in the first place. I did find some similar projects but they just opened the results in my browser instead which was once again defeating the point.

The main use-cases are:
* Searching and fetching youtube/google/'whatever gets implemented' search results from the command line
* Executing default actions per search provider with the -x flag (see configuration), like opening youtube results in mpv
* Piping results to external commands to open/play results like your web browser or mpv for youtube

it heavily relies on [rapidapi](https://rapidapi.com/) endpoints for now. Which means you need to register and configure personal API tokens for this to work. See the [configuration](#configuration) section below for more info.

Development is done on irregular intervals, while heavily distracted so expect nothing.
This is currently a first usable version, that will probably change a lot. Core functionality should stay about the same though.

Todo (for now):
* -c flag that shows only 1 result and copies that
* Interactive mode that allows selection of result and applying an action like copy or open
* Add more search providers
* Possibly add some webscraping fallback for when no api's are configured or free limits are reached

## Installation

```bash
$ pip install cws_clisearch
```

## Configuration

Configuration is done through .yml files either in `$HOME` or `$XDG_HOME/cws/`.
There's 2 different config files, one mandatory and one optional:
* .cws_tokens.yml (mandatory)
* .cws_config.yml (optional)

### .cws_tokens.yml

This is where your [rapidapi](https://rapidapi.com/) tokens are loaded from.

Example:
```yaml
google: "$token" # Get it from https://rapidapi.com/apigeek/api/google-search3/
youtube: "$token" # Get it from https://rapidapi.com/marindelija/api/youtube-search-results/
```

Use the `--list-providers` option to list all posibilities.

### .cws_config.yml

This is where you override default settings of cws.

Example with defaults shown:
```yaml
default_provider: 'google'
provider:
  youtube:
    default_action: 'mpv'
  google:
    default_action: 'firefox'
```

## Usage

See `cws -h` for general usage information.

For now Google is the default search provider. The -x option implies -u and -n1, then pipes that output to whatever you want.
It's also safe to manually use the -u and -n1 options to pipe results. This does not work with mpv, just like `echo '$youtube_url' | mpv` wouldn't. Use -x as a work-around.
