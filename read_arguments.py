import argparse
import yaml
import pprint

def read_arguments():
    example_config = """
    Example config.yaml:
    file_patterns: "*.txt,*.docx"
    dir_patterns: "/home/user/documents,/home/user/downloads"
    actions:
      - list_files
      - sanitize_filename
      - remove_files_with_zero_length
      - remove_duplicates
    """
    # parser = argparse.ArgumentParser(description=f'Process some integers. {example_config}')

    example_config = """
Example usages:

    python my_script --file_patterns="*.txt,*.docx" --dir_patterns="/tmp,./" --actions="list_files,sanitize_filename"

        OR

    python my_script --config=./config.yaml
   
        Example `config.yaml`: 

            file_patterns: "*.txt,*.docx"
            dir_patterns: "/home/user/documents,/home/user/downloads"
            actions:
            - list_files
            - sanitize_filename
            - remove_files_with_zero_length
            - remove_duplicates
    """
    parser = argparse.ArgumentParser(description=f'''This program will perform a series of actions on all files selected based on comma separated input list of filename-patterns and directories. Optionally, it supports inputs from a YAML configuration file.
        {example_config}''', formatter_class=argparse.RawTextHelpFormatter)
    # parser = argparse.ArgumentParser(description=f"Utility to perform a series of actions on files selected based on a list of filename patterns and directories provided via YAML configuration file. {example_config}")
    parser.add_argument("-f", "--file_patterns", type=str, default="*", help="Comma-separated list of filename patterns to search for (default: *)")
    parser.add_argument("-d", "--dir_patterns", type=str, default=".", help="Comma-separated list of directory patterns to search in (default: .)")
    parser.add_argument("-a", "--actions", type=str, default="list_files", choices=["sanitize_filename", "list_files", "remove_files_with_zero_length", "remove_duplicates"], help="Comma-separated list of actions to perform on matching files (default: list_files)")
    parser.add_argument("-c", "--config", help="YAML configuration file to specify inputs")
    parser.add_argument('-v', '--verbose', action='store_true',help='enable verbose mode')
    args = parser.parse_args()

    if args.verbose:
        print("Starting function read_arguments")

    # If a configuration file was provided, read it and use its values
    if args.config:
        with open(args.config, 'r') as f:
            config = yaml.safe_load(f)
        default_file_patterns = config.get('file_patterns', '*')
        default_dir_patterns = config.get('dir_patterns', '.')
        default_actions = config.get('actions', 'list_files')
    else:
        default_file_patterns = '*'
        default_dir_patterns = '.'
        default_actions = 'list_files'

    # Override the configuration values with the command-line arguments if they are not the default values
    args.file_patterns = args.file_patterns if args.file_patterns != '*' else default_file_patterns
    args.dir_patterns = args.dir_patterns if args.dir_patterns != '.' else default_dir_patterns
    args.actions = args.actions if args.actions != 'list_files' else default_actions

    # Split the file_patterns, dir_patterns, and actions arguments into lists
    args.file_patterns = args.file_patterns.split(',') if args.file_patterns else []
    args.dir_patterns = args.dir_patterns.split(',') if args.dir_patterns else []
    args.actions = args.actions.split(',') if args.actions else []

    # Print all arguments
    if args.verbose:
        print("Arguments:")
        pprint.pprint(vars(args))

    return args