# Prompts 1

Here are all the prompts provided during this session:

Write a Python utility to perform the following.
- The utility shall take a list of filename patterns as required input. At least one filename pattern must be provided.
- The utility shall take a list of directories as required input. Allow wildcards and relative paths in directory names. At least one directory pattern must be provided.
- Allow wildcard in input file and directory names.
- The utility shall recursively scan all the directories and select all the files matching the specified filename patterns.

The utility shall also provide a command-line option for an easy way to specify all the required and optional inputs from a YAML file.
- The utility shall provide help if required inputs are not provided.
- Provide help if an invalid or unsafe filename pattern is provided as input.
- Provide help if an invalid or unsafe directory name is provided as input.
- Do not allow unsafe file and directory names that are considered as system files or part of the operating system or require administrative privilege.

Can you make `if action == "sanitize_filename":` a separate function?

Now I want to add a few more actions. Let's start with `--action=remove_files_with_zero_length` to remove files with zero length.

Now add this action `--action=list_system_files` shall list system files that are considered as unsafe for modifications by unprivileged users.

In the previous step, modify the action to list and report files that are considered as unsafe for modifications by unprivileged users for each of the operating systems such as Windows OS, MacOS, and Linux OS flavors.

Can you improve the list of directories for each operating system?

Let us modify the input validations done by this script and add checks to not allow any directory paths associated with common system directories where sensitive files are often located.

Rename `scan_files()` to say `select_files()` to return matched files. Also, move the `perform_action_on_files(matched_files, action)` to the main higher-level function.

For better readability move this code fragment into a separate function and call it `input_validations()`.

For better readability move `input_validations()`, `select_files()`, `perform_actions()` into separate files.

I am thinking we no longer need the `def list_system_files(files)` option.

If input_validation fails, I want us to provide the help showing the command syntax and an example YAML file. In the example YAML file add comments to clarify that directories with system files are not allowed.

Modify the code so that we can perform multiple actions as specified by their sequence on the command line or in the YAML file.

In the `file_actions` module, assume that each `--action` upon the selected set of file may return a new list of files and the subsequent actions should take that new list of files.

For the `file_actions` module I want to add a new action `--action=remove_duplicates` to detect and remove files with duplicate content. You should provide a dialog listing all the files with duplicate contents and make the user select which file to persist and remove the rest.

Do we also need to modify the `main.py` for this newly added action?

Please provide the complete listing for all the modules, main program, and an example YAML configuration file with appropriate comments.

Can you also list all the prompts i provide to you during this session? 
