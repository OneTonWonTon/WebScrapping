import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

service = Service()
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)

driver.get('https://oxylabs.io/blog/dedicated-datacenter-proxies-self-service')


results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
driver.quit()

for a in soup.findAll(class_='e1premmp0 css-1462j37 e115oe510'):
    name = a.find('h2')
    if name not in results:
        results.append(name.text)

for b in soup.findAll(class_='e1premmp0 css-1462j37 e115oe510'):
    date = b.find('p')
    if date not in results:
        other_results.append(date.text)

print(name)
print(date)
df = pd.DataFrame({'Names': results, 'Dates': other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')
