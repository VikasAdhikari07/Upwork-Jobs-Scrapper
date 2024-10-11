from bs4 import BeautifulSoup
import pandas as pd

def job_wrapper_list(pageSource):
    soup = BeautifulSoup(pageSource,'html.parser')
    jobs = soup.findAll("section",class_="air3-card air3-card-outline job-tile vs-cursor-pointer p-md-6x p-4x mb-md-6x")
    return jobs

def parsed_pandas_table(jobs_wrapper_list):
    jobs_worksheet = pd.DataFrame(columns=["Job Title","Experience Required","Skills Required","Pay","Time Required","Discription","Job Link"])

    for jobs in jobs_wrapper_list:
        row = []
        # Jobtitle 
        jobtitle = jobs.find('a', class_='up-n-link d-block display-u2u job-title h5 mb-3x').text[9:-7]
        row.append(jobtitle)

        # Experience Required
        exp_req = jobs.find('p',class_="span-6 span-md-4 mb-0 pb-4x pb-md-6x").find('strong')
        row.append(exp_req.text)

        # Skills Required
        skills_with_tag = jobs.find('div',class_="skills-list mb-0").findAll("span")
        skills = ", ".join([" ".join(i.text.split()) for i in skills_with_tag])
        row.append(skills)

        # pay
        pay_or_time = " ".join(jobs.find('p').text.split())

        # Pay
        if("price" in pay_or_time):
            row.append(pay_or_time)
            row.append("Fixed Time")
        # Time
        else:
            row.append("Payment to be Determined")
            row.append(pay_or_time)

        # Discription
        discription = jobs.find('p', class_="mt-0 pt-0 text-body mb-6x job-description")
        row.append(discription.text)

        # Job Link
        link = "https://www.upwork.com" + jobs.find('a').get("href")
        row.append(link)

        
        jobs_worksheet.loc[len(jobs_worksheet)] = row
        
    return jobs_worksheet
