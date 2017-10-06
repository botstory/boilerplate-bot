import os

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'version.txt')) as version_file:
    __version__ = version_file.read().strip()

# some general information about this bot

BOT_ID = 'boilerplatebot'

BOT_NAME = 'Boilerplate bot'

GITHUB_URL = 'https://github.com/botstory/boilerplate-bot/'

SHORT_INTO = 'Hello dear {{user_first_name}}!\n' \
             'I\'m ' + BOT_NAME + ' assistant based on BotStory framework.\n' \
             'I\'m here to help you to get boilerplate and make new bot from it.\n'

SHORT_HELP = SHORT_INTO + \
             '\n' \
             'All sources could be find here:\n' \
             ':package: ' + GITHUB_URL + ',\n' \
             'feedback and contribution are welcomed!'
