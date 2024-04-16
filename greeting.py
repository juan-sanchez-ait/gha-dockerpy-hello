import os

def set_github_action_output(output_name, output_value):
    with open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a") as output:
        print(f'{output_name}={output_value}', file=output)

def run():
    name = os.getenv('INPUT_NAME', default="Stranger")
    set_github_action_output('greeting', f'Hello, {name}!')

if __name__ == '__main__':
    run()