from urllib import response

from click import command

from local_brain import local_brain
from system_control import execute_system_command
from memory import (
    recall_memory,
    update_memory
)
from avatar import update_status
from skill_loader import execute_skills


def route(command):

    # ---------- Local ----------
    response = local_brain(command)

    if response:
        return response
    
    #--------- Skills ----------
    response = execute_skills(command)

    if response:
        return response
    
    # ---------- System ----------
    response = execute_system_command(command)

    if response:
        update_status("system.PNG")
        return response


    # ---------- Memory Recall ----------
    response = recall_memory(command)

    if response:
        update_status("recalling_memory.PNG")
        return response


    # ---------- Memory Update ----------
    if update_memory(command):
        update_status("updating_memory.PNG")
        return "I'll remember that."


    return None