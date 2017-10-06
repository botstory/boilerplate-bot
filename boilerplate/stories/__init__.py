from boilerplate.stories.greetings import greeting_stories
from boilerplate.stories.help import help_stories
from boilerplate.stories.query import query_stories

story_modules = (
    greeting_stories,
    query_stories,

    # last hope :)
    # if we haven't handle message before,
    # then show help message to user
    help_stories,
)


def setup(story):
    for m in story_modules:
        m.setup(story)
