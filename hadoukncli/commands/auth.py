import getpass
import requests

from hadoukncli.config import get_config_file


#
# login
#

def login(args, config):
    # extract settings from the config files
    settings = config.get_dict()

    print('Enter your Hadoukn credentials.')
    username = raw_input("Username: ")
    password = getpass.getpass()

    # obtain the api_key from the server
    r = requests.get('%s/login' % settings['hadoukn']['api_url'],
                     auth=(username, password))

    if r.ok:
        # the json response represents a new/existing user
        user = r.json()

        print('Welcome, %s!' % user['username'])

        # get the main config file to write to
        config_file = get_config_file('hadoukncli.ini')

        # save off the credentials to our user config file
        config.set_dict('user', user)
        config.write(config_file)

        # close file
        config_file.close()
    else:
        error = r.json()
        print(error['msg'])
