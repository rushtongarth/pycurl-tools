import argparse

parser = argparse.ArgumentParser(
    description='Convert libcurl to pycurl.'
)
parser.add_argument(
    '-f', '--file',
    type=str, 
    nargs='?',
    help='Input file to convert to pycurl code'
)
parser.add_argument(
    '-o', '--output',
    type=str,
    nargs='?',
    help='File where output should be written'
)
parser.add_argument(
    '-v','--verbose',
    action='store_true',
    help='Print the conversion to standard out even if writing to file'
)
