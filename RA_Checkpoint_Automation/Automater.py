import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def findAllRatingDropdowns(driver):
    selects = driver.find_elements(By.CSS_SELECTOR, "select")
    ratingsDropdowns = []
    for i in range(len(selects)):
        selectOptions = selects[i].find_elements(By.CSS_SELECTOR, "option")
        if len(selectOptions) == 5:
            ratingsDropdowns.append(selects[i])
    
    # print(str(len(ratingsDropdowns)) + " ratings drowndowns detected")
    return ratingsDropdowns

def fillOutForm(driver, residentName):
    driver.get("https://buffalo.erezlife.com/app/one.php?manager=FormView&form_type_id=64")
    WebDriverWait(driver, timeout=300).until(
        EC.presence_of_element_located((By.ID, "gensec_form_date_from"))
    )

    datePicker = driver.find_element(by=By.ID, value="gensec_form_date_from")
    datePicker.send_keys("10/12/2025")

    hallPicker = driver.find_element(by=By.ID, value="answers[gensec][location]-1755")
    hallPicker.click()

    paraproSelector = driver.find_element(By.CSS_SELECTOR, "option[value='7543']")
    paraproSelector.click()

    residentSearch = driver.find_element(By.CSS_SELECTOR, "div.student-select-search-bar input")
    residentSearch.click()

    residentSearch.send_keys(residentName)
    time.sleep(1)
    residentOption = driver.find_elements(By.CSS_SELECTOR, "button.student-select-search-result")[0]
    residentOption.click()

    ratingsDropdowns = findAllRatingDropdowns(driver)
    for dropdown in ratingsDropdowns:
        randVal = random.random()
        randInt = 4
        if (randVal < 0.15):
            randInt = 2
        elif (randVal < 0.5):
            randInt = 3
        else:
            randInt = 4
        
        ratingOption = dropdown.find_elements(By.XPATH, f".//option[text()='{str(randInt)}']")
        # print(ratingOption)
        ratingOption = ratingOption[0]
        ratingOption.click()
        time.sleep(0.1 + random.random() * 0.1)
    

    themes = {
        "Academic Struggles": 0.1,
        "Class attendance": 0.05,
        "GPA / Grades": 0.1,
        "Major": 0.2,
        "Organization Skills": 0.1,
        "Study Habits": 0.1,
        "Homesickness": 0.05,
        "Making friends": 0.05,
        "Transition": 0.2,
        "Romantic Relationships": 0.05,
        "Roommate Experience": 1.0,
        "Fitness": 0.1,
        "Sleep": 0.1,
        "Work / Employment": 0.05,
        "Time Management": 0.1
    }

    resources = {
        "Instructor Office Hours": 0.1,
        "Clubs & Organizations": 0.4,
        "Financial Aid": 0.15,
        "Academic Advising": 0.2,
        "TASS (Tutoring)": 0.3,
        "Math Center": 0.15
    }

    for theme in themes.keys():
        randVal = random.random()
        if (randVal < themes[theme]):
            label = driver.find_elements(By.XPATH, f"//label[text()='{theme}']")[0]
            parent = label.find_element(By.XPATH, "..")
            inputBox = parent.find_elements(By.CSS_SELECTOR, "input")[0]
            inputBox.click()
            time.sleep(random.random() * 0.5)
    
    for resource in resources.keys():
        randVal = random.random()
        # print(resource)
        if (randVal < resources[resource]):
            print("Selecting resource..")
            if (random.random() < 0.4):
                label = driver.find_elements(By.XPATH, f"//label[text()='{resource}']")[0]
            else:
                label = driver.find_elements(By.XPATH, f"//label[text()='{resource}']")[1]
            parent = label.find_element(By.XPATH, "..")
            inputBox = parent.find_elements(By.CSS_SELECTOR, "input")[0]
            inputBox.click()
            time.sleep(random.random() * 0.5)

    time.sleep(1)
    submitButton = driver.find_element(By.ID, value="submit_form")
    submitButton.click()

    time.sleep(3)
    return True

def main():
    options = Options()
    options.debugger_address = "localhost:9222"
    driver = webdriver.Chrome(options=options)

    with open("Residents.txt", "r") as residentList:
        for resident in residentList:
            print("Filling out the form for " + resident[resident.find(",") + 1::])
            fillOutForm(driver, resident.strip())



if __name__ == "__main__":
    main()
