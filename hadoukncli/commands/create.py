import requests

from hadoukncli.decorators import logged_in


@logged_in
def run_create(args, config):
    # extract settings from the config files
    settings = config.get_dict()

    url = '%s/' % settings['hadoukn']['api_url']
    payload = {
        'api_key': settings['user']['api_key']
    }

    r = requests.post(url,
                      params=payload)
