# Initialize & configure selenium chromedriver
# Add chrome options



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def setup_driver():
    
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--headless")
    
    
    # Launch driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    if driver:
        print("<---- LAUNCHED CHROMEDRIVER SUCCESSFULLY ---->")
    else:
        print("UNABLE TO LAUNCH CHROMEDRIVER")
        