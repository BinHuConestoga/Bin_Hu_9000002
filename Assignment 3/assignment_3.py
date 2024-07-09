# Importing required libraries

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Edge()

# Navigating to the youtube homepage
driver.get("https://www.youtube.com/")
time.sleep(5)

# Finding the search bar and entering text "Music"
search_bar = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
search_bar.send_keys("Music")
search_bar.send_keys(Keys.RETURN)
time.sleep(5)

# Verifying that the search results page has loaded
assert "Music" in driver.title

# Finding the Videos filter on the top and click it
videos_filter = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/div/ytd-search-header-renderer/div[1]/yt-chip-cloud-renderer/div/div[2]/iron-selector/yt-chip-cloud-chip-renderer[3]/yt-formatted-string")
videos_filter.click()
time.sleep(3)

# Finding the Videos filter on the top and click it
first_video = driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-image/img")
first_video.click()
time.sleep(5)

# Giving thumbs-up for this video
click_thumbs_up = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/div/ytd-subscribe-button-renderer/yt-smartimation/div/__slot-el/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
click_thumbs_up.click()
time.sleep(3)

# Viewing the youtuber's page
view_youtuber = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/div[1]/ytd-channel-name/div/div/yt-formatted-string/a")
view_youtuber.click()
time.sleep(5)

# Clicking "YouTuBe CA" logo on the left top of the page
youtube_logo = driver.find_element("id", "logo-icon")
youtube_logo.click()
time.sleep(5)

# Clicking "Shorts" on the left manu
click_home = driver.find_element(By.LINK_TEXT, "Shorts")
click_home.click()
time.sleep(5)

# Closing the webdriver
driver.close()
