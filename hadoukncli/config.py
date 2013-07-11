import os.path

from ConfigParser import ConfigParser


def get_config_file():
    # get the settings
    package_root = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(package_root, 'hadoukncli.ini')

    return open(config_path, 'r+')


def get_config():
    config_file = get_config_file()

    # parse the the user settings file, and form a dict from it
    config = HadoukncliConfigParser()
    config.readfp(config_file)

    # close file
    config_file.close()
    return config


class HadoukncliConfigParser(ConfigParser):
    def get_dict(self):
        sections = self.sections()

        # convert a INI file into a dict
        settings = {}
        for section in sections:
            items = self.items(section)

            settings[section] = {}
            for k, v in items:
                settings[section][k] = v

        return settings

    def set_dict(self, section, params):
        # if the section doesn't exist add it
        if not section in self.sections():
            self.add_section(section)

        # convert a dict into INI settings
        for k, v in params.items():
            self.set(section, k, v)
