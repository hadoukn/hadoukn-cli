import json
import requests
import random
import string


# releases:add
#

def releases_add(args, config):
    # extract settings from the file
    settings = config.get_dict()

    length = 16
    random_string = ''.join([random.choice(string.ascii_uppercase + string.digits) for x in range(length)]).lower()
    repository = '%s/%s' % (args.name, random_string)

    payload = [
        {
            'id': random_string
        }
    ]
    url = '%s/v1/repositories/%s/images' % (settings['docker-registry']['registry_url'],
                                             repository)
    r = requests.put(url,
                     data=json.dumps(payload))
    import pdb;pdb.set_trace()
