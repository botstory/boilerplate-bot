import aiohttp
import asyncio
import botstory
import contextlib
import emoji
from io import StringIO
import os
import pytest
from unittest.mock import Mock

from boilerplate import bot, main, test_utils


@pytest.mark.asyncio
async def test_start_bot(event_loop):
    async with test_utils.SandboxBot(event_loop, bot.Bot()) as sandbox:
        assert len(sandbox.fb.history) > 0


@pytest.mark.asyncio
async def test_earth_message(event_loop):
    async with test_utils.SandboxBot(event_loop, bot.Bot()) as sandbox:
        initial_history_length = len(sandbox.fb.history)
        await test_utils.post('http://0.0.0.0:{}/webhook'.format(os.environ.get('API_PORT', 8080)),
                              json={
                                  'object': 'page',
                                  'entry': [{
                                      'id': 'PAGE_ID',
                                      'time': 1458692752478,
                                      'messaging': [{
                                          'sender': {
                                              'id': 'USER_ID'
                                          },
                                          'recipient': {
                                              'id': 'PAGE_ID'
                                          },
                                          'timestamp': 1458692752478,
                                          'message': {
                                              'mid': 'mid.1457764197618:41d102a3e1ae206a38',
                                              'seq': 73,
                                              'text': 'hello, world!',
                                          }
                                      }]
                                  }]
                              })

        # use it because we spawn fb handler process and return 200Ok
        await asyncio.sleep(0.1)

        # we can't use initial_history_length + 1
        # because it is very likely that we don't have user USER_ID in our user's collection
        # and fb handler will ask user's profile meanwhile process income message
        assert len(sandbox.fb.history) > initial_history_length
        assert await sandbox.fb.history[-1]['request'].json() == {
            'message': {
                'text': emoji.emojize(':earth:', use_aliases=False),
            },
            'recipient': {'id': 'USER_ID'},
        }


def test_parser_empty_arguments():
    parsed, _ = main.parse_args([])
    assert parsed.setup is not True
    assert parsed.start is not True


def test_parser_setup_arguments():
    parsed, _ = main.parse_args(['--setup'])
    assert parsed.setup is True
    assert parsed.start is not True


def test_parser_start_arguments():
    parsed, _ = main.parse_args(['--start'])
    assert parsed.setup is False
    assert parsed.start is True


def test_show_help_if_no_any_arguments():
    main.sys.argv = []
    temp_stdout = StringIO()
    with contextlib.redirect_stdout(temp_stdout):
        main.main()
    output = temp_stdout.getvalue().strip()
    assert 'help' in output
    assert 'setup' in output
    assert 'start' in output


def test_setup_bot_on_setup_argument(mocker):
    main.sys.argv = ['', '--setup']
    handler = mocker.patch('boilerplate.main.setup')
    main.main()
    assert handler.called is True


def test_start_bot_on_setup_argument(mocker):
    main.sys.argv = ['', '--start']
    handler = mocker.patch('boilerplate.main.start')
    main.main()
    assert handler.called is True
