import argparse
import re
import os

DEFAULT_ENVIRONMENT_FILE='environment.yml'

def load_env_file(env_file_path):
    with open(env_file_path) as f:
        return f.read().splitlines()

def save_env_file(env_file_path, env_file_list_string):
    env_file_list_string = [l + '\n' for l in env_file_list_string]
    with open(env_file_path, 'w') as f:
        f.writelines(env_file_list_string)

def remove_build_number_version(env_file_list_string):
    """
    remove build number version from env.yml file for conda package but not from pip package
    """
    return ['='.join(re.split(r'[=](?=[^=])', l)[0:2]) for l in env_file_list_string]



if __name__== '__main__':
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help='commands', dest='command')

    env_parser = subparsers.add_parser('env', help='env management')
    env_parser.add_argument('action', action='store', help='env action', choices=('clean-file',))


    env_parser.add_argument('-f', '--file', action='store', dest='file_path', default=DEFAULT_ENVIRONMENT_FILE,
                            help='file path (DEFAULT : ' + DEFAULT_ENVIRONMENT_FILE + ')', metavar='file')
    env_parser.add_argument('-e', '--env', action='store', dest='env_name', help='conda env name (DEFAULT : active env)', metavar='name')

    args = parser.parse_args()

    if args.command == 'env':
        if args.action == 'clean-file':
            env_content = load_env_file(args.file_path)
            env_content = remove_build_number_version(env_content)
            save_env_file(args.file_path, env_content)
        pass





