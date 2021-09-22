from os import times
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import mysql.connector 
from devidenumber import devidenumber
import time

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="table"
)


PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://q1-panel.asiatech.ir/admin/SystemStatus/wall/")

username = driver.find_element_by_id("UserUsername")
username.send_keys("m.sekhavat@asiatech.ir")

password = driver.find_element_by_id("UserP")
password.send_keys("MIL@D82525")

password.send_keys(Keys.ENTER)
while(True):
    time.sleep(30)
    vaziatebikar = driver.find_element_by_class_name("tablesorter-header-inner")

    vaziatebikar_value = vaziatebikar.get_attribute('innerHTML')

    
    mycursor = mydb.cursor()

    sql = "INSERT INTO elements (name, value) VALUES (%s, %s)"
    val = ("نفرات بی کار", devidenumber(vaziatebikar_value))
    mycursor.execute(sql, val)
    # vaziatebikar.send_keys(Keys.F5)

    mydb.commit() 
