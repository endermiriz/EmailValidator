import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
options.add_argument("--headless") # Required for Firefox to run headless. But if you don't run headless, the project gets faster.
geckodriver = 'geckodriver.exe' # Don't forget to add the 'geckodriver.exe' file to your project for your Selenium package to work.
profile = webdriver.Firefox(options=options)
extension_dir = 'C:\\Users\\Your Windows User Name\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\5k9n92gt.default-release\\extensions\\' # Enter your Firefox extensions location here.
extensions = ['browsec@browsec.com.xpi'] # Don't forget to add the browserc vpn xpi file into your project.
for extension in extensions:
    profile.install_addon(extension_dir + extension, temporary=True) # This loop allows firefox to add extensions every time I run the project.

profile.get('about:debugging#/runtime/this-firefox') # It's the way we go in firefox to find the extension's popup.html.
wait = WebDriverWait(profile, 60)
htmlbulma = wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div/div/main/article/section[1]/div/ul/li/section[1]/dl/div[4]/dd/a")))# This is the section that is used to get the extension's manifest link.
giris = htmlbulma.text.removesuffix('manifest.json') # It helps to delete the manifest.json part from the link we found.
popup ="popup/popup.html" # It serves to convert the manifest link we found into the extension's popup link.
popupgiris = giris+popup # Combines popup and link.
profile.get(popupgiris)
time.sleep(0.2)
vpnac = profile.execute_script('return document.querySelector("body > div > page-switch").shadowRoot.querySelector("div > main-index").shadowRoot.querySelector("div.Switch > index-home").shadowRoot.querySelector("div.In.transition > div > div.Inactive > div.Inactive_ButtonOut > div")').click()
# The top section is used to activate the vpn from the popup of our vpn extension.
print("Proxy on")

profile.get('https://validateemailaddress.org/')
print('Enter Email:')
Email = input()
emaillist = [Email] # You can edit existing codes and list them to check multiple emails.

profile.refresh()

for email in emaillist:
    giris = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form"]/input[1]'))).send_keys(email)
    tikla = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="form"]/input[2]'))).click()

    try:
        varvalid = profile.find_element(By.XPATH, '//*[@class="success valid"]')
        arama = profile.find_element(By.XPATH, '//*[@id="middle"]/div/table/tbody/tr[2]/td')
        print(email,'Valid')
        profile.find_element(By.XPATH, '//*[@id="form"]/input[1]').clear()
    except NoSuchElementException:
        print(email,'NoValid')
        profile.find_element(By.XPATH, '//*[@id="form"]/input[1]').clear()
profile.quit()


