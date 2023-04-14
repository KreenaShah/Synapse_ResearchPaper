from selenium import webdriver
from selenium.webdriver.common.by import By

# Replace the following variables with the URL of the website
# and the path to the chromedriver executable on your machine
website_url = "https://github.com/facebook/react/commits"
chromedriver_path = "/path/to/chromedriver"

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
# Run Chrome in headless mode to avoid opening a browser window
chrome_options.add_argument("--headless")

# Create a new Chrome WebDriver instance
browser = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

# Navigate to the website
browser.get(website_url)

# bold_text =  browser.find_elements(By.XPATH, "//a[@class='Link--primary text-bold js-navigation-open markdown-title']")

inner_text_commit_lines = []
# inner_text_button = browser.find_elements(By.CLASS_NAME, 'ellipsis-expander js-details-target btn')
inner_text_button = browser.find_elements(By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/ol/li[1]/div[1]/p/span/button')
print('sderft',inner_text_button)
for inner_text_btn in inner_text_button:
    inner_text_btn.click()
    print("hey")
    # inner_text = browser.find_elements(By.CLASS_NAME, 'text-small ws-pre-wrap')
    inner_text = browser.find_elements(By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/ol/li[1]/div[1]/div[1]/pre')
    for element in inner_text:
        commit = element.text
        print("commit",commit)
        inner_text_commit_lines.append(commit)

# bold_text_commit_lines = []
# for element in bold_text:
#     commit = element.text
#     bold_text_commit_lines.append(commit)
# print(bold_text_commit_lines)


print(inner_text_commit_lines)


# # //*[@id="repo-content-pjax-container"]/div/div[2]/div[2]/div[2]/h2
# commit_date = []
# date_fields = browser.find_elements(By.XPATH,'//*[@id="repo-content-pjax-container"]/div/div[2]/div[{0}]/div[2]/h2'.format(i))
# for date_field in date_fields:
#     date = date_field.text
#     commit_date.append(date)
# print(commit_date)

# Normal Commits ( jo dikh raha hai vo line )
# commits = []
# elements = browser.find_elements(By.XPATH, "//a[@class='Link--primary text-bold js-navigation-open markdown-title']")
# for element in elements:
#     commit = element.text
#     commits.append(commit)
# print(commits)

# Close the browser
browser.quit()
