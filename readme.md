<h1 align="center">arXiv Digester</h1>

## About our project

This project is aimed to yield a Python scipt run in cli to allow the users to:
*[1] [search] Perform search with some "search_term" and download N files from arXiv
*[2] [history] Record the download related command history as json or Excel files.
*[3] [dual-mode] Allow input with/without cli arguments.

Unfortunately, it is too hard for us to implement the advanced search tool, due to limited experience and time issue.
We hope we can complete it in the future if possible.
## Usage

### Installation
---bash
$ git clone https://github.com/jiaxiang-cai/Arxiv-digester.git
$ cd ./Arxiv-disgeter
$ pip install -r requirements.txt
---

### Search

---bash
$ python arxiv_digester.py [-d|--download] search_term num_download sort_criterion sort_order
---

*[search_term] specifies the keyword in search (mandatory)
*[num_download] Number of files you want to download (optional, 10 in default)
*[sort_criterion] (optional)
*    "--rel":=> Relevance (default)
*    "--smd":=> SubmittedDate
*    "--lud":=> LastUpdatedDate
*[sort_order] (optional)
*    "--des":=> Descending (default)
*    "--asc":=> Ascending

*PDF files would be saved in fthe folder specifies at config.ini (in default ./articles)
*In config.ini, save_excel allows user to trigger if he/she wants to save the result as Excel file 'history.xlsx' for future review.

*The download log will be saved in 'history.json', please do not delete it if you don't want to download duplicate files.

### History

---bash
$ python arxiv_digester.py [-i|--history]
---

*Load data from history.json, user can preview the search_term, what time the search was conducted, how many files retrived with a user friendly interface.


# Contributer
* [Jiaxiang cai](https://github.com/jiaxiang-cai)
* [Shiyi gao](https://github.com/shiyig233)

# Tester