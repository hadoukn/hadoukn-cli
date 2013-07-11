class HadoukncliException(Exception):
    def __init__(self, msg):
        self.msg = msg


class HadoukncliBadRequest(HadoukncliException):
    pass
