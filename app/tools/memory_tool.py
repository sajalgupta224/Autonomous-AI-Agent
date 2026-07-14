from datetime import datetime

memory_store = []


def save_memory(tool, content):

    memory_store.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tool": tool,
        "content": content
    })


def get_memory():
    return memory_store


def memory_count():
    return len(memory_store)