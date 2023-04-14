from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://github.com/facebook/react/issues'

driver = webdriver.Chrome()

driver.get(url)

issues_element = driver.find_element(
    By.XPATH, "//*[@id='issues-repo-tab-count']")

pulls_element = driver.find_element(
    By.XPATH, "//*[@id='pull-requests-repo-tab-count']")

stars_element = driver.find_element(
    By.XPATH, "//*[@id='repo-stars-counter-star']")

fork_element = driver.find_element(
    By.XPATH, "//*[@id='repo-network-counter']")

# watch_element = driver.find_element(
#     By.ID, "repo-notifications-counter")

# wait = WebDriverWait(driver, 10)
# watch_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='repo-notifications-counter']")))

text = issues_element.text
if 'k' in text:
    num_issues = float(float(text[:-1]) * 1000)
else:
    num_issues = float(text)

text = pulls_element.text
if 'k' in text:
    num_pulls = float(float(text[:-1]) * 1000)
else:
    num_pulls = float(text)

text = stars_element.text
if 'k' in text:
    num_stars = float(float(text[:-1]) * 1000)
else:
    num_stars = float(text)

text = fork_element.text
if 'k' in text:
    num_fork = float(float(text[:-1]) * 1000)
else:
    num_fork = float(text)

# text = watch_element.text
# if 'k' in text:
#     num_watch = float(text.replace('k', '000'))
# else:
#     num_watch = float(text)


# num_issues = int(issues_element.text)
# num_pulls = int(pulls_element.text)
# num_stars = int(stars_element.text)

print(num_issues)
print(num_pulls)
print(num_stars)
print(num_fork)
# print(num_watch)

driver.quit()
