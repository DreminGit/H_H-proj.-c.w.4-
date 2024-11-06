from typing import List
from models.vacancy import Vacancy
from storage.json_storage import JSONVacancyStorage


def filter_vac_salary(vacancies: List[Vacancy], desired_salary: int) -> List[Vacancy]:
    """
    Функция, которая сортирует  спискок экземпляров Vacancy
    """
    filtered_vacancies = []

    for vac in vacancies:

        if vac.salary_from is not None and vac.salary_to is not None:
            if vac.salary_from <= desired_salary <= vac.salary_to:
                filtered_vacancies.append(vac)

        elif vac.salary_from is not None:
            if vac.salary_from <= desired_salary <= vac.salary_from + 10000:
                filtered_vacancies.append(vac)

        elif vac.salary_to is not None:
            if vac.salary_to - 10000 <= desired_salary <= vac.salary_to:
                filtered_vacancies.append(vac)

    return filtered_vacancies


def sort_vac_for_salary(data: List[Vacancy]) -> List[Vacancy]:
    """Функция сортировки для вакансий по убыванию"""
    return sorted(data, reverse=True)


def top_sort_vac(data: List[Vacancy], top_n: int) -> List[Vacancy]:
    """Функция возвращает 5 первых элементов вакансий"""
    return data[:top_n]


def print_vac(data: List[Vacancy]) -> None:
    """Функция печатает найденные вакансии"""
    for vac in data:
        print(vac)
    print(f'\nНайдены {len(data)} вакансии\n')


def overwrite_file(json_storage: JSONVacancyStorage, data: List[Vacancy]) -> None:
    """Функция, которая записывает вакансии в файл"""
    user_choice = input('Сохранить в файле только полученные вакансии? (Д/Н)  ').lower()
    if user_choice == 'д':
        json_storage.add_vacancies(data)
