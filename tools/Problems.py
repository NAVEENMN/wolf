import os
from PyInquirer import prompt
from components.Techniques import Techniques


class Problems:
    def __init__(self, path):
        print("*** INFO: Problem tool")
        self.root_path = path
        self.dir_path = os.path.join(path, 'problems')

    def _setup_directories(self):
        questions = [
            {
                'type': 'input',
                'name': 'directory_name',
                'message': 'Name your problem directory',
            },
            {
                'type': 'input',
                'name': 'title',
                'message': 'What is the problem title',
            }
        ]
        status = True
        answers = prompt(questions)
        if os.path.exists(os.path.join(self.dir_path, answers['directory_name'])):
            print("*** Warning directory already exists delete it manually")
            status = True
        else:
            os.mkdir(os.path.join(self.dir_path, answers['directory_name']))

        return status, answers

    def setup(self):
        status, answers = self._setup_directories()
        if not status:
            return

        save_path_file = os.path.join(self.dir_path, answers['directory_name'], 'problem.md')
        with open(save_path_file, "w") as f:
            f.write(f"# {answers['title']}\n")
            f.write("---\n")
            f.write("## Problem Statement\n")
            f.write('What is the problem? : \n')
            f.write('Why is it a problem? : \n')
            f.write('Can you quantify the problem? : \n')

        _techniques = Techniques(path=os.path.join(self.dir_path, answers['directory_name']))
        _techniques.trail_and_error()
        _techniques.root_causing()
