<h1 align="center">arXiv Digester</h1>

## About our project

This project is aimed to yield a Python scipt run in cli to allow the users to:
*   [1] [search] Perform search with some "search_term" and download N files from arXiv
*   [2] [history] Record the download related command history as json or Excel files.
*   [3] [dual-mode] Allow input with/without cli arguments.

Unfortunately, the advance search mode is only partially functional with limited usage, but following https://info.arxiv.org/help/api/user-manual.html#query_details you can compose your search option in cli mode. (If you don't want to input parameter in the config.ini)
## Usage

### Installation
```bash
$ git clone https://github.com/jiaxiang-cai/Arxiv-digester.git
$ cd ./Arxiv-disgeter
$ pip install -r requirements.txt
```

### Search

```bash
$ python arxiv_digester.py [-d|--download] search_term num_download sort_criterion sort_order
```

[search_term] 
*   specifies the keyword in search (mandatory)

[num_download] 
*   Number of files you want to download (optional, 10 in default)

[sort_criterion] (optional)
*    --rel :=> Relevance (default)
*    --smd :=> SubmittedDate
*    --lud :=> LastUpdatedDate

[sort_order] (optional)
*    --des :=> Descending (default)
*    --asc :=> Ascending



PDF files would be saved in fthe folder specifies at config.ini (in default ./articles)

In config.ini, save_excel allows user to trigger if he/she wants to save the result as Excel file 'history.xlsx' for future review.

The download log will be saved in 'history.json', please do not delete it if you don't want to download duplicate files.

### History

```bash
$ python arxiv_digester.py [-i|--history]
```

*   Load data from history.json, user can preview the search_term, what time the search was conducted, how many files retrived with a user friendly interface.

### Directly excute the script

```bash
$ python arxiv_digester.py
```

If the advance search is turned off (in config.ini), you will enter a cli program to compose your own query term

#### Advance search
If the advance search is turned on, you can compose your search option in config.ini

* You can choose to search by title, abstract or both (with relation 'and' or 'or')
* You can search in specific category, following https://arxiv.org/category_taxonomy

# Contributer
* [Jiaxiang cai](https://github.com/jiaxiang-cai)
* [Shiyi gao](https://github.com/shiyig233)

# Reviewer
* [Aditi Kakkad]