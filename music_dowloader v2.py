from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as  EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# songs
song_list = []
while True:
    song_name = input('what is the song name ? :')
    q  = input('would you like to add another song (yes,no) ? : ').strip().lower() 
    song_list.append(song_name)
    if q == 'no':
        break 

# chrome options 
chrome_options = ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver,20)

# looping to each song  
for song in song_list:
    try:    
        driver.get(f'https://www.youtube.com/results?search_query={song}')
        time.sleep(2)

        link = driver.find_element(By.XPATH,'//*[@id="video-title"]').get_attribute('href')

        driver.get('https://ytmp3s.nu/6ufl/')
        time.sleep(2)

        input_bar = wait.until(EC.element_to_be_clickable((By.ID,'url')))
        input_bar.clear()
        input_bar.send_keys(link,Keys.ENTER)

        dowlaod = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'Download')))

        q = input(f'would you like to donlaod {song} ? (yes/no) ').strip().lower()

        if q == 'yes':
            dowlaod.click()
            print(f'dowlading {song}...')
            time.sleep(4)
        else:
            print(f'skipping {song}...')    
            
    except (NoSuchElementException, TimeoutException) as e:
        print(f'there was a problem loading {song} and the error was {e}')
        continue
              
time.sleep(100)        