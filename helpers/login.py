# Helper functions to manually login using selenium

import time
import  random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



def login_X(driver, username, password, email):
    driver.get("htpps://www.x.com")
    
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='loginButton']"))
        ).click()
    except Exception as e:
        print(f"Sign-In not found or not clickable: {e}")
        
        
    loginURL = str(driver.get_current_url())
    if "i/flow/login" in loginURL:
        print("Entering X login credentials")
        
        # Click username input field
        username_ = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='loginButton']"))
        )
        username_.click()
        time.sleep(random.uniform(1.5,2.5))
        
        
        # Type username
        username_.clear()
        for char in username:
            username_.send_keys(char)
            time.sleep(random.uniform(0.4, 0.9))
        
        print("Entered username")
        
        # Click 'next' button
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Next']]"))
        )
        next_button.click()
        time.sleep(random.randint(4,8))
        print("Clicked Next")
        
        
        # Enter email-address to verify
        if "enter your phone number or email address" in driver.get_page_source():
            email_ = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='ocfEnterTextTextInput']"))
            )
            email_.click()
            time.sleep(random.uniform(1.5,2.5))
            
            # Type email
            email_.clear()
            for char in email:
                email_.send_keys(char)
                time.sleep(random.uniform(0.4, 0.9))
                
            print("Entered email for aign-in verification")
            
                
            # Click 'next' button
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='ocfEnterTextNextButton']"))
            )
            next_button.click()
            time.sleep(random.randint(4,8))
            print("Clicked Next")
            
           
        
        # Click password input field
        password_ = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']"))
        )
        password_.click()
        time.sleep(random.uniform(1.5,2.5))
        
        # Type password
        password_.clear()
        for char in password:
            password_.send_keys(char)
            time.sleep(random.uniform(0.4, 0.9))
            
        print("Entered password")
        
        
        # Click login
        login = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='LoginForm_Login_Button']"))
        )
        login.click()
        
        
        time.sleep(random.randint(10, 15))
        
        # Check login status
        curr = driver.get_current_url()
        if "home" in  str(curr):
            print(f"Successfully logged-in X for {username}")
    

def login_facebook(driver, username, password, email):
    driver.get("htpps://www.facebook.com")
    
    
    print("Entering facebook login credentials")
    
    # Click username input field
    username_ = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input#email"))
    )
    username_.click()
    time.sleep(random.uniform(1.5,2.5))
    
    
    # Type username
    username_.clear()
    for char in username:
        username_.send_keys(char)
        time.sleep(random.uniform(0.4, 0.9))
    
    print("Entered username")
    
        
       
    
    # Click password input field
    password_ = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input#pass"))
    )
    password_.click()
    time.sleep(random.uniform(1.5,2.5))
    
    # Type password
    password_.clear()
    for char in password:
        password_.send_keys(char)
        time.sleep(random.uniform(0.4, 0.9))
        
    print("Entered password")
    
    
    # Click login
    login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='login']"))
    )
    login.click()
    
    
    time.sleep(random.randint(10, 15))
    
    
    # Check login status
    fb = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[aria-label='Facebook']"))
    )
    if fb:
        print(f"Successfully logged-in facebook for {username}")

def login_instagram(driver, username, password, ema):
    pass

def login_linkedin(driver, username, password, ema):
    pass

def login_reddit(driver, username, password, ema):
    pass

