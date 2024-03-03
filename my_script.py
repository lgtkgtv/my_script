import argparse
from read_arguments import read_arguments
from input_validation import input_validation
from file_selection import select_files
from file_actions import perform_action_on_files


def main():
    args = read_arguments()

    try:
        args = input_validation(args)
    except (ValueError, argparse.ArgumentError) as e:
        print(e)
        return

    # Select files based on input patterns
    matched_files = select_files(args.file_patterns, args.dir_patterns)

    # Perform specified actions on selected files
    if args.actions:
        perform_action_on_files(matched_files, args.actions)

if __name__ == "__main__":
    main()