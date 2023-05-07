from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Subject:

    def __init__(self):
        super().__init__()


def get_subjects_from_selenium(driver):
    subjects = []
    table_rows = driver.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

    for row in table_rows:
        subject = Subject()

        row_cols = row.find_elements(By.TAG_NAME, 'td')

        subject.title = row_cols[1].text
        subject.faculty = row_cols[2].text
        print(f"{subject.title}:{subject.faculty}\n")
        try:
            a_tag = row_cols[0].find_element(By.TAG_NAME, 'a')
            subject.code = a_tag.text
            subject.link = a_tag.get_attribute('href')
        except NoSuchElementException:
            subject.code = row_cols[0].find_element(By.TAG_NAME, 'b').text.split()[0]
            subject.link = None

        subjects.append(subject)

    return subjects
