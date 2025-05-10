# Random manual actions scripts to carry out in social-media web automated scraping to mature accounts
# Mimics human-like actions
# Avoids accounts/sessions being flagged as bots
# May not be undetectable as such


# Possible actions
'''
# ------ Low ------
1. Scrolling upwards/downwards
2. Viewport sizing


# ------ Medium ------
1. Clicking post interactions buttons (like, repost, , follow/unfollow)
2. Clicking and navigating on random posts's sources (user profile, scrolloing post's comments)
3. Typing in input fields with delays between each character 
4. Mouse hover


# ------ High ------
1. React to post (comments, replies to comments)
2. Sending DMs to connections
3. Login differeny geolocations using proxies
4. Interact with notifications

'''


import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def twitter_actions(driver):
    
    
    # Scroll
    for _ in range(random.randint(5,20)):
        driver.execute_script(f"window.scrollTo(0, {random.randint(300, 1800)});")
        time.sleep(random.uniform(3.5, 5.5))
        
        if random.randint(0,1)==1:
            #like a post
            try:
                like = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "a[like]"))
                )
                like.click()
            except Exception as e:
                print(f"Unable to like a post: {e}")
            
        if random.randint(0,1)==1:
            #bookmark a post
            try:
                save = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "a[bookmark]"))
                )
                save.click()
            except Exception as e:
                print(f"Unable to bookmark a post: {e}")
            
        if random.randint(0,1)==1:
            #repost a post
            try:
                repost = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "a[repost]"))
                )
                repost.click()
            except Exception as e:
                print(f"Unable to like a post: {e}")
                
                
    if random.randint(0,1)==1:
        # Click a sidebar
        
        sections = ["Messages", "Notifications", "Explore", "Account"]
        section = random.choice(sections)
        
        try:
            sidebar = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"a[{section}]"))
            )
            sidebar.click()
        except Exception as e:
            print(f"Unable to click sidebar: {e}")
            
        for _ in range(random.randint(3,9)):
            driver.execute_script(f"window.scrollTo(0, {random.randint(700, 900)});")
            time.sleep(random.uniform(1.5, 2.5))
        
        
            
        


def facebook_actions(driver):
    pass


def instagram_actions(driver):
    pass



def reddit_actions(driver):
    pass



def linkedin_actions(driver):
    pass



def twitter_actions(driver):
    pass



def twitter_actions(driver):
    pass



def threads_actions(driver):
    pass



def tumblr_actions(driver):
    pass



def pinterest_actions(driver):
    pass



def quora_actions(driver):
    pass



def youtube_actions(driver):
    pass




