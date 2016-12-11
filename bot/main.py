import asyncio
import botstory
from botstory.integrations import aiohttp, fb, mongodb
from botstory.integrations.ga import tracker
import logging
import os

from . import stories

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('echo-bot')
logger.setLevel(logging.DEBUG)

story = None


def init(auto_start, fake_http_session):
    global story
    story = botstory.Story()
    stories.setup(story)

    story.use(fb.FBInterface(
        # will show on initial screen
        greeting_text='Hello dear {{user_first_name}}! '
                      'I'' m demo bot of BotStory framework.',
        # you should get on admin panel for the Messenger Product in Token Generation section
        page_access_token=os.environ.get('FB_ACCESS_TOKEN', 'TEST_TOKEN'),
        # menu of the bot that user has access all the time
        persistent_menu=[{
            'type': 'postback',
            'title': 'Monkey Business',
            'payload': 'MONKEY_BUSINESS'
        }, {
            'type': 'web_url',
            'title': 'Source Code',
            'url': 'https://github.com/botstory/bot-story/'
        }],
        # should be the same as in admin panel for the Webhook Product
        webhook_url='/webhook{}'.format(os.environ.get('FB_WEBHOOK_URL_SECRET_PART', '')),
        webhook_token=os.environ.get('FB_WEBHOOK_TOKEN', None),
    ))

    # Interface for HTTP
    http = story.use(aiohttp.AioHttpInterface(
        port=os.environ.get('API_PORT', 8080),
        auto_start=auto_start,
    ))

    # User and Session storage
    story.use(mongodb.MongodbInterface(
        uri=os.environ.get('MONGODB_URI', 'mongo'),
        db_name=os.environ.get('MONGODB_DB_NAME', 'echobot'),
    ))

    story.use(tracker.GAStatistics(
        tracking_id=os.environ.get('GA_ID'),
    ))

    # for test purpose
    http.session = fake_http_session

    # connect bot specific stories

    logger.debug('story.stories_library.message_handling_stories')
    logger.debug(story.stories_library.message_handling_stories)

    return http


async def setup(fake_http_session=None):
    logger.info('setup')
    init(auto_start=False, fake_http_session=fake_http_session)
    await story.setup()


async def start(auto_start=True, fake_http_session=None):
    http = init(auto_start, fake_http_session)
    # start bot
    await story.start()

    logger.info('started')

    return http.app


async def stop():
    logger.info('stop')
    await story.stop()
    story.clear()


def main(forever=True):
    logging.basicConfig(level=logging.DEBUG)

    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(start(auto_start=forever))

    # and run forever
    if forever:
        story.forever(loop)

    # or you can use gunicorn for an app of http interface
    return app


if __name__ == '__main__':
    main(forever=True)
