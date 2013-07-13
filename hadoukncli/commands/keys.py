import os
import json
import requests

from subprocess import call
from hadoukncli.util import key_to_parts


#
# keys:add
#

def keys_add(args, config):
    if args.keyfile:
        associate_key(args, config, args.keyfile)
    else:
        associate_or_generate_ssh_key(args, config)


def associate_key(args, config, path):
    settings = config.get_dict()

    with open(path) as key:
        # split up the key
        key_type, key_key, key_comment = key_to_parts(key.read())

        url = '%s/keys' % settings['hadoukn']['api_url']
        params = {
            'api_key': settings['user']['api_key']
        }
        payload = {
            'key_key': key_key,
            'key_type': key_type,
            'key_comment': key_comment
        }

        r = requests.post(url,
                          params=params,
                          data=json.dumps(payload))

    if r.ok:
        print('Uploaded SSH public key!')
    else:
        error = r.json()
        print(error['msg'])


def generate_ssh_key(args, config, path):
    if not os.path.exists(path):
        call(['ssh-keygen', '-t', 'rsa', '-N', '""', '-f', path])


def associate_or_generate_ssh_key(args, config):
    home_directory = os.path.expanduser('~')
    ssh_key_path = os.path.join(home_directory, '.ssh', 'id_rsa.pub')

    if os.path.exists(ssh_key_path):
        print('Found existing public key: %s' % ssh_key_path)
        associate_key(args, config, ssh_key_path)
    else:
        print('Could not find an existing public key.')
        yn = raw_input('Would you like to generate one? [Yn]')

        if not yn.lower() == 'n':
            print('Generating new SSH public key.')
            generate_ssh_key(args, config, ssh_key_path)
            associate_key(args, config, ssh_key_path)
