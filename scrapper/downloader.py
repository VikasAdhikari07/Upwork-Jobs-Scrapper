from selenium import webdriver

def html_loader(upwork_url):
    try:    
        website = upwork_url
        driver = webdriver.Chrome()
        driver.get(website)
        button = driver.find_element("xpath", '//*[@id="main"]/div/div/div[3]/section[2]/div/div[3]/a')
        button.click()
        html = driver.page_source
        driver.quit()
        return html
    except Exception as e:
        print(f'The error is: {e}')
        return None
