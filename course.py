from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By
from section import get_sections_from_selenium


class Course:

    def __init__(self):
        super().__init__()


def get_courses_from_selenium(driver):
    courses = []
    table_rows = driver.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

    for row in table_rows:
        course = Course()

        row_col = row.find_elements(By.TAG_NAME, 'td')

        a_tag = row_col[0].find_element(By.TAG_NAME, 'a')
        course.name = a_tag.text
        course.link = a_tag.get_attribute('href')
        course.subject_code = a_tag.text.split()[0]
        course.number = a_tag.text.split()[1]
        course.title = row_col[1].text

        a_tag.click()
        course.sections = get_sections_from_selenium(driver)
        action = ActionBuilder(driver)
        action.pointer_action.pointer_down(MouseButton.BACK)
        action.pointer_action.pointer_up(MouseButton.BACK)
        action.perform()

        print(f"got data for: {course.name}")

        courses.append(course)

    return courses
