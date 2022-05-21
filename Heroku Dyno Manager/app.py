from time import sleep
from json import load
from os.path import dirname, realpath

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# # # Functions # # #

def set_dyno(process, state = False):
    # Get the process items #

    items = process.find_element_by_class_name('items-center')

    # Get the process actions #

    actions = items.find_element_by_class_name('actions')
    actions.find_element_by_class_name('actions__edit').click()

    driver.implicitly_wait(0.5)

    # Get the process switch #

    switch = items.find_element_by_class_name('toggle-switch').find_element_by_tag_name('input')

    # Which value should be converted to what Boolean #

    if switch.is_selected() != state:
        switch.click()

    driver.implicitly_wait(0.5)

    actions.find_element_by_class_name('actions__confirm').click()

    sleep(1)

# # # Getting the user login infos # # #

with open(dirname(realpath(__file__)) + '\\json\\arguments.json') as file:
    arguments = load(file)

file.close()

with open(dirname(realpath(__file__)) + '\\json\\login.json') as file:
    data = load(file)

file.close()

del file

email_text = data.get('email')
password_text = data.get('password')

if not email_text:
    email_text = input('Please enter your Heroku E-Mail')
    password_text = data.get('password') or input('Please enter your Heroku password (E-Mail: ' + email_text + '): ')
elif not password_text:
    password_text = data.get('password') or input('Please enter your Heroku password (E-Mail: ' + email_text + '): ')

# Setting up Chrome #

chrome_driver = 'C:\Program Files (x86)\Chrome\chromedriver.exe'

options = Options()
options.headless = True
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# # # Starting the WebDriver # # #

driver = webdriver.Chrome(chrome_driver, options = options)
driver.get('https://heroku.com/login')

# Getting the login elements #

email = driver.find_element_by_id('email')
password = driver.find_element_by_id('password')
login_button = driver.find_element_by_name('commit')

# Sending the login infos #

email.send_keys(email_text)
password.send_keys(password_text)
login_button.click()

try:

    # # Getting the app list # #

    items = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'apps-list-item'))
    )

    selected = None

    while not selected:

        # Printing out the available apps #
        
        if not arguments.get('app_name'):
            for index, item in enumerate(items): 
                print(str(index + 1) + '. ' + item.find_element_by_tag_name('a').get_attribute('href')[34:])

        # Gettings user input for the app that should be selected #

        input_seletor = arguments.get('app_name') or input('\n Please select a project via it\'s index or name: ')

        # Gettings the URL to the app #

        for index, item in enumerate(items):
            try:
                if index == int(input_seletor) - 1:
                    selected = item.find_element_by_tag_name('a').get_attribute('href') + '/resources'
            except ValueError:
                process_name = item.find_element_by_tag_name('a').get_attribute('href')[34:]

                if process_name == input_seletor or process_name.startswith(input_seletor):
                    selected = item.find_element_by_tag_name('a').get_attribute('href') + '/resources'
            except:
                continue
        
        # Retry if invalid #

        if not selected:
            print('Unknown index. Please try again \n')

            arguments['app_name'] = None
            
    # Update URL to app URL #

    driver.get(selected)

    # # Gettings the workers of the app ( Dynos ) # #

    processes = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'process'))
    )

    selected = None
    dynos = []

    # Check if arguments for the workers #

    if arguments.get('workers'):
        for worker in arguments.get('workers'):

            selected = { }

            for index, process in enumerate(processes):

                # Gettings the process details #

                process_name = process.find_elements_by_tag_name('div')[0].find_element_by_tag_name('span').text

                if process_name.startswith(worker.get('name')) and (index + 1 == worker.get('index') or worker.get('index') == -1):
                    dynos.append({
                        'process': process,
                        'state': worker.get('set_to')
                    })

    else:
        while not selected:
            for index, process in enumerate(processes):

                # Gettings the process details #

                process_name = process.find_elements_by_tag_name('div')[0].find_element_by_tag_name('span').text

                print(str(index + 1) + '. ' + process_name)
            
            input_seletor = input('\n Please select a project via it\'s index or name: ')

            # Gettings the process of the worker #

            for index, process in enumerate(processes):
                try:
                    if index == int(input_seletor) - 1:
                        selected = process
                except ValueError:
                    process_name = process.find_elements_by_tag_name('div')[0].find_element_by_tag_name('span').text

                    if process_name == input_seletor or process_name.startswith(input_seletor):
                        selected = process
                except:
                    continue
                    
            # Retry if invalid #

            if not selected:
                print('Unknown index or name. Please try again \n')
        
        # Define what string are what booleans #

        bool_values = {
            True: [
                'True',
                't',
                '1',
                'on',
                'start'
            ],
            False: [
                'False',
                'f',
                '0',
                'off',
                'stop'
            ]
        }

        set_to = False

        while not set_to:
            input_seletor = input('\n Please select a boolean value: ')

            # Getting the seleted boolean #

            for key in bool_values.keys():
                if input_seletor in bool_values[key]:
                    set_to = key
                    
            # Retry if invalid #

            if not selected:
                print('Unknown boolean value. Please try again \n')

        # Generate seleted array #

        dynos.append({
            'process': selected,
            'state': set_to
        })
        

    # Update the dynos #

    for dyno in dynos:
        set_dyno(dyno.get('process'), dyno.get('state'))    

    driver.quit()
except TimeoutException:
    driver.quit()


