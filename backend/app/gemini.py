import os
import json
import logging
import time
from openai import OpenAI

logger = logging.getLogger(__name__)


class GeminiClient:

    def __init__(self):
        self.model = os.getenv("GEMINI_MODEL", "openrouter/free")

        self.client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )

    def generate_json(self, system_prompt, prompt):

        last_error = None

        for attempt in range(3):

            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "system",
                            "content": system_prompt
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0,
                    max_tokens=3500
                )

                # Handle OpenRouter returning no choices
                if not response.choices:
                    raise RuntimeError(
                        f"OpenRouter returned no choices: {response}"
                    )

                result_text = response.choices[0].message.content

                if not result_text:
                    raise RuntimeError(
                        "Model returned empty content"
                    )

                logger.info(
                    "Model response length: %d",
                    len(result_text)
                )

                return self.parse_json(result_text)

            except Exception as e:

                last_error = e

                logger.error(
                    "OpenRouter attempt %d failed: %s",
                    attempt + 1,
                    e
                )

                # Retry after a short delay
                if attempt < 2:
                    time.sleep(2 ** attempt)

        raise RuntimeError(
            f"OpenRouter request failed after 3 attempts: {last_error}"
        )

    def parse_json(self, text):

        try:
            result = json.loads(text)

            if isinstance(result, dict):
                return result

        except json.JSONDecodeError:
            pass

        # Try extracting JSON from markdown/code fences
        start = text.find("{")
        end = text.rfind("}")

        if start != -1 and end != -1 and end > start:
            try:
                result = json.loads(text[start:end + 1])

                if isinstance(result, dict):
                    return result

            except json.JSONDecodeError:
                pass

        raise ValueError(
            "Model returned invalid JSON"
        )


# IMPORTANT:
# Other files in your project import this variable.
client = GeminiClient()