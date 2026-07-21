import os
import importlib

skills = []


def load_skills():

    global skills

    skills.clear()

    folder = "skills"

    for file in os.listdir(folder):

        if file.endswith(".py") and file != "__init__.py":

            module_name = f"skills.{file[:-3]}"

            try:

                module = importlib.import_module(module_name)

                if hasattr(module, "handle"):

                    skills.append({
                                    "name": module.SKILL_NAME,
                                    "keywords": module.KEYWORDS,
                                    "handler": module.handle
                                })

                    print(f"Loaded skill: {module.SKILL_NAME}")

            except Exception as e:

                print(f"Couldn't load {file}: {e}")


def execute_skills(command):

    command = command.lower()

    for skill in skills:

        if any(keyword in command for keyword in skill["keywords"]):

            try:
                response = skill["handler"](command)

                if response:
                    return response

            except Exception as e:
                print(f"{skill['name']} error: {e}")

    return None