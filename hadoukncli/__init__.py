import sys
import argparse

from hadoukncli.config import get_config
from hadoukncli.commands.auth import login
from hadoukncli.commands.apps import apps_create
from hadoukncli.commands.keys import keys_add


def run_command(argv=sys.argv):
    # get cli and user configs
    config = get_config('hadoukncli.ini')

    # CLI argument parser
    parser = argparse.ArgumentParser(description='Do stuff with Hadoukn.')
    subparsers = parser.add_subparsers(title='available sub-commands',
                                       help='sub-command help',
                                       dest='subparser')

    # login
    login_parser = subparsers.add_parser('login',
                                         help='login help')
    login_parser.set_defaults(func=login)

    # apps:create
    create_parser = subparsers.add_parser('apps:create',
                                          help='apps:create help')
    create_parser.add_argument('name',
                               type=str,
                               help='The name of your app.')
    create_parser.set_defaults(func=apps_create)

    # keys:add
    keys_add_parser = subparsers.add_parser('keys:add', help='keys:add help')
    keys_add_parser.add_argument('keyfile',
                                 type=str,
                                 help='The keyfile to add.',
                                 nargs='?')
    keys_add_parser.set_defaults(func=keys_add)

    args = parser.parse_args()
    args.func(args, config)
