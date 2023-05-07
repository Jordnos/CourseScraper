from selenium import webdriver
from course import get_courses_from_selenium
from subject import get_subjects_from_selenium
# import config
# import random
import urllib.parse
import jsonpickle


# def rand_proxy():
#     proxy = random.choice(config.ips)
#     return proxy


def format_url(session="", subject_code="", course_number="", pname="subjarea", tname=""):
    root = "https://courses.students.ubc.ca/cs/courseschedule?"

    if session != "":
        sessyr = session.split()[0]
        sesscd = session.split()[1][0]
    else:
        return root

    if subject_code != "":
        tname = "subj-department"

    if course_number != "":
        tname = "subj-course"

    params = {
        "sessyr": sessyr,
        "sesscd": sesscd,
        "pname": pname,
        "tname": tname,
        "dept": subject_code,
        "course": course_number,
    }

    return root + urllib.parse.urlencode(params)


def get_selenium_driver_for_url(url):
    chrome_options = webdriver.ChromeOptions()
    # proxy = rand_proxy()
    # chrome_options.add_argument(f'--proxy-server={proxy}')
    chrome_options.add_argument('--headless=new')
    chrome_options.page_load_strategy = 'eager'
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    return driver


def save_session_to_file(session, session_subjects):
    print(f"saving to file ...")
    file_name = f"./data/{session}.json"
    f = open(file_name, 'w')
    json_data = jsonpickle.encode(session_subjects, unpicklable=False)
    print("data encoded?")
    f.write(json_data)
    print(f"saved to {file_name}!")


def scrape():
    session = input(f"enter session to scrape (eg. '2023 Summer') (session must be capitalized):")
    url = format_url(session)
    driver = get_selenium_driver_for_url(url)
    subjects = get_subjects_from_selenium(driver)
    driver.quit()

    for subject in subjects:
        if subject.link is None:
            continue
        url = format_url(session, subject.code)
        driver = get_selenium_driver_for_url(url)
        subject.courses = get_courses_from_selenium(driver)
        driver.quit()

    save_session_to_file(session, subjects)


if __name__ == '__main__':
    scrape()
