import argparse
import yaml
import pprint

def read_arguments():
    """Read and parse command-line arguments and return them as a namespace object."""

    example_config = """
Example usages:

    python my_script --file_patterns="*.txt,*.docx" --dir_patterns="/tmp,./" --actions="list_files,sanitize_filename"
        OR
    python my_script --config=./config.yaml
   
        Example `config.yaml`: 

                file_patterns:
                - "*.txt"
                - "*.docx"
                dir_patterns:
                - "./tests"
                - "/home/s/Downloads"
                actions:
                - list_files
                - sanitize_filename
                - remove_files_with_zero_length
                - remove_duplicates
    """
    parser = argparse.ArgumentParser(description=f'''This program will perform a series of actions on all files selected based on comma separated input list of filename-patterns and directories. Optionally, it supports inputs from a YAML configuration file.
        {example_config}''', formatter_class=argparse.RawTextHelpFormatter)
    # parser = argparse.ArgumentParser(description=f"Utility to perform a series of actions on files selected based on a list of filename patterns and directories provided via YAML configuration file. {example_config}")
    """
    parser.add_argument("-f", "--file_patterns", type=str, default="*", help="Comma-separated list of filename patterns to search for (default: *)")
    parser.add_argument("-d", "--dir_patterns", type=str, default=".", help="Comma-separated list of directory patterns to search in (default: .)")
    parser.add_argument("-a", "--actions", type=str, default="list_files", choices=["sanitize_filename", "list_files", "remove_files_with_zero_length", "remove_duplicates"], help="Comma-separated list of actions to perform on matching files (default: list_files)")
    """
    parser.add_argument("-f", "--file_patterns", type=str, help="Comma-separated list of filename patterns to search for (default: *)")
    parser.add_argument("-d", "--dir_patterns", type=str, help="Comma-separated list of directory patterns to search in (default: .)")
    parser.add_argument("-a", "--actions", type=str, choices=["sanitize_filename", "list_files", "remove_files_with_zero_length", "remove_duplicates"], help="Comma-separated list of actions to perform on matching files (default: list_files)")

    parser.add_argument("-c", "--config", help="path for YAML configuration file to read input arguments")
    parser.add_argument('-v', '--verbose', action='store_true',help='enable verbose mode')
    args = parser.parse_args()

    if args.verbose:
        print()
        print("Command line Arguments:")
        pprint.pprint(vars(args),indent=4)
        print()

    # Default configuration to use when YAML configuration is not provided 
    yamlcfg_file_patterns = '*'
    yamlcfg_dir_patterns = '.'
    yamlcfg_actions = 'list_files'
    # If a configuration file was provided, read it and use its values
    if args.config:
        try:
            with open(args.config, 'r') as f:
                config = yaml.safe_load(f)

                yamlcfg_file_patterns = config.get('file_patterns', ['*'])
                yamlcfg_dir_patterns = config.get('dir_patterns', ['.'])
                yamlcfg_actions = config.get('actions', ['list_files'])

                if args.verbose:
                    print(f"Configuration read from the YAML:")
                    print(f"\tFile patterns: {yamlcfg_file_patterns}")
                    print(f"\tDirectory patterns: {yamlcfg_dir_patterns}")
                    print(f"\tActions: {yamlcfg_actions}")
                    print()

        except FileNotFoundError:
            print(f"Error: The file {args.config} was not found.")
            config = {}
        except yaml.YAMLError as e:
            print(f"Error: There was a problem with the format of the YAML file: {e}")
            config = {}

    # Override the YAML configuration and defaults with the command-line arguments if and when they are specified 
    args.file_patterns = args.file_patterns if args.file_patterns is not None else yamlcfg_file_patterns
    args.dir_patterns = args.dir_patterns if args.dir_patterns is not None else yamlcfg_dir_patterns
    args.actions = args.actions if args.actions is not None else yamlcfg_actions

    if args.verbose:
        print("Arguments after YAML configuration override checks:")
        pprint.pprint(vars(args),indent=4)
        print()

    # Split the file_patterns, dir_patterns, and actions arguments into lists
    args.file_patterns = args.file_patterns.split(',') if isinstance(args.file_patterns, str) else args.file_patterns
    args.dir_patterns = args.dir_patterns.split(',') if isinstance(args.dir_patterns, str) else args.dir_patterns
    args.actions = args.actions.split(',') if isinstance(args.actions, str) else args.actions    

    # Print all arguments
    if args.verbose:
        print("Arguments provided:")
        pprint.pprint(vars(args),indent=4)
        print("-------------------------------------------------------------")

    return args