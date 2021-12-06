from PyInquirer import prompt
from itertools import permutations

questions_json = {
  "Existence_Questions": ["Does _X exist?"],
  "Description_Questions": ["What is _X like?",
                            "What are _X properties?",
                            "How can we measure _X?",
                            "What is the purpose of _X?",
                            "What are the components of _X",
                            "How do components of _X related to each other?",
                            "What are all types of _X?"],
  "Classification_Questions": ["What can _X be categorized as?"],
  "Frequency_Questions": ["How often does _X occur?", "What is the average amount of _X?"],
  "Comparative_Questions": ["How does _X differ from _Y?"],
  "Process_Questions": ["How does _X normally work?",
                        "What is the process by which _X happens?",
                        "In what order does events in _X occur?",
                        "What are the steps _X goes through as it evolves",
                        "How does _X achieve its purpose?"],
  "Causality_Questions": ["Does _X cause _Y ?", "Does _X prevent _Y?",
                          "What are all the factors that cause _X and/or _Y?"],
  "Causality_Degree_Questions": ["Is _X better at _Y preventing than _Z"],
  "Relationship_Questions": ["Are _X and _Y related?", "How _X and _Y related?"],
  "Design_Questions": ["Whats an effective way to achieve _X?",
                       "How can we increase _X?",
                       "How can we decrease _X?",
                       "How can be optimize _X?",
                       "What strategies helps to achieve _X"]
}


class Questions:
    def __init__(self, fp):
        self.fp = fp
        self.variables = []
        self.variable_pairs = []
        self.variable_triplets = []

    def add_heading(self, heading):
        self.fp.write(f"# {heading}\n")
        self.fp.write(f"#### Question pools\n")
        self.fp.write("---\n")
        self.fp.write("Here are some generic questions to ask, remove questions which make no sense\n")

    def add_a_line(self, line):
        self.fp.write(f"{line}\n")

    def collect_variables(self):
        questions = [
            {
                'type': 'input',
                'name': 'variables',
                'message': 'Enter comma seperated variables',
            }
        ]
        answers = prompt(questions)
        self.variables = answers['variables'].split(", ")
        self.variable_pairs = list(permutations(self.variables, 2))
        if len(self.variables) > 2:
            self.variable_triplets = list(permutations(self.variables, 3))

    def ask_one_variable_questions(self, sections):
        q_types = ['Existence_Questions', 'Description_Questions', 'Classification_Questions', 'Frequency_Questions', 'Process_Questions', 'Design_Questions']
        for q_type in q_types:
            self.fp.write(f"## {q_type}\n")
            for variable in self.variables:
                questions = sections[q_type]
                for i, question in enumerate(questions):
                    self.fp.write(f"{i}. {question.replace('_X', variable)}\n")

    def ask_two_variable_questions(self, sections):
        q_types = ['Causality_Questions', 'Relationship_Questions']
        for q_type in q_types:
            self.fp.write(f"## {q_type}\n")
            for variable in self.variable_pairs:
                questions = sections[q_type]
                for i, question in enumerate(questions):
                    _q = question.replace('_X', variable[0])
                    _q = _q.replace('_Y', variable[1])
                    self.fp.write(f"{i}. {_q}\n")

    def ask_three_variable_questions(self, sections):
        q_types = ['Causality_Degree_Questions']
        for q_type in q_types:
            self.fp.write(f"## {q_type}\n")
            for variable in self.variable_triplets:
                questions = sections[q_type]
                for i, question in enumerate(questions):
                    _q = question.replace('_X', variable[0])
                    _q = _q.replace('_Y', variable[1])
                    _q = _q.replace('_Z', variable[2])
                    self.fp.write(f"{i}. {_q}\n")

    def ask_all_questions(self):
        sections = questions_json
        self.ask_one_variable_questions(sections)
        self.ask_two_variable_questions(sections)
        self.ask_three_variable_questions(sections)