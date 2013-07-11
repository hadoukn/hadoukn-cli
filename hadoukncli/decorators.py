from hadoukncli.exceptions import HadoukncliException


def logged_in(func):
    def wrapped(args, config):
        try:
            func(args, config)
        except HadoukncliException as e:
            print('FAILED: ' + e.msg)
    return wrapped
