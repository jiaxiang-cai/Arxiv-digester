import arxiv
import json
import openpyxl

def arxiv_search(search_term, num_download, criterion, order):
    search = arxiv.Search(
        query = search_term,
        max_results = 300000, # API limit
        sort_by = criterion,
        sort_order = order
    )
    save_result(search)
    result_download(search, num_download)

def save_result(search):
    return

def result_download(search, num_download):
    return
