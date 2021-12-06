import os
from PyInquirer import prompt


class Investigations:
    def __init__(self, path):
        print("*** INFO: Investigations")
        self.path = path
        self.dir_path = os.path.join(path, 'investigations')

    def _setup_directories(self):
        questions = [
            {
                'type': 'input',
                'name': 'directory_name',
                'message': 'Name your investigation directory',
            },
            {
                'type': 'input',
                'name': 'title',
                'message': 'What is the investigation title',
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

        save_path_file = os.path.join(self.dir_path, answers["directory_name"], "investigation.md")
        with open(save_path_file, "w") as f:
            f.write(f"# {answers['title']}\n")
            f.write("---\n")
            f.write(f"Investigations are launched when an incident has occurred/occurring.\n")

            f.write(f"## Description\n")
            f.write(f"Your incident description goes here. "
                    f"How long has this been occurring or when did this happen?\n"
                    f"How costly is this incident?\n")

            f.write(f"## Stakeholders\n")
            f.write(f"Who are the teams/people interested in this investigations and why?.\n")

            f.write(f"## Simulation/Reproductions\n")
            f.write(f"Simulating events which happened during the incidents will give us clue.\n")

            f.write(f"## Expected Behavior vs Actual Behavior\n")
            f.write(f"Under the original designed conditional what was expected by what happened/happening?\n")

            f.write(f"## Chain of Events\n")
            f.write(f"Linking cause and effects will give us clues.\n")

            f.write(f"## Suggestion/Fix/Mitigation\n")
            f.write(f"Your suggestion, fix or resolution for this issue or incident.\n")

            f.write(f"## Conclusion\n")
            f.write(f"A detailed conclusion on this investigation.\n")

        save_path_file = os.path.join(self.dir_path, answers["directory_name"], "clues.md")
        with open(save_path_file, "w") as f:
            f.write(f"# Clues\n")
            f.write("---\n")
            f.write(f"Clue 1: \n")

        save_path_file = os.path.join(self.dir_path, answers["directory_name"], "references.md")
        with open(save_path_file, "w") as f:
            f.write(f"# References\n")
            f.write("---\n")
            f.write(f"Handy references for investigations\n")


