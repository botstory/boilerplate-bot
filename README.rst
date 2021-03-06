Boilerplate-bot
---------------

.. image:: https://travis-ci.org/botstory/boilerplate-bot.svg?branch=develop
    :target: https://travis-ci.org/botstory/boilerplate-bot

.. image:: https://coveralls.io/repos/github/botstory/boilerplate-bot/badge.svg?branch=develop
    :target: https://coveralls.io/github/botstory/boilerplate-bot?branch=develop


Good place to start your bot based on `BotStory framework <https://github.com/botstory/bot-story>`_.

Stack
~~~~~

`:rocket:` auto deploying `landing page <https://botstory.github.io/boilerplate-bot/>`_ (`sources <https://github.com/botstory/boilerplate-bot-landing>`_)

`:snake:` Python 3.6 and `AsyncIO <https://docs.python.org/3/library/asyncio.html>`_ and `AioHTTP <http://aiohttp.readthedocs.io/en/stable/>`_

`:package:` `Mongodb <https://www.mongodb.com/>`_ - storage for user and session

`:ship:` `Docker Container <https://www.docker.com/>`_ for Mongo and Python

`:tractor:` `Travis-CI <https://travis-ci.org/>`_ - test and coverage

Instruction
~~~~~~~~~~~

Test performance of webhook

.. code-block:: bash

    WEBHOOK_URL=<url-to-webhook-of-your-bot> ./scripts/performance.sh


Bot Checklist
~~~~~~~~~~~~~
Common checklist for common bot

- [ ] Mindmap. Could use `Coggle <https://coggle.it/>`_. `Example <https://coggle.it/diagram/WcgsjGjgVAABxW_M>`_
- [ ] Describe bot profile at *<chatbot-name>/__init__.py*.
