from botstory.middlewares import any, option, sticker, text
import emoji
import logging

logger = logging.getLogger(__name__)


def setup(story):
    @story.on(text.EqualCaseIgnore('hello, world!'))
    def earth_message():
        @story.part()
        async def say_something(ctx):
            logger.warning('# Unhandled message')

            # TODO:
            # - store somewhere information about those messages
            # - add quick_replies

            await story.say(
                emoji.emojize(':earth:', use_aliases=True),
                user=ctx['user']
            )
            logger.debug('# end of say_something')
