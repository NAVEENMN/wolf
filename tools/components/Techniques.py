import os

class Techniques:
    def __init__(self, path):
        self.path = path
        self.tpath = os.path.join(self.path, 'techniques')
        if not os.path.exists(self.tpath):
            os.mkdir(self.tpath)

    def trail_and_error(self):
        save_path_file = os.path.join(self.tpath, 'trialanderror.md')
        with open(save_path_file, "w") as f:
            f.write(f"# Trail and Error\n")
            f.write("---\n")
            f.write("This is the most commonly used technique. "
                    "This is an expensive technique if you are dealing with costly problem.\n")
            f.write(f"## Things I have tried so far\n")
            f.write(f"1. I have tried 1\n")
            f.write(f"## Things I am planning to try\n")
            f.write(f"1. Plan 1\n")

    def root_causing(self):
        save_path_file = os.path.join(self.tpath, 'root_causing.md')
        with open(save_path_file, "w") as f:
            f.write(f"# Root Causing\n")
            f.write("---\n")
            f.write("This document will help you to identify different root causes.\n")
            f.write('Since when is this a problem? : \n')
            f.write('Was there any recent change that might have sourced this problem? :\n')

            f.write(f"## 5 whys.\n")

            f.write(f"## Fish bone diagram\n")
            # TODO: Add diagram

            f.write(f'## Scatter or Pair plot diagram for regression/correlation analysis.\n')

            f.write(f"## Failure mode and effect analysis\n")

            f.write(f"## Pareto chart\n")

    def abstract(self):
        save_path_file = os.path.join(self.tpath, 'abstract.md')
        with open(save_path_file, "w") as f:
            f.write(f"# Abstract\n")
            f.write("---\n")
            f.write("This technique builds a model of the system and tries to solve it in the model. "
                    "Of course it helps if the model is close to real world. \n")

    def analogy(self):
        save_path_file = os.path.join(self.tpath, 'analogy.md')
        with open(save_path_file, "w") as f:
            f.write(f"# Analogy\n")
            f.write("---\n")

    def backwards(self):
        save_path_file = os.path.join(self.tpath, 'backwards.md')
        with open(save_path_file, "w") as f:
            f.write(f"# Backwards\n")
            f.write("---\n")

    def brainstorming(self):
        save_path_file = os.path.join(self.tpath, 'brainstorming.md')
        with open(save_path_file, "w") as f:
            f.write(f"# Brainstorming\n")
            f.write("---\n")

    def break_and_sort(self):
        save_path_file = os.path.join(self.tpath, 'breakandsort.md')
        with open(save_path_file, "w") as f:
            f.write(f"# Break and Sort\n")
            f.write("---\n")

    def divide_and_conquer(self):
        save_path_file = os.path.join(self.tpath, 'divideandconquer.md')
        with open(save_path_file, "w") as f:
            f.write(f"# Divide and Conquer\n")
            f.write("---\n")

    def hypothesis_testing(self):
        save_path_file = os.path.join(self.tpath, 'hypothesistesting.md')
        with open(save_path_file, "w") as f:
            f.write(f"# Hypothesis testing\n")
            f.write("---\n")

    def means_end_analysis(self):
        save_path_file = os.path.join(self.tpath, 'meansendanalysis.md')
        with open(save_path_file, "w") as f:
            f.write(f"# Means End Analysis\n")
            f.write("---\n")

    def method_of_focal_objects(self):
        save_path_file = os.path.join(self.tpath, 'methodoffocalobjects.md')
        with open(save_path_file, "w") as f:
            f.write(f"# Method of Focal Objects\n")
            f.write("---\n")

    def morphological_analysis(self):
        save_path_file = os.path.join(self.tpath, 'morphologicalanalysis.md')
        with open(save_path_file, "w") as f:
            f.write(f"# Morphological Analysis\n")
            f.write("---\n")

    def ney_proof(self):
        save_path_file = os.path.join(self.tpath, 'neyproof.md')
        with open(save_path_file, "w") as f:
            f.write(f"# Ney Proof\n")
            f.write("---\n")

    def reduction(self):
        save_path_file = os.path.join(self.tpath, 'reduction.md')
        with open(save_path_file, "w") as f:
            f.write(f"# Reduction\n")
            f.write("---\n")