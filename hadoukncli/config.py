from ConfigParser import ConfigParser


class HadouknConfigParser(ConfigParser):
    def dict(self):
        items = self.items('hadoukncli')

        settings = {}
        for k, v in items:
            settings[k] = v

        return settings
