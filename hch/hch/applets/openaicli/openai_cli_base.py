import os
import openai

from hch.utils import Logger


logger = Logger()


class OpenAICliBase:

    def __init__(self):

        self._api_key: str = None
        self._load_api_key()

        self._client = openai.OpenAI(api_key=self._api_key)

    def _load_api_key(self) -> None:

        api_key = os.environ.get("OPENAI_API_KEY")
        if api_key is None:
            raise ValueError("OPENAI_API_KEY not set")

        self._api_key = api_key
        logger.debug("API key loaded")
