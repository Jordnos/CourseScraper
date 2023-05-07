from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Section:

    def __init__(self):
        super().__init__()


def get_sections_from_selenium(driver):
    sections = []
    table_rows = driver.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

    for row in table_rows:
        section = Section()

        row_col = row.find_elements(By.TAG_NAME, 'td')
        try:
            a_tag = row_col[1].find_element(By.TAG_NAME, 'a')
            section.section = a_tag.text
            section.subject_code = section.section.split()[0]
            section.course_number = section.section.split()[1]
            section.section_number = section.section.split()[2]
            section.link = a_tag.get_attribute('href')
        except NoSuchElementException:
            section.section = sections[-1].section
            section.subject_code = sections[-1].subject_code
            section.course_number = sections[-1].course_number
            section.section_number = sections[-1].section_number
            section.link = sections[-1].link

        section.activity = row_col[2].text
        section.delivery_mode = row_col[3].text
        section.term = row_col[4].text
        section.interval = row_col[5].text
        section.days = row_col[6].text
        section.start = row_col[7].text
        section.end = row_col[8].text

        print(f"got data for: {section.section}")

        sections.append(section)

    return sections
