from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait #ilgili driver ı bekleten bir yapı -beklenen koşullar karşılanana kadar web driverı bekleticez.
from selenium.webdriver.support import expected_conditions #beklenen koşullar
from selenium.webdriver.common .action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.etiya.com")
driver.maximize_window()
#function
def fncGetByX(param1,param2):
    WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((param1,param2)))
    return driver.find_element(param1, param2)

########################################

# Open-Position Button Test 
# 1.https://www.etiya.com sayfası açılır.
# 2.menu tıklanır.
# 3.career tıklanır.
# 4.listeden 'open positions' tıklanır.
# 5.open positions butonu tıklanır. -> Expected Result: Açık pozisyonların ekrana gelmesi beklenir.

menuselector = fncGetByX(By.CLASS_NAME,"menu-title")
menuselector.click()

carierselector = fncGetByX(By.XPATH,"//*[@id='menu-container']/ul/li[7]/a")
carierselector.click()

openpositionselector = fncGetByX(By.XPATH,"//*[@id='etiya']/div[2]/div/div[1]/ul/li[4]/a")
openpositionselector.click()

openPositionBtn = driver.find_element(By.XPATH,"//*[@id='etiya']/div[2]/div/div[2]/div[2]/a")
actionChain = ActionChains(driver)
actionChain.move_to_element(openPositionBtn)
actionChain.click()
actionChain.perform()
openPositionBtn.click() 

sleep(3)

########################################


########################################

# Contact Us Ekranı Send Button Test 
# 1. https://www.etiya.com sayfası açılır.
# 2.'Menu' tıklanır.
# 3.'Contact Us' tıklanır.
# 4. Zorunlu alanlara bilgi girişi yapılır.
# 5. Onay kutusu tıklanır.
# 6. 'Send' Butonu tıklanır.-> Expected Result - Uyarı mesajı açılmalı.

driver.get("https://www.etiya.com")
menuselector = fncGetByX(By.CLASS_NAME,"menu-title")
menuselector.click()

contactselector = fncGetByX(By.XPATH,"//*[@id='menu-container']/ul/li[8]")
contactselector.click()

nameInput = fncGetByX(By.XPATH,"//*[@id='etiya']/div[1]/div[1]/form/div[1]/input")
nameInput.send_keys("Ali")

mailInput = fncGetByX(By.XPATH,"//*[@id='etiya']/div[1]/div[1]/form/div[2]/input")
mailInput.send_keys("ali@etiya.com")

titleInput = fncGetByX(By.XPATH,"//*[@id='etiya']/div[1]/div[1]/form/div[3]/input")
titleInput.send_keys("Ali Company Aş.")

mobileInput = fncGetByX(By.XPATH,"//*[@id='etiya']/div[1]/div[1]/form/div[4]/input")
mobileInput.send_keys("05552226699")

messageInput = fncGetByX(By.XPATH,"//*[@id='etiya']/div[1]/div[1]/form/div[5]/textarea")
messageInput.send_keys("Deneme deneme deneme")

sleep(2)

checkbtn = fncGetByX(By.XPATH,"//*[@id='etiya']/div[1]/div[1]/form/div[8]/label/span")
checkbtn.click()

sendBtn = fncGetByX(By.CLASS_NAME,"btn-send")
sendBtn.click()

sleep(2)

warningdBtn = fncGetByX(By.XPATH,"/html/body/div[5]/div/div[3]/div/button")
warningdBtn.click()

sleep(2)


####################################################


####################################################
# 'Contact Us' Ekranı Email Valid Test
# 1. https://www.etiya.com sayfası açılır.
# 2.'Menu' tıklanır.
# 3.'Contact Us' tıklanır.
# 4. Zorunlu alanlara veri girişi yapılır.
# 5. Email alanına hatalı veri girişi yapılır. ->İnput: ayseqmailcom 
# 6.'Send' Butonu tıklanır.-> Expected Result: 'Please include an '@' and in the email address'  uyarı mesajı açılmalı.


driver.get("https://www.etiya.com")
menuselector = fncGetByX(By.CLASS_NAME,"menu-title")
menuselector.click()

contactselector = fncGetByX(By.XPATH,"//*[@id='menu-container']/ul/li[8]")
contactselector.click()

nameInput = fncGetByX(By.XPATH,"//*[@id='etiya']/div[1]/div[1]/form/div[1]/input")
nameInput.send_keys("Ali")

mailInput = fncGetByX(By.XPATH,"//*[@id='etiya']/div[1]/div[1]/form/div[2]/input")
mailInput.send_keys("ayseqmailcom")

titleInput = fncGetByX(By.XPATH,"//*[@id='etiya']/div[1]/div[1]/form/div[3]/input")
titleInput.send_keys("Ali Company Aş.")

mobileInput = fncGetByX(By.XPATH,"//*[@id='etiya']/div[1]/div[1]/form/div[4]/input")
mobileInput.send_keys("05552226699")

messageInput = fncGetByX(By.XPATH,"//*[@id='etiya']/div[1]/div[1]/form/div[5]/textarea")
messageInput.send_keys("Deneme deneme deneme")

sleep(2)


sendBtn = fncGetByX(By.CLASS_NAME,"btn-send")
sendBtn.click()


sleep(2)

####################################################




####################################################

driver.get("https://www.etiya.com")
button = driver.find_element(By.XPATH,"//*[@id='nval']")
actionChain = ActionChains(driver)
actionChain.move_to_element(button)
actionChain.click()
actionChain.perform()

sleep(3)

## 'let us share' alanı kontrol
## 1.mail alanına 's' girilir.
## 2.search tıklanır.
## 3.ekrana uyarı gelir.


letusshare = driver.find_element(By.CLASS_NAME, "form-control")
letusshare.send_keys("s")
letusclick = driver.find_element(By.ID, "send-newsl")
letusclick.click()
sleep(2)

okbutton = driver.find_element(By.XPATH, "/html/body/div[11]/div/div[3]/div/button")
okbutton.click()

sleep(2)


# let us sahare alanı kontrol
# 1.privicy kutucuğu işaretlenir.
# 2.search tıklanır.
# 3.krana uyarı gelir.

driver.get("https://www.etiya.com")
button = driver.find_element(By.XPATH,"//*[@id='newsletter-form']/div[3]/label/span")
actionChain = ActionChains(driver)
actionChain.move_to_element(button)
actionChain.click()
actionChain.perform()

sleep(2)

letusbutton = driver.find_element(By.XPATH, "//*[@id='newsletter-form']/div[3]/label/span")
letusbutton.click()

sleep(2)

letusclick = driver.find_element(By.ID, "send-newsl")
letusclick.click()

sleep(2)

emailok = driver.find_element(By.XPATH, "/html/body/div[11]/div/div[3]/div/button")
emailok.click()

sleep(2)
#####################################################

sleep(5000)