from app.prompts import PLANNER_PROMPT
from app.gemini_client import ask_gemini
from app.tools.memory_tool import save_memory
from app.logger import logger

def create_plan(user_request: str):

    logger.info("Planner started")

    prompt = f"""
{PLANNER_PROMPT}

User Request:

{user_request}
"""
    
#cleaning of prompt

    response = ask_gemini(prompt)

    tasks = []                        #storage (empty list)

    for line in response.split("\n"):

        line = line.strip()           #cleaning of line one by one

        if line:

            tasks.append(line) 
    save_memory("Planner", str(tasks))
    logger.info("Planner completed successfully")
    return tasks