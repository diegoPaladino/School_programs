#SETRANSP_AUTO_BOT
#This bot has access of Gemul(the school County plataform), save the document and after that sends to specific email

#importing the libs
import pyautogui as p
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import winsound

#searching the executable of selenium webdriver
#chromedriver='C://CHROMEDRIVER//chromedriver.exe'
driver=webdriver.Chrome()

#requesting the opening of a page
driver.get('http://www.gemul.com.br/')
driver.set_window_position(166,-700)
driver.maximize_window()

#clicking in the "LOGIN" botton
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/ul/li[2]/a/img').click()
driver.find_element_by_xpath('//*[@id="frm"]/div/p/strong[3]/a').click()

