import os
from PyInquirer import prompt

class Innovent:
    def __init__(self, path):
        print("*** INFO: Innovent")
        self.path = path
        self.dir_path = os.path.join(path, 'innovents')

    def _setup_directories(self):
        questions = [
            {
                'type': 'input',
                'name': 'directory_name',
                'message': 'Name your innovent directory',
            },
            {
                'type': 'input',
                'name': 'title',
                'message': 'What is the innovent title',
            }
        ]
        status = True
        answers = prompt(questions)
        if os.path.exists(os.path.join(self.dir_path, answers['directory_name'])):
            print("*** Warning directory already exists delete it manually")
            status = True
        else:
            os.mkdir(os.path.join(self.dir_path, answers['directory_name']))
            os.mkdir(os.path.join(self.dir_path, answers['directory_name'], 'media'))

        return status, answers

    def setup(self):
        status, answers = self._setup_directories()
        if not status:
            return

        save_path_file = os.path.join(self.dir_path, answers["directory_name"], "innovent.md")
        with open(save_path_file, "w") as f:
            f.write(f"# {answers['title']}\n")
            f.write("---\n")
            f.write(f"Innovations are done when there is an incremental improvement eg Bulb to LED. "
                    f"Inventions are done when a new way is created eg. Candle to Bulb. This document is created to capture both.\n")

            f.write(f"## Area of focus\n")
            f.write(f"Your area of focus goes here. "
                    f"This can be device, system, appliance, software, anything\n")

            f.write(f"## Purpose\n")
            f.write(f"Everything we humans build has a purpose. What is the purpose of item in area of focus? "
                    f"ex: purpose of bulb is to give light, purpose of telescope is to see distant objects.\n")

            f.write(f"## Measurements\n")
            f.write(f"If the item in area of focus is serving it's purpose how it is measured?\n")

            f.write(f"## Innovate\n")
            f.write(f"To innovate bring a small change to improve performance, or efficiency etc\n")

            f.write(f"## Invent\n")
            f.write(f"To Invent keep the purpose fixed and find a new way to achieve same purpose.")

