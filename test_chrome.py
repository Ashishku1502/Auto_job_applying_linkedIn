#!/usr/bin/env python3
"""
Simple Chrome test script to verify compatibility
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def test_chrome():
    try:
        print("Testing Chrome compatibility...")
        
        # Set up Chrome options
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        
        # Use webdriver-manager to automatically download and manage ChromeDriver
        service = Service(ChromeDriverManager().install())
        
        # Create driver
        driver = webdriver.Chrome(service=service, options=options)
        
        # Test basic functionality
        driver.get("https://www.google.com")
        print("✅ Chrome test successful! Browser opened and navigated to Google.")
        
        # Close browser
        driver.quit()
        print("✅ Browser closed successfully.")
        
        return True
        
    except Exception as e:
        print(f"❌ Chrome test failed: {e}")
        return False

if __name__ == "__main__":
    test_chrome() 