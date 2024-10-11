from scrapper.downloader import html_loader
from scrapper.exporter import google_sheet_transfer
from scrapper.parser import job_wrapper_list, parsed_pandas_table

def main(url):
    page_source = html_loader(url)
    job_list = job_wrapper_list(pageSource=page_source) 
    job_table = parsed_pandas_table(job_list)
    job_table.to_csv("Jobs.csv")
    google_sheet_transfer(job_table)


if __name__ == '__main__':
    # Example URL (change to your target URL)
    url = 'https://www.upwork.com/freelance-jobs/machine-learning/'
    main(url)