import os
import time
import google.generativeai as genai
from dotenv import load_dotenv
from app.logger import logger
from google.api_core.exceptions import (
    ResourceExhausted,
    DeadlineExceeded,
    ServiceUnavailable,
)


load_dotenv("app/.env")

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(os.getenv("MODEL_NAME"))


def ask_gemini(prompt: str) -> str:

    retries = 3

    last_exception = None

    for attempt in range(1, retries + 1):

        try:

            logger.info(f"Gemini Request | Attempt {attempt}")

            response = model.generate_content(prompt)

            if (
                response
                and hasattr(response, "text")
                and response.text
            ):

                logger.info("Gemini Response Received")

                return response.text

            raise Exception("Gemini returned an empty response.")

        except (
            ResourceExhausted,
            DeadlineExceeded,
            ServiceUnavailable,
        ) as e:

            last_exception = e

            wait_time = 5 * attempt

            logger.warning(
                f"Gemini temporary failure ({attempt}/{retries}). "
                f"Retrying in {wait_time} seconds..."
            )

            time.sleep(wait_time)

        except Exception as e:

            logger.error(f"Gemini Error : {str(e)}")

            raise

    logger.error("Gemini failed after all retries.")

    raise Exception(
        f"Gemini unavailable after {retries} retries."
    ) from last_exception