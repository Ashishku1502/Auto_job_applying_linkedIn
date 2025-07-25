'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

version:    24.12.29.12.30
'''

from modules.helpers import make_directories
from config.settings import run_in_background, stealth_mode, disable_extensions, safe_mode, file_name, failed_file_name, logs_folder_path, generated_resume_path
from config.questions import default_resume_path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from modules.helpers import find_default_profile_directory, critical_error_log, print_lg

try:
    make_directories([
        file_name,
        failed_file_name,
        logs_folder_path+"/screenshots",
        default_resume_path,
        generated_resume_path+"/temp"
    ])

    # Set up WebDriver with Chrome Profile
    options = Options()
    if run_in_background:
        options.add_argument("--headless")
    if disable_extensions:
        options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    print_lg("IF YOU HAVE MORE THAN 10 TABS OPENED, PLEASE CLOSE OR BOOKMARK THEM! Or it's highly likely that application will just open browser and not do anything!")
    if safe_mode:
        print_lg("SAFE MODE: Will login with a guest profile, browsing history will not be saved in the browser!")
    else:
        profile_dir = find_default_profile_directory()
        if profile_dir:
            options.add_argument(f"--user-data-dir={profile_dir}")
        else:
            print_lg("Default profile directory not found. Logging in with a guest profile, Web history will not be saved!")

    # Use webdriver-manager to automatically handle ChromeDriver compatibility
    print_lg("Setting up Chrome with automatic driver management...")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 5)
    actions = ActionChains(driver)
except Exception as e:
    msg = (
        'Seems like either... '\
        '\n\n1. Chrome is already running. '\
        '\nA. Close all Chrome windows and try again. '\
        '\n\n2. Google Chrome or Chromedriver is out dated. '\
        '\nA. Update browser and Chromedriver (You can run "windows-setup.bat" in /setup folder for Windows PC to update Chromedriver)! '\
        '\n\n3. If error occurred when using "stealth_mode", try reinstalling undetected-chromedriver. '\
        '\nA. Open a terminal and use commands "pip uninstall undetected-chromedriver" and "pip install undetected-chromedriver". '\
        '\n\nIf issue persists, try Safe Mode. Set, safe_mode = True in config.py '\
        '\n\nPlease check GitHub discussions/support for solutions https://github.com/GodsScion/Auto_job_applier_linkedIn '\
        '\n                                   OR '\
        '\nReach out in discord ( https://discord.gg/fFp7uUzWCY )'
    )
    if isinstance(e, TimeoutError):
        msg = "Couldn't download Chrome-driver. Set stealth_mode = False in config!"
    print_lg(msg)
    critical_error_log("In Opening Chrome", e)
    try:
        driver.quit()
    except NameError:
        exit()
    
