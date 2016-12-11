import os
import pytest

from . import main, test_utils


@pytest.mark.asyncio
async def test_start_bot(event_loop):
    async with test_utils.SandboxBot(event_loop, main.Bot()) as sandbox:
        assert len(sandbox.fb.history) == 0


@pytest.mark.asyncio
async def test_text_echo(event_loop):
    async with test_utils.SandboxBot(event_loop, main.Bot()) as sandbox:
        await test_utils.post('http://0.0.0.0:{}/webhook'.format(os.environ.get('API_PORT', 8080)),
                              json={
                                  "object": "page",
                                  "entry": [{
                                      "id": "PAGE_ID",
                                      "time": 1458692752478,
                                      "messaging": [{
                                          "sender": {
                                              "id": "USER_ID"
                                          },
                                          "recipient": {
                                              "id": "PAGE_ID"
                                          },
                                          "timestamp": 1458692752478,
                                          "message": {
                                              "mid": "mid.1457764197618:41d102a3e1ae206a38",
                                              "seq": 73,
                                              "text": "hello, world!",
                                          }
                                      }]
                                  }]
                              })

        assert len(sandbox.fb.history) == 1
        assert await sandbox.fb.history[0]['request'].json() == {
            'message': {
                'text': '<React on text message>'
            },
            'recipient': {'id': 'USER_ID'},
        }
