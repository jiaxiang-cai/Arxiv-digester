import argparse
import configparser
import sys
import basic_search_tool as bst
import advanced_search_tool as ast

def cli_runtime():
    exit(0)

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    if config['Advanced_search_option']['enable'] == True:
        ast.advanced_search(config)
        exit(0)
    subparser = argparse.ArgumentParser()

    if len(sys.argv) == 1:
        cli_runtime()
    
    subparser.add_argument('-i', '--history', )

    exit(0)