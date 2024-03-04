
# Prompts to help generate unit tests 

> write a unit test for the read_arguments() function
> show me the directory structure and step by step instructions to run the unit test

    my_scripts/
    │
    ├── read_arguments.py
    └── tests/
        └── test_read_arguments.py

    python -m unittest tests/test_read_arguments.py

> can you think of additional unit tests for the read_arguments() function
> Can you generate some example config.yaml files for the purpose of creating unit tests. Think about all the corner conditions.
> Can you modify the unittests for the read_arguments() function to include all test cases involving the configurations read from the YAML file
> Can you mearge these new unittests with the unittests that already exit for this function. Please generate the complete program listing  

> Some of the unit tests failed. Can you help me fix the problems
> how can i list all unit tests
> Show me all the tests that run successfully and tests that failed
> How can I run all the unit tests in a specific directory?


    python -m unittest discover -s directory
    python -m unittest discover -s tests -p '*_test.py'
    This will discover all *_test.py files in the tests directory and its subdirectories, and run them.


# To run unittests

cd my_scripts

python -m unittest tests.test_read_arguments.TestReadArguments
python -m unittest tests.test_read_arguments.TestReadArguments.test_read_arguments
python -m unittest tests.test_read_arguments.TestReadArguments.test_no_arguments

