"""
Project name: arXiv digestor
Author: Jiaxiaang Cai, Shiyi Gao
"""

import argparse
import configparser
import sys, os

import cli_mode as cm
import basic_search_tool as bst
import advanced_search_tool as ast

def transfer_to_download_mode(download_cmd, download_path):
    criterion = ['--rel', '--lud', '--smd']
    order = ['--des', '--asc']
    if len(download_cmd) > 4:
        exit('The maximal length of input arguments should not exceed 4')

    if len(download_cmd) == 1:
        bst.arxiv_search(download_path, download_cmd[0], 10, '--rel', '--des')
        # The default setting
        
    # now the length of arguments is limited to 2, 3, 4, treat them separately
    if download_cmd[1].isdigit() and not download_cmd[1] == 0:
        if len(download_cmd) == 2:
            bst.arxiv_search(download_path, download_cmd[0], int(download_cmd[1]), '--rel', '--des')
        elif len(download_cmd) == 3:
            if download_cmd[2] in criterion:
                bst.arxiv_search(download_path, download_cmd[0], int(download_cmd[1]), download_cmd[2], '--des')
            else:
                exit('Please enter legal input for parameter search_criterion')
        elif len(download_cmd) == 4:
            if download_cmd[2] in criterion and download_cmd[3] in order:
                bst.arxiv_search(download_path, download_cmd[0], int(download_cmd[1]), download_cmd[2], download_cmd[3])
            else:
                exit('Please enter legal input for parameters search_criterion and search_order')
    else:
        exit('Please enter integer digit for the parameter num_download')


if __name__ == '__main__':
    
    config = configparser.ConfigParser()
    config.read('config.ini')
    save_path = config['download_option']['save_folder']
    # first read configuration from config.ini
    download_path = os.path.join(os.getcwd(), save_path)
    if not os.path.exists(save_path):
        os.mkdir(save_path)
        # create the folder for downloaded paper if not exists


    if config['advanced_search'].getboolean('enable') == True:
        ast.advanced_search(config)
        exit(0)
    # advanced search mode, read settings in './config.ini' and perform desired operation.

    if len(sys.argv) == 1:
        cm.cli_mode(download_path)
    # no arguments given, start cli mode to ask the user to provide information.

    # cli parser below
    parser = argparse.ArgumentParser(description="Search tool for arXiv")
    switch = parser.add_mutually_exclusive_group()
    # history and download methods are mutually exclusive.
    switch.add_argument('-i', '--history', 
                        help="display previous search", action='store_true')
    switch.add_argument('-d', '--download', 
                        help="usage: [download] = search_term num_download(optional, default 10) search_criterion(optional) search_order(optional)", 
                        nargs='+', type=str)
    
    args = parser.parse_args()
    
    if not args.history:
        transfer_to_download_mode(args.download, download_path)
    
    bst.show_history()
        
    exit(0)