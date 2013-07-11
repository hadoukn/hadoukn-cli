import os
import sys
import argparse

from hadoukncli.config import HadouknConfigParser
from hadoukncli.login import run_login
from hadoukncli.create import run_create


def run_command(argv=sys.argv):
    package_root = os.path.dirname(os.path.dirname(__file__))
    config_file = open(os.path.join(package_root, 'hadoukncli.ini'))

    # parse the file and make a dict out of it
    config = HadouknConfigParser()
    config.readfp(config_file, 'r')

    # all settings for hadoukncli
    settings = config.dict()

    # CLI argument parser
    parser = argparse.ArgumentParser(description='Do stuff with Hadoukn.')
    subparsers = parser.add_subparsers(title='available sub-commands',
                                       help='sub-command help',
                                       dest='subparser')

    # login
    create_parser = subparsers.add_parser('login', help='login help')
    create_parser.set_defaults(func=run_login)

    # create
    create_parser = subparsers.add_parser('create', help='create help')
    create_parser.add_argument('name', type=str, help='The name of your app.')
    create_parser.set_defaults(func=run_create)

    args = parser.parse_args()
    args.func(args, settings)
