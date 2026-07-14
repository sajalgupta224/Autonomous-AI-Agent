from app.tools.writer_tool import write_document
from app.tools.reflection_tool import improve_document
from app.models import TaskStatus
from app.tools.doc_tool import generate_doc
from app.tools.memory_tool import memory_count
import time

"""
Autonomous Agent

This file is the brain of the application.

Responsibilities:
- Receive request
- Decide which tool to invoke
- Coordinate execution
- Return final result

No business logic should exist here.
"""

from app.logger import logger

from app.tools.planner_tool import create_plan


class AutonomousAgent:

    def __init__(self):

        logger.info("Autonomous Agent Initialized")
    
    def process_request(self, user_request):
        start = time.time()
        logger.info("Processing User Request")

        logger.info("Planning Started")
        plan = create_plan(user_request)
        logger.info("Planning Completed")
#-------------------------------------------------
        execution_tasks = []
        for i, task in enumerate(plan):
            execution_tasks.append(
            TaskStatus(
                id=i + 1,
                name=task,
                status="Pending"
                )
            )

#--------------------------------------------------
        logger.info("Writing Started")
        document = write_document(plan)
        logger.info("Writing Completed")

#--------------------------------------------------       
        for task in execution_tasks:
            task.status = "Completed"
#--------------------------------------------------
        
#--------------------------------------------------        
        logger.info("Reflection Started")
        improved_document = improve_document(document)
        logger.info("Reflection Completed")

#---------------------------------------------------
        logger.info("Document Generation Started")
        doc_path=generate_doc(
            improved_document,
            user_request = user_request,
            tasks=execution_tasks
        )
        logger.info("Document Generation Completed")

        execution_time = round(time.time() - start, 2)
        logger.info(f"Execution Time : {execution_time} sec")

        return {
            "status": "Success",
            "request": user_request,
            "tasks": execution_tasks,
            "document_path": doc_path,
            "memory_entries": memory_count(),
            "execution_time": f"{execution_time} sec"
        }