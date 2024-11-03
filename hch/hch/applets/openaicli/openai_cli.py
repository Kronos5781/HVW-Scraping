import openai

from .openai_cli_base import OpenAICliBase


class OpenAICli(OpenAICliBase):

    def __init__(self):
        super().__init__()

    def send_message(self, content: str) -> str:

        # setup message
        messages = [
            {
                "role": "system",
                "content": content
            },
        ]

        # send to openai
        response = self._client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        return response.choices[0].message.content
