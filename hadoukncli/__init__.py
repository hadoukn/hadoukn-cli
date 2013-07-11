import sys
import argparse

from hadoukncli.config import get_config
from hadoukncli.commands.auth import login
from hadoukncli.commands.apps import apps_create


def run_command(argv=sys.argv):
    # get cli and user configs
    config = get_config()

    # CLI argument parser
    parser = argparse.ArgumentParser(description='Do stuff with Hadoukn.')
    subparsers = parser.add_subparsers(title='available sub-commands',
                                       help='sub-command help',
                                       dest='subparser')

    # login
    create_parser = subparsers.add_parser('login', help='login help')
    create_parser.set_defaults(func=login)

    # apps:create
    create_parser = subparsers.add_parser('apps:create', help='apps:create help')
    create_parser.add_argument('name', type=str, help='The name of your app.')
    create_parser.set_defaults(func=apps_create)

    args = parser.parse_args()
    args.func(args, config)
