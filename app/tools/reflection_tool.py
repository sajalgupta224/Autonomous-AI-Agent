from app.prompts import REFLECTION_PROMPT
from app.gemini_client import ask_gemini
from app.logger import logger
from app.tools.memory_tool import save_memory


def improve_document(document: str):

    logger.info("Reflection started")

    review_prompt = f"""
{REFLECTION_PROMPT}

Review the following business document.

If there are missing sections,
grammar mistakes,
weak explanations,
poor formatting,
or better recommendations,

rewrite the COMPLETE document professionally.

Business Document:

{document}

Return ONLY the improved final document.
"""

    improved_document = ask_gemini(review_prompt)

    save_memory("Reflection", improved_document)

    logger.info("Reflection completed")

    return improved_document