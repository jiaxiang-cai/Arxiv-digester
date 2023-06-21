import arxiv
import json
import openpyxl
from openpyxl.utils import get_column_letter

def arxiv_search(search_term, num_download, criterion, order):
    search = arxiv.Search(
        query = search_term,
        max_results = 50, # API limit
        sort_by = arxiv.SortCriterion.SubmittedDate
    )
    save_result(search)
    result_download(search, num_download)

def save_result(search):
    # to get information we wanted, from https://pypi.org/project/arxiv/#example-downloading-papers make a dictionary contain all information for searched result
    results = []
    for result in search.results():
        # Extract relevant information from the search result
        result_info = {
            'title': result.title,
            'authors': result.authors,
            'abstract': result.summary,
            'upload_date': result.update,
            # Add more information as needed
        }
        results.append(result_info)

    # then save this dictionary in json file or excel file if needed.
    with open('search_results.json', 'w') as json_file:
        json.dump(results, json_file, indent=4)
# save in excel 

    save_result_excel(results)

def save_result_excel(results):
    wb = openpyxl.Workbook()
    ws = wb.active

    # Write the header row
    header = ['Title', 'Authors', 'Abstract', 'Upload Date']
    for col_num, column_title in enumerate(header, 1):
        col_letter = get_column_letter(col_num)
        ws[f"{col_letter}1"] = column_title

    # Write the data rows
    for row_num, result in enumerate(results, 2):
        ws[f"A{row_num}"] = result['title']
        ws[f"B{row_num}"] = ", ".join(result['authors'])
        ws[f"C{row_num}"] = result['abstract']
        ws[f"D{row_num}"] = result['upload_date']

    wb.save('search_results.xlsx')

# get url for pdf using result.pdf_url from https://pypi.org/project/arxiv/#example-fetching-results
import requests

def result_download(search, num_download):
    import requests

    num_download = 5  # Specify the number of papers to download

    results = search.results()
    downloaded_papers = []
    for i in range(num_download):
        try:
            result = next(results)
            pdf_url = result.pdf_url
            response = requests.get(pdf_url)
            downloaded_papers.append(response.content)
            print(f"Downloaded paper {i+1}/{num_download}")
        except StopIteration:
            print("Reached the end of search results.")
            break
        except Exception as e:
            print(f"Error occurred while downloading paper {i+1}: {str(e)}")

# Save downloaded papers as PDF files
    for i, paper in enumerate(downloaded_papers):
        try:
            with open(f"paper_{i+1}.pdf", "wb") as file:
                file.write(paper)
            print(f"Saved paper {i+1} as PDF file.")
        except Exception as e:
            print(f"Error occurred while saving paper {i+1}: {str(e)}")

