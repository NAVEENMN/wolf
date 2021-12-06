class Design:
    def __init__(self, fp, method):
        self.name = "Design"
        self.fp = fp
        self.method = method

    def add_quantitative_design(self):
        # correlational
        # descriptive
        pass

    def add_qualitative_design(self):
        pass

    def add_experiment_design_section(self):
        self.fp.write(f"## Experiment Design\n")
        self.fp.write("Your experiment design goes here. Typically diagrams would be better. Experiment typically produce data")

    def add_observational_design_section(self):
        self.fp.write(f"## Observational Design\n")
        self.fp.write("Your observational design goes here. Typically data sources and data descriptions go here")

    def add_engineering_design_section(self):
        self.fp.write(f"## Engineering Design\n")
        self.fp.write("Your engineering design goes here. Typically system diagram go here")

    def add_measurements_section(self):
        self.fp.write(f"## Engineering Measurements\n")
        self.fp.write("Your descriptions for measurements goes here.\n")
        self.fp.write("List all the variables you are measuring, their units and descriptions.\n")


    def add_plan(self):
        if self.method == 'experimental':
            self.add_experiment_design_section()
        elif self.method == 'observational':
            self.add_observational_design_section()
        else:
            self.add_engineering_design_section()

    def add_heading(self, heading):
        self.fp.write(f"# {heading}\n")
        self.fp.write(f"#### {self.method} research design\n")
        self.fp.write("---\n")