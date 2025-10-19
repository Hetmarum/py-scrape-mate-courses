import requests
from bs4 import BeautifulSoup, Tag
from dataclasses import dataclass


BASE_URL = "https://mate.academy/"


@dataclass
class Course:
    name: str
    short_description: str
    duration: str


def get_single_course(element: Tag) -> Course:
    name = element.select_one(".ProfessionCard_title__m7uno").text
    short_description = element.select_one(
        ".ProfessionCard_description__K8weo"
    ).text
    duration = element.select_one(".ProfessionCard_duration__13PwX").text
    return Course(
        name=name,
        short_description=short_description,
        duration=duration
    )


def get_all_courses() -> list[Course]:
    courses = []
    url = BASE_URL

    while url:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        for element in soup.select(".ProfessionCard_content__mPiVi"):
            courses.append(get_single_course(element))

        return courses


if __name__ == "__main__":
    courses = get_all_courses()
    for course in courses:
        print(course)
