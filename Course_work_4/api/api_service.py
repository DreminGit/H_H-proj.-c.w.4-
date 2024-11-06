from abc import ABC, abstractmethod
from typing import List
import requests

""""""
class API(ABC):
    @abstractmethod
    def get_vacancies(self, search_query: str) -> List[dict]:
        pass


class HhAPI(API):
    """
    Класс HhAPI дает возможность для взаимодействия с API hh.ru, специально разработанный
    для получения данных о вакансиях.
    """
    BASE_URL = "https://api.hh.ru/vacancies"

    def get_vacancies(self, search_query: str) -> List[dict]:
        """
        Отправляет GET-запрос к API hh.ru для получения списка вакансий
        """
        params = {
            "text": search_query,
            "area": 1,
            "per_page": 100,
            'only_with_salary': True,
        }
        response = requests.get(url=self.BASE_URL, params=params)
        return response.json()['items']

