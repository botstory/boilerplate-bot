from botstory import chat, story
from botstory.middlewares import any, text
import logging

logger = logging.getLogger(__name__)

logger.debug('parse stories')


@story.on_start()
def on_start_story():
    """
    User just pressed `get started` button so we can greet him
    """

    @story.part()
    async def greetings(message):
        logger.info('greetings')
        await chat.say('<Motivate user to act>', message['user'])


@story.on(receive=text.Any())
def text_story():
    """
    React on any text message
    """

    logger.debug('parse echo story')

    @story.part()
    async def echo(message):
        logger.info('echo')
        await chat.say('<React on text message>', message['user'])


@story.on(receive=any.Any())
def any_story():
    """
    And all the rest messages as well
    """

    @story.part()
    async def something_else(message):
        logger.info('something_else')
        await chat.say('<React on unknown message>', message['user'])
