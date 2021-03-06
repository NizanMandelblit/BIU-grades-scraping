import sys
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from tabulate import tabulate

id = input("what is your id?> ")
pwd = getpass("password?> ")

op = webdriver.ChromeOptions()
op.add_argument('headless')
chromedriver = "chromedriver.exe location"
driver = webdriver.Chrome(chromedriver, options=op)
driver.get("https://inbar.biu.ac.il/Live/Login.aspx")

driver.implicitly_wait(1)
driver.find_element_by_name("edtUsername").send_keys(id)
driver.find_element_by_name("edtPassword").send_keys(pwd)
driver.find_element_by_css_selector("#btnLogin").click()
driver.implicitly_wait(1)
driver.find_element_by_css_selector("#tvMainn7").click()
driver.find_element_by_css_selector("#tvMainn7Nodes > table:nth-child(2)").click()
table_id = driver.find_element(By.ID, 'ContentPlaceHolder1_gvGradesList')
rows = table_id.find_elements(By.TAG_NAME, "tr")
for row in rows[1:]:
    td = row.find_elements(By.TAG_NAME, "td")
    if len(td) > 6 and td[6].text != '':
        course =  td[1].text
        grade = td[6].text
        print(tabulate([[course[::-1], grade]], headers=['course', 'grade']))

input("enter to exit ")
sys.exit()
