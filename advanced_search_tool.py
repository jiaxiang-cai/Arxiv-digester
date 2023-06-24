import basic_search_tool as bst
import arxiv

def advanced_search(config, download_path):
    advanced_search_config = config['advanced_search']

    if advanced_search_config['search_criteria'] not in bst.criteria_decode:
        print('Invalid search criteria')
        exit(1)

    criteria =advanced_search_config['search_criteria']
    
    if advanced_search_config['search_order'] not in bst.order_decode:
        print('Invalid sort order')
        exit(1)

    order = advanced_search_config['search_order']

    if not advanced_search_config['num_download'].isdigit():
        print('Invalid number of downloads')
        exit(1)
    
    num_download = int(advanced_search_config['num_download'])

    if num_download == 0:
        num_download = 10
        # default value

    query_list = []
    if advanced_search_config.getboolean('query_title') == True and advanced_search_config.getboolean('query_abstract') == True:
        query_list.append('ti:' + advanced_search_config['title'])
        query_list.append(' ' + advanced_search_config['title_abstract_relation'] + ' ')
        query_list.append('ab:' + advanced_search_config['abstract'])

    elif advanced_search_config.getboolean('query_title') == True:
        query_list.append('ti:' + advanced_search_config['title'])

    else:
        query_list.append('ab:' + advanced_search_config['abstract'])
    
    if advanced_search_config.getboolean('query_author') == True and not query_list == []:
        query_list.append(' AND ')
        query_list.append('au:' + advanced_search_config['author'])
    elif query_list == [] and advanced_search_config.getboolean('query_author') == True:
        query_list.append('au:' + advanced_search_config['author'])

    if query_list != []:
        query_term = "".join(query_list)
        # print(query_term)
        bst.arxiv_search(download_path, query_term, num_download, criteria, order)

    return

