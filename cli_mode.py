import os
import basic_search_tool as bst

cli_instruction = """
    This is a crawling tool for arXiv, utilizing the official API.
    The cli mode is for basic use, for advanced application please edit config.ini and directly execute the arxiv_digester.py

    Please enter the mode:
    [s] Search mode
    [h] Display history

    """
mode_option = ('s', 'h')


def search_mode(download_path):
    search_term = input('Please enter the search term:\n')

    num_download = input('Please enter the number of files you want to retrive, press enter for default setting\n')
    while not num_download.isdigit():
        if num_download == '':
            num_download = 10
            break
        else:
            num_download = input('Illegal input, please enter a number or press enter for default setting:\n')

    sort_by = input('Please enter the sort criterion:\n[1] Relevance\n[2] Submission Date\n[3] Last updated date\n')
    while sort_by not in ['1', '2', '3']:
        sort_by = input('Illegal input, please enter a valid number:\n')

    if sort_by == '1':
        sort_by = '--rel'
    elif sort_by == '2':
        sort_by = '--smd'
    else:
        sort_by = '--lud'
    
    sort_order = input('Please enter the sort order:\n[1] Ascending\n[2] Descending\n')
    while sort_order not in ['1', '2']:
        sort_order = input('Illegal input, please enter a valid number:\n')
    
    if sort_order == '1':
        sort_order = '--asc'
    else:  
        sort_order = '--des'
    
    bst.arxiv_search(download_path, search_term, num_download, sort_by, sort_order)

    
    return

def cli_mode(download_path):
    print(cli_instruction)
    mode = input('Please enter the mode:\n').lower()

    if mode not in mode_option:
        _ = input('Illegal input, press any key to reenter.')
        bst.cls()
        cli_mode(download_path)
    
    if mode == 's':
        search_mode(download_path)
    
    if mode == 'h':
        bst.show_history()

    exit(0)

if __name__ == '__main__':
    cli_mode()