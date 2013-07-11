import getpass
import requests

from hadoukncli.config import get_config_file


def run_login(args, config):
    # extract settings from the config files
    settings = config.get_dict()

    print('Enter your Hadoukn credentials.')
    username = raw_input("Username: ")
    password = getpass.getpass()

    # obtain the api_key from the server
    r = requests.get('%s/login' % settings['hadoukn']['api_url'],
                     auth=(username, password))
    json_response = r.json()

    if 'api_key' in json_response:
        print('Welcome, %s!' % json_response['username'])

        # get the main config file to write to
        config_file = get_config_file()

        # save off the credentials to our user config file
        config.set_dict('user', json_response)
        config.write(config_file)

        # close file
        config_file.close()
    else:
        print('Login failed :(')
