import numpy as np

MAX_PEDAGOG_LOAD_WEEK_IN_HOURS = 50
MAX_HOURS_IN_WEEK = {
    1: 21,
    2: 23,
    3: 23,
    4: 23,
    5: 29,
    6: 30,
    7: 32,
    8: 33,
    9: 36,
    10: 37,
    11: 37
}

MAX_HOURS_IN_WEEK_FIVE = {
    1: 21,
    2: 23,
    3: 23,
    4: 23,
    5: 29,
    6: 30,
    7: 32,
    8: 33,
    9: 33,
    10: 34,
    11: 34
}

MAX_HOURS_IN_WEEK_SIX = {
    1: 0,
    2: 26,
    3: 26,
    4: 26,
    5: 32,
    6: 33,
    7: 35,
    8: 36,
    9: 36,
    10: 37,
    11: 37
}

WEIGHT_DISCIPLINES = {
    1: {
        "Математика": 8,
        "Русский язык": 7,
        "Родной язык": 7,
        "Иностранный язык": 7,
        "Окружающий мир": 6,
        "Природоведение": 6,
        "Информатика": 6,
        "Литература": 5,
        "История": 4,
        "ИЗО": 3,
        "Музыка": 3,
        "Технология": 2,
        "Физическая культура": 1
    },
    2: {
        "Математика": 8,
        "Русский язык": 7,
        "Родной язык": 7,
        "Иностранный язык": 7,
        "Окружающий мир": 6,
        "Природоведение": 6,
        "Информатика": 6,
        "Литература": 5,
        "История": 4,
        "ИЗО": 3,
        "Музыка": 3,
        "Технология": 2,
        "Физическая культура": 1
    },
    3: {
        "Математика": 8,
        "Русский язык": 7,
        "Родной язык": 7,
        "Иностранный язык": 7,
        "Окружающий мир": 6,
        "Природоведение": 6,
        "Информатика": 6,
        "Литература": 5,
        "История": 4,
        "ИЗО": 3,
        "Музыка": 3,
        "Технология": 2,
        "Физическая культура": 1
    },
    4: {
        "Математика": 8,
        "Русский язык": 7,
        "Родной язык": 7,
        "Иностранный язык": 7,
        "Окружающий мир": 6,
        "Природоведение": 6,
        "Информатика": 6,
        "Литература": 5,
        "История": 4,
        "ИЗО": 3,
        "Музыка": 3,
        "Технология": 2,
        "Физическая культура": 1
    },
    5: {
        "Биология": 10,
        "Математика": 10,
        "Иностранный язык": 9,
        "Иностранный язык (гр1)": 9,
        "Иностранный язык (гр2)": 9,
        "Русский язык": 8,
        "Краеведение": 7,
        "География": 7,
        "Природоведение": 6,
        "Информатика": 4,
        "Литература": 4,
        "История": 5,
        "Обществознание": 5,
        "ИЗО": 3,
        "Музыка": 2,
        "Технология": 4,
        "Технология (дев)": 4,
        "Технология (мал)": 4,
        "Физическая культура": 3
    },
    6: {
        "Биология": 8,
        "Математика": 13,
        "Иностранный язык": 11,
        "Иностранный язык (гр1)": 11,
        "Иностранный язык (гр2)": 11,
        "Русский язык": 12,
        "Краеведение": 9,
        "География": 7,
        "Природоведение": 8,
        "Информатика": 10,
        "Литература": 6,
        "История": 8,
        "Обществознание": 9,
        "ИЗО": 3,
        "Музыка": 1,
        "Технология": 3,
        "Технология (дев)": 3,
        "Технология (мал)": 3,
        "Физическая культура": 4
    },
    7: {
        "Биология": 7,
        "Химия": 13,
        "Геометрия": 13,
        "Алгебра": 10,
        "Физика": 8,
        "Иностранный язык": 10,
        "Иностранный язык (гр1)": 10,
        "Иностранный язык (гр2)": 10,
        "Русский язык": 11,
        "Краеведение": 5,
        "География": 6,
        "Обществознание": 9,
        "История": 6,
        "Технология": 2,
        "Технология (дев)": 2,
        "Технология (мал)": 2,
        "Литература": 4,
        "ИЗО": 1,
        "Физическая культура": 2,
        "Музыка": 1,
        "Информатика": 4,
        "Информатика (гр1)": 4,
        "Информатика (гр2)": 4
    },
    8: {
        "Химия": 10,
        "Геометрия": 10,
        "Физика": 9,
        "Алгебра": 9,
        "Черчение": 5,
        "Биология": 7,
        "Иностранный язык": 8,
        "Иностранный язык (гр1)": 8,
        "Иностранный язык (гр2)": 8,
        "Русский язык": 7,
        "Краеведение": 5,
        "География": 6,
        "Обществознание": 5,
        "История": 8,
        "Технология": 1,
        "Технология (дев)": 1,
        "Технология (мал)": 1,
        "Литература": 4,
        "ИЗО": 3,
        "Физическая культура": 2,
        "Музыка": 1,
        "Информатика": 7,
        "Информатика (гр1)": 7,
        "Информатика (гр2)": 7,
        "ОБЖ": 3
    },
    9: {
        "Химия": 12,
        "Геометрия": 8,
        "Физика": 13,
        "Алгебра": 7,
        "Черчение": 4,
        "Биология": 7,
        "Иностранный язык": 9,
        "Иностранный язык (гр1)": 9,
        "Иностранный язык (гр2)": 9,
        "Русский язык": 6,
        "Краеведение": 5,
        "География": 5,
        "Обществознание": 5,
        "История": 10,
        "Технология": 4,
        "Технология (дев)": 4,
        "Технология (мал)": 4,
        "Литература": 7,
        "ИЗО": 3,
        "Физическая культура": 2,
        "Музыка": 1,
        "Информатика": 7,
        "Информатика (гр1)": 7,
        "Информатика (гр2)": 7,
        "ОБЖ": 3
    },
    10: {
        "Химия": 11,
        "Геометрия": 11,
        "Физика": 12,
        "Алгебра": 10,
        "Черчение": 5,
        "Биология": 7,
        "Иностранный язык": 8,
        "Иностранный язык (гр1)": 8,
        "Иностранный язык (гр2)": 8,
        "Русский язык": 9,
        "Астрономия": 4,
        "География": 3,
        "Обществознание": 5,
        "История": 5,
        "Технология": 1,
        "Технология (дев)": 1,
        "Технология (мал)": 1,
        "Литература": 8,
        "ИЗО": 3,
        "Физическая культура": 1,
        "Музыка": 1,
        "Информатика": 6,
        "Информатика (гр1)": 6,
        "Информатика (гр2)": 6,
        "ОБЖ": 2
    },
    11: {
        "Химия": 11,
        "Геометрия": 11,
        "Физика": 12,
        "Алгебра": 10,
        "Черчение": 5,
        "Биология": 7,
        "Иностранный язык": 8,
        "Иностранный язык (гр1)": 8,
        "Иностранный язык (гр2)": 8,
        "Русский язык": 9,
        "Астрономия": 4,
        "География": 3,
        "Обществознание": 5,
        "История": 5,
        "Технология": 1,
        "Технология (дев)": 1,
        "Технология (мал)": 1,
        "Литература": 8,
        "ИЗО": 3,
        "Физическая культура": 1,
        "Музыка": 1,
        "Информатика": 6,
        "Информатика (гр1)": 6,
        "Информатика (гр2)": 6,
        "ОБЖ": 2
    }
}

TYPE_DISCIPLINES = {

    "Русский язык": "Филология",
    "Литература": "Филология",
    "Иностранный язык": "Филология",
    "Иностранный язык (гр1)": "Филология",
    "Иностранный язык (гр2)": "Филология",

    "Математика": "Точные",
    "Алгебра": "Точные",
    "Геометрия": "Точные",
    "Информатика": "Точные",
    "Информатика (гр1)": "Точные",
    "Информатика (гр2)": "Точные",

    "История": "Общественнонаучные",
    "Обществознание": "Общественнонаучные",
    "География": "Общественнонаучные",
    "Окружающий мир": "Общественнонаучные",

    "Биология": "Естественнонаучные",
    "Физика": "Естественнонаучные",
    "Химия": "Естественнонаучные",
    "Астрономия": "Естественнонаучные",

    "ИЗО": "Искусство",
    "Музыка": "Искусство",
    "МХК": "Искусство",
    "ОРКиСЭ": "Искусство",

    "Технология": "Технология",
    "Технология (дев)": "Технология",
    "Технология (мал)": "Технология",
    "Черчение": "Технология",

    "Физкультура": "Физкультура",
    "Физкультура (дев)": "Физкультура",
    "Физкультура (мал)": "Физкультура",
    "ОБЖ": "Физкультура"
}

RUSSIAN_ALPHABET = np.array(["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С",
                             "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "ь", "Э", "Ю", "Я"])
