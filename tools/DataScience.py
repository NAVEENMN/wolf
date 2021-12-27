import os
from PyInquirer import prompt


class DataScience:
    def __init__(self, path):
        print("*** INFO: Data Science Research")
        self.path = path
        self.dir_path = os.path.join(path, 'research')

    def _setup_directories(self):
        questions = [
            {
                'type': 'input',
                'name': 'directory_name',
                'message': 'Name your research directory',
            },
            {
                'type': 'input',
                'name': 'title',
                'message': 'What is the research title',
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
            os.mkdir(os.path.join(self.dir_path, answers['directory_name'], 'code'))
            os.mkdir(os.path.join(self.dir_path, answers['directory_name'], 'code', 'data'))
            os.mkdir(os.path.join(self.dir_path, answers['directory_name'], 'code', 'source'))
            print("*** INFO: Use this path for coding project.")
            print(f"path: {os.path.join(self.dir_path, answers['directory_name'], 'code')}")

        return status, answers

    def setup(self):
        status, answers = self._setup_directories()
        if not status:
            return

        save_path_file = os.path.join(self.dir_path, answers["directory_name"], "dsresearch.md")
        with open(save_path_file, "w") as f:
            f.write(f"# {answers['title']}\n")
            f.write("---\n")
            f.write(f"Data Science research involves methodical steps and process to uncover answers from the data.\n")

            f.write(f"## Description/Goal/Objective\n")
            f.write(f"What are you trying to uncover using data?")

            f.write(f"## Data Description\n")
            f.write(f"Describe your data.")
            f.write(f"#### Data Properties\n")
            f.write(f"What are you trying to uncover using data?")
            f.write(f"What are the rows and columns and types? What does each variable mean and what are their units?\n")
            f.write(f"#### Data Acquisition\n")
            f.write(f"How was this data acquired? Who acquired it and what sensors and where was it acquired? Was this a statistical sample?")

        save_path_file = os.path.join(self.dir_path, answers["directory_name"], "steps.md")
        with open(save_path_file, "w") as f:
            f.write(f"# Steps\n")
            f.write("---\n")
            f.write(f"1: Obtain\n")
            f.write(f"Source of data\n")
            f.write(f"2: Refine\n")
            f.write(f"Scrub and refine the data\n")
            f.write(f"3: Explore\n")
            f.write(f"Exploratory data analysis\n")
            f.write(f"4: Model\n")
            f.write(f"Given this data what system would have produced such data. Model such a system. Predict or forecast or test a hypothesis\n")
            f.write(f"5: Interpret\n")
            f.write(f"Put results into use by stories or description.\n")

        save_path_file = os.path.join(self.dir_path, answers["directory_name"], "references.md")
        with open(save_path_file, "w") as f:
            f.write(f"# References\n")
            f.write("---\n")
            f.write(f"Handy references for your research\n")



