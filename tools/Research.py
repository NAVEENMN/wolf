import os
from PyInquirer import prompt
from components.Questions import Questions
from components.Design import Design


class Research:
    def __init__(self, path):
        print("*** INFO: Research tool")
        self.root = path
        self.dir_path = None
        self.title = None
        self.fp = None

    def set_file_ptr(self, fp):
        self.fp = fp

    def _set_dir_path(self, dir_path):
        self.dir_path = f"/Users/naveenmysore/Dropbox/obsidian/research/{dir_path}"

    def get_dir_path(self):
        return self.dir_path

    def _set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def _create_directory(self):

        if os.path.exists(self.dir_path):
            print("*** Directory already exists, delete it manually to proceed")
            return False
        else:
            print(f"*** Creating {self.dir_path}")
            os.mkdir(self.dir_path)

        return True

    def add_heading(self):
        self.fp.write(f"# {self.title}\n")
        self.fp.write("---\n")
        self.fp.write("[[design]] [[questions]] [[references]] [[evidences]]\n")

    def add_people(self):
        self.fp.write(f"## Key people\n")
        self.fp.write("Who are some key people in this domain and their contribution.\n")

    def add_a_line(self, line):
        self.fp.write(f"{line}\n")

    def add_a_sentence(self, line):
        self.fp.write(f"{line}")

    def add_inductive_section(self):
        print("Adding inductive")
        self.fp.write("## Typical workflow\n")
        self.fp.write("<b>Inductive</b> : Observation -> Observe a pattern -> develop a theory\n")
        self.fp.write("Examples Observation\n")
        self.fp.write("A low-cost airline flight is delayed, Dogs A and B have fleas, Elephants depend on water to exist\n")
        self.fp.write("Examples Observe a pattern\n")
        self.fp.write(
            "Another 20 flights from low-cost airlines are delayed, All observed dogs have fleas, All observed animals depend on water.\n")
        self.fp.write("Examples develop a theory - $\\forall$\n")
        self.fp.write(
            "Low cost airlines always have delays, All dogs have fleas, All biological life depends on water to exist, \n")

    def add_deductive_section(self):
        print("Adding deductive")
        self.fp.write("## Typical workflow\n")
        self.fp.write(
            "<b>Deductive</b> : Pick an existing theory -> Formulate an Hypothesis -> Collect data to test hypothesis -> Analyze support or reject hypothesis\n")
        self.fp.write("Examples Pick an existing theory\n")
        self.fp.write(
            "Low cost airlines always have delays, All dogs have fleas, All biological life depends on water to exist, \n")
        self.fp.write("Examples Formulate an Hypothesis\n")
        self.fp.write(
            "If passengers pick low cost airline then they will always experience delays, All dogs in my apartment have fleas, All land mammals depends on water to exist\n")
        self.fp.write("Examples Collect data to test hypothesis - - $\\exists$\n \n")
        self.fp.write(
            "Collect data for low cost airlines, Test all dogs in apartment, study all land mammals if they need water\n")
        self.fp.write("Examples Analyze support or reject hypothesis\n")
        self.fp.write("$\\exists$ one example so reject, p value is 0.8 so reject\n")
        self.fp.write(
            "Based on descriptive statistics the mean value is x so reject, based on inferential statistics, t test we reject\n")

    def add_design_section(self):
        self.fp.write("## Typical workflow\n")
        self.fp.write(
            "<b>Design</b> : Pick an existing model or design -> What are you optimizing -> Collect data to test your change or new design -> Analyze support or reject design or model\n")
        self.fp.write("Examples Pick an existing model/design/architecture\n")

    def add_other_section(self):
        pass

    def add_hypothesis(self):
        self.fp.write("## Hypothesis\n")
        self.fp.write("Your research hypothesis goes here.\n")

    def add_problem_statement(self):
        self.fp.write("## Problem Statement\n")
        self.fp.write("Your problem statement goes here.\n")

    def add_project_end(self):
        self.fp.write("## Project end state\n")
        self.fp.write("All projects needs an end state and upon arrival to conclude project as complete.\n")

    def check_for_type_of_research(self):
        questions = [
            {
                'type': 'list',
                'name': 'r_aim',
                'message': 'What is the aim of research?',
                'choices': ['Applied', 'Fundamental'],
                'filter': lambda val: val.lower()
            },
            {
                'type': 'list',
                'name': 'r_type',
                'message': 'Inductive reasoning aims at developing a theory. Deductive reasoning aims at testing a theory.\n'
                           'What type of research are you conducting?',
                'choices': ['Inductive', 'Deductive', 'Engineering', 'Other'],
                'filter': lambda val: val.lower()
            },
            {
                'type': 'list',
                'name': 'r_solved',
                'message': '[Design] Is the problem you are targeting solved or unsolved.\n',
                'choices': ['solved', 'unsolved', 'partially_solved', 'i_dont_know', 'n/a'],
                'filter': lambda val: val.lower()
            },
            {
                'type': 'list',
                'name': 'r_method',
                'message': 'Are you planning to run experiments or observe data.\n',
                'choices': ['Observational', 'Experimental'],
                'filter': lambda val: val.lower()
            }
        ]
        answers_1 = prompt(questions)

        response = {}
        response['aim'] = answers_1['r_aim']
        response['type'] = answers_1['r_type']
        response['solved'] = answers_1['r_solved']
        response['method'] = answers_1['r_method']
        response['area'] = None

        if answers_1['r_aim'] == 'applied':
            questions = [
                {
                    'type': 'input',
                    'name': 'application_area',
                    'message': 'Enter comma seperated application areas',
                }
            ]
            answers_2 = prompt(questions)
            response['application_area'] = answers_2['application_area']

        return response

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
        answers = prompt(questions)
        self._set_dir_path(answers['directory_name'])
        self._set_title(answers['title'])
        status = self._create_directory()
        return status

    def setup(self):
        status = self._setup_directories()
        if not status:
            return
        save_path_file = f"{self.get_dir_path()}/research.md"
        with open(save_path_file, "w") as f:
            self.set_file_ptr(f)
            self.add_heading()
            research = self.check_for_type_of_research()

            if research['aim'] == 'applied':
                self.add_a_sentence(
                    line=f"This is an applied {research['type']} research targeting {research['area']} areas")

            else:
                self.add_a_sentence(line=f"This is a fundamental {research['type']} research")

            self.add_a_sentence(line=f"This is an {research['method']} research")
            self.add_a_sentence(
                line="This objective of this document is to clearly organize information. Also, help myself in constructing an execution plan.")
            self.add_a_sentence(line="The output of this projects or research will be a paper, code or video.")

            self.add_project_end()

            if research['type'] == "inductive":
                self.add_inductive_section()
                self.add_a_sentence(line=f"This is an inductive research proposing a new theory.\n")

            elif research['type'] == "deductive":
                self.add_deductive_section()
                self.add_a_sentence(line=f"This is a deductive research testing an existing hypothesis.\n")
                self.add_hypothesis()

            elif research['type'] == "engineering":
                self.add_design_section()
                self.add_problem_statement()
                if research['solved'] == 'solved':
                    self.add_a_line(
                        line=f"This is a design research improving performance or optimizing existing model, design or architecture. "
                             f"This is a design research proposing a new design to solve an existing problem\n")
                elif research['solved'] == 'unsolved':
                    self.add_a_line(
                        line=f"This is a design research proposing a new design to a solved problem because its better")
                elif research['solved'] == 'partially_solved':
                    self.add_a_line(line=f"This is a design research targeting a partially solved problem.")

                self.add_a_line(line="## Current state\n")
                self.add_a_line(
                    line="What are the costs associated with current state of the art. In terms of time, energy, efficiency or price.")

                # Creating components structures
                if not os.path.exists(f"{self.get_dir_path()}/methods"):
                    os.mkdir(f"{self.get_dir_path()}/methods")

                save_path_file = f"{self.get_dir_path()}/methods/methods.md"
                with open(save_path_file, "w") as f:
                    f.write(f"# Exisiting methods\n")
                    f.write(f"[[method1]] [[method2]]\n")

                save_path_file = f"{self.get_dir_path()}/methods/method_1.md"
                with open(save_path_file, "w") as f:
                    f.write(f"# Method 1\n")

                save_path_file = f"{self.get_dir_path()}/methods/method_2.md"
                with open(save_path_file, "w") as f:
                    f.write(f"# Method 2 1\n")

                # Create methods structures
                # TODO: Based on a json file create hirerachial structure.
                if not os.path.exists(f"{self.get_dir_path()}/components"):
                    os.mkdir(f"{self.get_dir_path()}/components")

                save_path_file = f"{self.get_dir_path()}/components/component_1.md"
                with open(save_path_file, "w") as f:
                    f.write(f"# component 1\n")

                save_path_file = f"{self.get_dir_path()}/components/component_2.md"
                with open(save_path_file, "w") as f:
                    f.write(f"# component 2\n")

            else:
                self.add_other_section()

            self.add_people()

        save_path_file = f"{self.get_dir_path()}/design.md"
        with open(save_path_file, "w") as f:
            _design = Design(fp=f, method=research['method'])
            _design.add_heading(heading=self.get_title())
            _design.add_plan()
            _design.add_measurements_section()
            # TODO: Add contents from here https://www.scribbr.com/methodology/research-design/

        save_path_file = f"{self.get_dir_path()}/questions.md"
        with open(save_path_file, "w") as f:
            _questions = Questions(fp=f)
            _questions.add_heading(heading=self.get_title())
            _questions.add_a_line(line="Base rate questions are normal patterns of occurance, "
                                       "without base rate we cannot know whether something is normal or unusual.")
            _questions.collect_variables()
            _questions.ask_all_questions()


        # Create evidence structures
        if not os.path.exists(f"{self.get_dir_path()}/literature"):
            os.mkdir(f"{self.get_dir_path()}/literature")

        save_path_file = f"{self.get_dir_path()}/literature/evidences.md"
        with open(save_path_file, "w") as f:
            f.write(f"# {self.get_title()}\n")
            f.write(f"[[evidences_in_favour]] [[evidences_not_in_favour]] [[references]]")

        save_path_file = f"{self.get_dir_path()}/literature/evidences_in_favour.md"
        with open(save_path_file, "w") as f:
            f.write(f"# Evidences in favour\n")
            f.write("---\n")
            f.write(f"[[evidences_not_in_favour]]")

        save_path_file = f"{self.get_dir_path()}/literature/evidences_not_in_favour.md"
        with open(save_path_file, "w") as f:
            f.write(f"# Evidences not in favour\n")
            f.write("---\n")
            f.write(f"[[evidences_in_favour]]")

        save_path_file = f"{self.get_dir_path()}/literature/references.md"
        with open(save_path_file, "w") as f:
            f.write(f"# References\n")
            f.write("---\n")

