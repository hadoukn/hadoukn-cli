import getpass
import requests
import os.path


def run_login(args, settings):
    print('Enter your Hadoukn credentials.')

    username = raw_input("Username: ")
    password = getpass.getpass()

    # obtain the api_key from the server
    r = requests.get('%s/login' % settings['api_url'],
                     auth=(username, password))
    json_response = r.json()

    if 'api_key' in json_response:
        print('Welcome, %s!' % json_response['username'])

        # get the path to the current user's home dir
        home = os.path.expanduser('~')

        # store of the api_key into a file
        with open(os.path.join(home, '.hadoukn'), 'w') as f:
            f.write(json_response['api_key'])
    else:
        print('Login failed :(')
