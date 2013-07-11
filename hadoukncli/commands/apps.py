import json
import requests


def apps_create(args, config):
    # extract settings from the config files
    settings = config.get_dict()

    url = '%s/apps' % settings['hadoukn']['api_url']
    params = {
        'api_key': settings['user']['api_key']
    }
    payload = {
        'name': args.name,
        'stack': 'cedar'
    }

    r = requests.post(url,
                      params=params,
                      data=json.dumps(payload))

    if r.ok:
        app = r.json()

        print('Created %s. stack is %s' % (app['name'], app['stack']))
        print('%s | %s' % (app['web_url'], app['git_url']))
    else:
        error = r.json()
        print(error['msg'])
