# Autonomous AI Agent

An autonomous AI agent built using Python and FastAPI that understands a natural language request, creates its own execution plan, executes the plan using specialized tools, performs self-review, and generates a professional Microsoft Word document.

---

## Features

- Autonomous task planning
- AI-powered business document generation
- Reflection / self-review
- Microsoft Word (.docx) generation
- Execution logging
- Retry & fallback logic
- Memory tracking
- REST API using FastAPI

---

## Architecture

User
↓

FastAPI
↓

Autonomous Agent
↓

Planner Tool

↓

Writer Tool

↓

Reflection Tool

↓

Document Generator

↓

DOCX Output

---

## Project Structure

app/

main.py

agent.py

models.py

logger.py

gemini_client.py

tools/

planner_tool.py

writer_tool.py

reflection_tool.py

memory_tool.py

doc_tool.py

generated_docs/

logs/

---

## Engineering Improvement

Implemented Retry & Fallback Logic.

The Gemini client automatically retries failed requests caused by temporary API failures, rate limits, or service interruptions before returning a controlled error.

---

## Technologies

Python

FastAPI

Gemini API

python-docx

Pydantic

Logging

REST API

---

## Run

```bash
uvicorn app.main:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## Sample Request

```json
{
  "request":"Create a proposal for an AI chatbot for a hospital."
}
```

---

## Output

Execution Plan

Professional Business Proposal

Microsoft Word Document

Execution Logs

Memory Summary

---

## Future Improvements

Multi-agent execution

RAG Integration

Database persistence

Conversation memory

Additional output formats (PDF)
