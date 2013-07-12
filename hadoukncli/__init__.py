from __future__ import print_function
import argparse
import os
import sys

from hadoukncli.config import get_config
from hadoukncli.commands.auth import login
from hadoukncli.commands.apps import apps_create
from hadoukncli.commands.keys import keys_add


def run_command(argv=sys.argv):
    # CLI argument parser
    parser = argparse.ArgumentParser(
        description=''
    )
    parser.add_argument(
        '-c',
        '--config',
        help=(
            'Path to the configuration file. If not specified then the '
            'lookup order will check for a HADOUKN_CONFIG environ '
            'variable, then fallback to .hadouknrc in the CWD.'
        ),
    )
    subparsers = parser.add_subparsers(
        title='available sub-commands',
        help='sub-command help',
        dest='subparser',
    )

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

    # get cli and user configs
    cfg_path = args.config
    if cfg_path is not None and not os.path.exists(cfg_path):
        print('Invalid path "{}" specified for the config file.'
              .format(cfg_path), file=sys.stderr)
        return 1

    config = get_config(cfg_path)

    args.func(args, config)
