import atheris
import sys
import argparse
import yaml
import io
from read_arguments import read_arguments

@atheris.instrument_func
def test_one_input(data):
    fdp = atheris.FuzzedDataProvider(data)
    try:
        file_patterns = fdp.ConsumeUnicode(atheris.ALL_BYTES)
        dir_patterns = fdp.ConsumeUnicode(atheris.ALL_BYTES)
        actions = fdp.ConsumeUnicode(atheris.ALL_BYTES)
        config = fdp.ConsumeUnicode(atheris.ALL_BYTES)
        verbose = fdp.ConsumeBool()

        sys.argv = ["read_arguments.py"]
        if file_patterns:
            sys.argv += ["--file_patterns", file_patterns]
        if dir_patterns:
            sys.argv += ["--dir_patterns", dir_patterns]
        if actions:
            sys.argv += ["--actions", actions]
        if config:
            sys.argv += ["--config", config]
        if verbose:
            sys.argv += ["--verbose"]

        read_arguments()
    except UnicodeDecodeError:
        pass  # Ignore inputs that can't be decoded into strings
    except SystemExit:
        pass  # Ignore SystemExit (which can be caused by argparse)

def main():
    atheris.setup(sys.argv, test_one_input)
    atheris.run()

if __name__ == "__main__":
    main()