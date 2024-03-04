import unittest
from unittest.mock import patch, mock_open
import argparse
import yaml
import my_script  # replace with the actual name of your script

class TestReadArguments(unittest.TestCase):
    # Existing test
    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(file_patterns='*.txt,*.docx', dir_patterns='./tests,/home/s/Downloads', actions='list_files,sanitize_filename', config=None, verbose=False))
    def test_read_arguments(self, mock_args):
        args = my_script.read_arguments()
        self.assertEqual(args.file_patterns, ['*.txt', '*.docx'])
        self.assertEqual(args.dir_patterns, ['./tests', '/home/s/Downloads'])
        self.assertEqual(args.actions, ['list_files', 'sanitize_filename'])

    # Test when no arguments are provided
    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(file_patterns=None, dir_patterns=None, actions=None, config=None, verbose=False))
    def test_no_arguments(self, mock_args):
        args = my_script.read_arguments()
        self.assertIsNone(args.file_patterns)
        self.assertIsNone(args.dir_patterns)
        self.assertIsNone(args.actions)

    # Test when only one type of argument is provided
    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(file_patterns='*.txt', dir_patterns=None, actions=None, config=None, verbose=False))
    def test_one_argument(self, mock_args):
        args = my_script.read_arguments()
        self.assertEqual(args.file_patterns, ['*.txt'])
        self.assertIsNone(args.dir_patterns)
        self.assertIsNone(args.actions)

    # Test when the config argument is provided
    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(file_patterns=None, dir_patterns=None, actions=None, config='config.yaml', verbose=False))
    @patch('builtins.open', new_callable=mock_open, read_data=yaml.dump({'file_patterns': ['*.txt', '*.docx'], 'dir_patterns': ['./tests', '/home/s/Downloads'], 'actions': ['list_files', 'sanitize_filename']}))
    def test_config_argument(self, mock_file, mock_args):
        args = my_script.read_arguments()
        self.assertEqual(args.file_patterns, ['*.txt', '*.docx'])
        self.assertEqual(args.dir_patterns, ['./tests', '/home/s/Downloads'])
        self.assertEqual(args.actions, ['list_files', 'sanitize_filename'])

    # Test when the verbose flag is set
    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(file_patterns=None, dir_patterns=None, actions=None, config=None, verbose=True))
    def test_verbose_flag(self, mock_args):
        args = my_script.read_arguments()
        self.assertTrue(args.verbose)

    # Test when invalid arguments are provided
    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(file_patterns='*.txt', dir_patterns='./tests', actions='invalid_action', config=None, verbose=False))
    def test_invalid_arguments(self, mock_args):
        with self.assertRaises(ValueError):
            my_script.read_arguments()

    # Test when the config file is empty
    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(file_patterns=None, dir_patterns=None, actions=None, config='config_empty.yaml', verbose=False))
    @patch('builtins.open', new_callable=mock_open, read_data="")
    def test_empty_config_file(self, mock_file, mock_args):
        with self.assertRaises(ValueError):
            my_script.read_arguments()

    # Test when the config file has invalid actions
    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(file_patterns=None, dir_patterns=None, actions=None, config='config_invalid_actions.yaml', verbose=False))
    @patch('builtins.open', new_callable=mock_open, read_data=yaml.dump({'file_patterns': ['*.txt', '*.docx'], 'dir_patterns': ['./tests', '/home/s/Downloads'], 'actions': ['invalid_action']}))
    def test_invalid_actions_in_config_file(self, mock_file, mock_args):
        with self.assertRaises(ValueError):
            my_script.read_arguments()

if __name__ == '__main__':
    unittest.main()
    