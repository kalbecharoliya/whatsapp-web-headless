import time
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


message = "This is Line 1./nThis is line 2/nThis is Line 3"


# Specify the user agent for headless browsing
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'

# Specify the path to the ChromeDriver executable
chrome_driver_path = 'C:/PATH/TO/chromedriver.exe'

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('user-agent={0}'.format(user_agent))

# Add any desired options, e.g., headless mode
chrome_options.add_argument('--headless')

# Set the user data directory to store the session data
user_data_dir = 'C:/PATH/TO/DIRECTORY'  # Replace with the desired user data directory
chrome_options.add_argument(f'--user-data-dir={user_data_dir}')
chrome_options.add_argument("--window-size=1920x1080")

# Set up the Chrome service
service = Service(chrome_driver_path)

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open web.whatsapp.com
driver.get('https://web.whatsapp.com/YOUR_WHATSAPPGROUP') #Copy the ID from sharing whatsapp link.

# Save the session data for future use
session_data = {
    'user_data_dir': user_data_dir
}
session_file = 'C:/PATH/TO/DIRECTORY/session.pkl'  # Replace with the desired path for the session data file
with open(session_file, 'wb') as file:
    pickle.dump(session_data, file)

# Wait for the user to scan the QR code manually
input("Press Enter after scanning the QR code")

#Time delay to open Whatsapp web.
time.sleep(15)

#Inspect element and check for the Xpath of Whatsapp web Chat box - Replace the Path with //*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p
chat_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
time.sleep(3)

# Split the message into lines
#If you do not split then it will send lines from chat box instead of whole message.
lines = message.split("\n")

# Type each line followed by the Ctrl+Enter key combination
for line in lines:
    chat_box.send_keys(line)
    chat_box.send_keys(Keys.CONTROL, Keys.ENTER)
    time.sleep(0.5)  # Adjust the delay between lines as needed

# Send the message
chat_box.send_keys(Keys.ENTER)

#driver.save_screenshot("image.png")
print("The Message has been sent to WhatsApp Group")
