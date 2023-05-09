from selenium import webdriver

from selenium.webdriver.common.by import By
import re
import pandas as pd
import os

# url='https://github.com/facebook/react/pulls'
driver = webdriver.Chrome()
# driver.get(url)
name=['Facebook React']
readme = []
list_of_commits=[]
list_of_pulls=[]
total_pulls=0
list_of_issues=[]
total_issues=0
page_number=0
new_url_pulls='https://github.com/facebook/react/pulls'
new_url_issues='https://github.com/facebook/react/issues'
new_url_readme='https://github.com/facebook/react'
new_url_commits='https://github.com/facebook/react/commits/main'

# pulls function
def get_pulls(url):
    global total_pulls
    
    url = str(url)
    driver.get(url)
    issues = driver.find_elements(By.CLASS_NAME,'markdown-title')
    total_pulls = total_pulls+len(issues)
    for issue in issues:
        list_of_pulls.append(issue.text)
    next_btn = driver.find_elements(By.CLASS_NAME,'next_page') 
    return next_btn[0].get_attribute('href')

# issue function
def get_issues(url):
    global total_issues
    
    url = str(url)
    driver.get(url)
    issues = driver.find_elements(By.CLASS_NAME,'markdown-title')
    total_issues = total_issues+len(issues)
    for issue in issues:
        list_of_issues.append(issue.text)
    next_btn = driver.find_elements(By.CLASS_NAME,'next_page') 
    return next_btn[0].get_attribute('href')

# commit function
def get_commits(url):
    global total_commits
    global page_number
    
    
    url=url
    driver.get(url)
   
    commits = driver.find_elements(By.CLASS_NAME,'markdown-title')
    page_number+=1
    
    for commit in commits:
        # if commit.exists():
            list_of_commits.append(commit.text)
        # else:
            # pass 

    
    all_btn=driver.find_elements(By.CLASS_NAME,'BtnGroup-item')
    for btn in all_btn:
        if btn.text=='Older':
            older_btn_link=btn.get_attribute('href')
    return older_btn_link


#readme code
driver.get(new_url_readme)
readC = driver.find_elements(By.CLASS_NAME, "Box-body")
for i in range(len(readC)):
    readme.append(readC[i].text)




while(new_url_pulls!=None):
# for i in range(1):
    new_url_pulls=get_pulls(new_url_pulls)

while(new_url_issues!=None):
    new_url_issues=get_issues(new_url_issues)

while(new_url_commits!=None):
# for i in range(1):
    new_url_commits=get_commits(new_url_commits)


# print(total_pulls)
driver.close()

dataDf = pd.DataFrame()
# print(list_of_issues)

dataDf['commits'] = list_of_commits
list_of_pulls_padded = list_of_pulls.copy() 
list_of_pulls_padded.extend([0] * (len(dataDf) - len(list_of_pulls))) 
list_of_issues_padded = list_of_issues.copy()
list_of_issues_padded.extend([0]*(len(dataDf)-len(list_of_issues)))
readme_padded = readme.copy()
readme_padded.extend([0]*(len(dataDf)-len(readme)))
name_padded = name.copy()
name_padded.extend([0]*(len(dataDf)-len(name)))
dataDf["pulls"] = list_of_pulls_padded
dataDf['issues'] = list_of_issues_padded
dataDf['readme'] = readme_padded
dataDf['repository'] = name_padded
print(dataDf)

# this will return a CSV file
dataDf.to_csv(r'C:\Users\uravd\ResearchPaper\react.csv') 