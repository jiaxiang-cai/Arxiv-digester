import argparse
import configparser
import sys

import cli_mode as cm
import basic_search_tool as bst
import advanced_search_tool as ast



if __name__ == '__main__':
    
    config = configparser.ConfigParser()
    config.read('config.ini')
    # first read configuration from config.ini

    if config['advanced_search'].getboolean('enable') == True:
        ast.advanced_search(config)
        exit(0)
    # advanced search mode, read settings in './config.ini' and perform desired operation.

    if len(sys.argv) == 1:
        cm.cli_mode()
    # no arguments given, start cli mode to ask the user to provide information.

    main_parser = argparse.ArgumentParser(description="Search tool for arXiv, leave no additional cli element for cli mode",
                                          add_help=False)
    switch = main_parser.add_mutually_exclusive_group()
    # history and download methods are mutually exclusive.
    switch.add_argument('-i', '--history', 
                        help="Display previous search", action='store_true')
    switch.add_argument('-d', '--download', 
                        help="Search and download by title", 
                        metavar=("search_term", "n_down"), nargs=2, type=str)
    main_args, _ = main_parser.parse_known_args()

    parser = argparse.ArgumentParser(parents=[main_parser])
    if main_args.download != None:
        parser.add_argument('--rel', help="Search by relevance", action='store_false')
    args = parser.parse_args()

    exit(0)