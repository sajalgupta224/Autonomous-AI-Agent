from app.gemini_client import ask_gemini
from app.logger import logger
from app.tools.memory_tool import save_memory


def write_document(plan):

    logger.info("Writer Tool Started")

    prompt = f"""
You are an experienced Business Consultant.

Using the execution plan below, generate a professional business document.

Execution Plan:
{plan}

Return the document in MARKDOWN format.

Rules:

# Title

## Executive Summary

## Business Objectives

## Current Challenges

## Proposed Solution

## Key Features

## Business Benefits

## Implementation Roadmap

## Estimated Timeline

## Cost Estimate

## Risks and Mitigation

## Recommendations

## Conclusion

Formatting Rules:

- Use Markdown headings (# and ##)
- Use bullet points where appropriate
- Write professionally
- Keep the language suitable for business stakeholders
- Do NOT wrap the response inside markdown code blocks.
Return ONLY the document.
"""

    document = ask_gemini(prompt)

    save_memory("Writer", document)

    logger.info("Writer Tool Completed")

    return document