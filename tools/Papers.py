import os
from PyInquirer import prompt


class Papers:
    def __init__(self, path):
        print("*** INFO: Papers tool")
        self.path = path

    def setup(self):
        questions = [
            {
                'type': 'input',
                'name': 'title',
                'message': 'What is the title of the paper?',
            },
            {
                'type': 'input',
                'name': 'link',
                'message': 'Link to the paper: ',
            },
            {
                'type': 'input',
                'name': 'location',
                'message': 'Where do you want to create this doc on local disk? ',
            },
            {
                'type': 'input',
                'name': 'name',
                'message': 'What do you want to name this doc as? ',
            }
        ]
        answers = prompt(questions)
        path = os.path.join(self.path, answers['location'])
        if not os.path.exists(path):
            print(f"This path does not exists. {path}")
        else:
            save_path_file = os.path.join(path, f"{answers['name']}.md")
            with open(save_path_file, "w") as f:
                f.write(f"# {answers['title']}\n")
                f.write("---\n")

                f.write('## Source\n')
                f.write(f"{answers['link']}\n")

                f.write("## Abstract\n")
                f.write('Your paraphrased abstract goes here\n')

                f.write("## Conclusion\n")
                f.write('Your paraphrased conclusion goes here\n')

                f.write("## Key Questions\n")
                f.write('1. What problem is the study trying to solve? : \n')
                f.write('2. Are the findings well supported by evidence? : \n')
                f.write('3. Are the findings unique and supported by others in the field? : \n')
                f.write('4. What was the sample size? : \n')
                f.write('5. Are samples representative of larger population? : \n')
                f.write('6. Is the study repeatable? : \n')
                f.write('7. What factors might affect the result? : \n')
                f.write('8. Have you examined the graphs and tables carefully? : \n')
                f.write('9. Have you tried interpreting the graphs and data before reading caption? : \n')

                f.write("## Key People\n")
                f.write('Authors\n')

                f.write("## Related Works\n")
                f.write('Details about related goes here\n')

                f.write("## Other details\n")
                f.write('Any other details.\n')