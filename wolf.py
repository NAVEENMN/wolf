from PyInquirer import prompt
from tools.Research import Research
from tools.Problems import Problems
from tools.Papers import Papers
from tools.Investigations import Investigations
from tools.Innovent import Innovent
from tools.DataScience import DataScience

question = [
        {
            'type': 'input',
            'name': 'rootpath',
            'message': 'Set your root path.\n',
            'default': '/Users/naveenmysore/Dropbox/obsidian'
        }
    ]
answers = prompt(question)
root_path = answers['rootpath']


def main():
    question = [
        {
            'type': 'list',
            'name': 'tools',
            'message': 'Please select the tool you wish to use.\n',
            'choices': ['research', 'problem', 'investigation', 'papers', 'ideas', 'queries', 'innovent'],
        }
    ]
    answers = prompt(question)
    tool = answers['tools']
    if tool == 'research':

        _question = [
            {
                'type': 'list',
                'name': 'rtype',
                'message': 'Please select the type of research you are conducting.\n',
                'choices': ['normal', 'datascience'],
            }
        ]
        _answer = prompt(_question)
        rtype = _answer['rtype']
        if rtype == 'normal':
            _research = Research(path=root_path)
            _research.setup()
        elif rtype == 'datascience':
            print("To Be Implemented")
            _datascience = DataScience(path=root_path)
            _datascience.setup()
        else:
            print("Invalid")
    elif tool == 'problem':
        _problems = Problems(path=root_path)
        _problems.setup()
    elif tool == 'investigation':
        _investigations = Investigations(path=root_path)
        _investigations.setup()
    elif tool == 'papers':
        _papers = Papers(path=root_path)
        _papers.setup()
    elif tool == "ideas":
        print("ideas: To be implemented")
    elif tool == "queries":
        print("queries: To be implemented")
    elif tool == 'innovent':
        _innovent = Innovent(path=root_path)
        _innovent.setup()
    else:
        print("*** INFO: Not a valid tool")

    print("*** INFO: Done.")


if __name__ == "__main__":
    main()
