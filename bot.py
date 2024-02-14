import telebot
from telebot import types
import random

bot = telebot.TeleBot('6834474544:AAG1JmoAMGyt1diuELK17Zh6ppDOAxqthpc')
anim = open('C:/Users/Anton/YandexDisk/Скриншоты/BestPornhubmoments.mp4', 'rb')
sticker = open('C:/Users/Anton/YandexDisk/Скриншоты/sticker1.webp', 'rb')
start_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_button = types.KeyboardButton("Начать")
start_markup.add(start_button)

topic_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
health_button = types.KeyboardButton("Здоровье")
sports_button = types.KeyboardButton("Спорт")
work_button = types.KeyboardButton("Работа")
entertainment_button = types.KeyboardButton("Развлечения")
topic_markup.row(health_button, sports_button)
topic_markup.row(work_button, entertainment_button)

health_questions = [
    {
        'question': 'Как переводится слово "temperature" на английский?',
        'options': ['Температура', 'Текст', 'Теннис'],
        'correct_option': 0,
    },
    {
        'question': 'Какое из следующих слов означает "боль" на английском?',
        'options': ['Cold', 'Pain', 'Sleep'],
        'correct_option': 1,
    },
    {
        'question': 'Что означает слово "prescription" в медицинском контексте?',
        'options': ['Рецепт (в кулинарии)', 'Приглашение', 'Рецепт (на лекарство)'],
        'correct_option': 2,
    },
    {
        'question': 'Как перевести на английский язык слово "X-ray"?',
        'options': ['Эксперимент', 'Рентген', 'Язва'],
        'correct_option': 1,
    },
    {
        'question': 'Как называется "зубной врач" по-английски?',
        'options': ['Tooth fairy', 'Dentist', 'Doctor Teeth'],
        'correct_option': 1,
    },
]
sport_questions = [
    {
        'question': 'Как называется соревнование по бегу на длинные дистанции на английском языке?',
        'options': ['Sprint', 'Marathon', 'Hurdles'],
        'correct_option': 1,
    },
    {
        'question': 'Что означает слово "goalkeeper" на английском языке?',
        'options': ['Нападающий', 'Вратарь', 'Защитник'],
        'correct_option': 1,
    },
    {
        'question': 'Как переводится слово "score" в контексте спорта?',
        'options': ['Замена', 'Забить', 'Отбор'],
        'correct_option': 1,
    },
    {
        'question': 'Какое слово означает "ракетка" в теннисе по-английски?',
        'options': ['Racket', 'Shuttlecock', 'Paddle'],
        'correct_option': 0,
    },
    {
        'question': 'Что такое "stadium" на английском языке?',
        'options': ['Спорткомплекс', 'Тренажерный зал', 'Стадион'],
        'correct_option': 2,
    },
]
job_questions = [
    {
        'question': 'Что означает слово "deadline" на английском?',
        'options': ['Срок завершения работы', 'Заголовок документа', 'Резюме'],
        'correct_option': 0,
    },
    {
        'question': 'Как переводится слово "promotion"?',
        'options': ['Продвижение', 'Производство', 'Перемещение'],
        'correct_option': 0,
    },
    {
        'question': 'Что такое "colleague" в рабочем контексте?',
        'options': ['Клиент', 'Коллега', 'Конкурент'],
        'correct_option': 1,
    },
    {
        'question': 'Как перевести на английский термин "job interview"?',
        'options': ['Рабочее место', 'Собеседование по работе', 'Профессиональный опыт'],
        'correct_option': 1,
    },
    {
        'question': 'Какое слово означает "занятость" в английском языке?',
        'options': ['Employment', 'Enjoyment', 'Endorsement'],
        'correct_option': 0,
    },
]
entertainment_questions = [
    {
        'question': 'Как переводится слово "entertainment" на английском языке?',
        'options': ['Волнение', 'Развлечение', 'Образование'],
        'correct_option': 1,
    },
    {
        'question': 'Где обычно проходят выступления комиков вживую?',
        'options': ['Художественная галерея', 'Клуб комиков', 'Библиотека'],
        'correct_option': 1,
    },
    {
        'question': 'Что означает термин "blockbuster" в контексте кино?',
        'options': ['Популярный и успешный фильм', 'Мультфильм', 'Фильм с низким бюджетом'],
        'correct_option': 0,
    },
    {
        'question': 'Какая из перечисленных игр часто ассоциируется с тактикой и дипломацией?',
        'options': ['Монополия', 'Скраббл', 'Шахматы'],
        'correct_option': 2,
    },
    {
        'question': 'Какова основная цель "roller coaster" в парке развлечений?',
        'options': ['Обслуживание еды и напитков', 'Предоставление захватывающих аттракционов',
                    'Проведение художественных выставок'],
        'correct_option': 1,
    },
]

# Create a dictionary to keep track of the user's progress for each topic.
user_progress = {}
user_scores = {}


@bot.message_handler(func=lambda message: message.text in ['Здоровье', 'Спорт', 'Работа', 'Развлечения'])
def handle_topic(message):
    user_id = message.from_user.id
    topic = message.text

    # Устанавливаем прогресс пользователя для выбранной темы на 0.
    user_progress[user_id] = {'topic': topic, 'question_index': 0}
    user_scores[user_id] = 0
    bot.send_message(message.chat.id, f'Вы выбрали тему: {topic}')

    if topic == "Здоровье":
        # Перемешиваем health_questions, чтобы представить их случайным образом.
        random.shuffle(health_questions)
        send_next_question(user_id, message.chat.id)
    elif topic == "Спорт":
        random.shuffle(sport_questions)
        send_next_question(user_id, message.chat.id)
    elif topic == "Работа":
        random.shuffle(job_questions)
        send_next_question(user_id, message.chat.id)
    elif topic == "Развлечения":
        random.shuffle(entertainment_questions)
        send_next_question(user_id, message.chat.id)


def send_next_question(user_id, chat_id):
    user_data = user_progress.get(user_id)
    if user_data:
        topic = user_data['topic']
        question_index = user_data['question_index']

        if topic == "Здоровье" and question_index < len(health_questions):
            question = health_questions[question_index]
            bot.send_message(chat_id, question['question'])
            options = question['options']
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for option in options:
                markup.add(types.KeyboardButton(option))

            bot.send_message(chat_id, "Выберите вариант ответа:", reply_markup=markup)

        elif topic == "Спорт" and question_index < len(sport_questions):
            question = sport_questions[question_index]
            bot.send_message(chat_id, question['question'])
            options = question['options']
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for option in options:
                markup.add(types.KeyboardButton(option))

            bot.send_message(chat_id, "Выберите вариант ответа:", reply_markup=markup)
        # Добавьте аналогичные условия для других тем (Работа и Развлечения)
        elif topic == "Работа" and question_index < len(job_questions):
            question = job_questions[question_index]
            bot.send_message(chat_id, question['question'])
            options = question['options']
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for option in options:
                markup.add(types.KeyboardButton(option))

            bot.send_message(chat_id, "Выберите вариант ответа:", reply_markup=markup)

        elif topic == "Развлечения" and question_index < len(entertainment_questions):
            question = entertainment_questions[question_index]
            bot.send_message(chat_id, question['question'])
            options = question['options']
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for option in options:
                markup.add(types.KeyboardButton(option))

            bot.send_message(chat_id, "Выберите вариант ответа:", reply_markup=markup)

        else:
            display_results(user_id, chat_id)
            # Добавляем кнопку для возврата к выбору тем после завершения вопросов.
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(types.KeyboardButton("Вернуться к темам"))
            bot.send_message(chat_id, "Вы ответили на все вопросы в данной теме.", reply_markup=markup)
    else:
        bot.send_message(chat_id, "Произошла ошибка. Пожалуйста, выберите тему снова.")


@bot.message_handler(
    func=lambda message: message.text in ['Температура', 'Текст', 'Теннис', 'Cold', 'Pain', 'Sleep', 'Рецепт (в кулинарии)', 'Приглашение', 'Рецепт (на лекарство)', 'Эксперимент',
                                          'Рентген', 'Язва', 'Tooth fairy', 'Dentist', 'Doctor Teeth', 'Sprint', 'Marathon', 'Hurdles', 'Нападающий', 'Вратарь', 'Защитник', 'Замена', 'Забить',
                                          'Отбор', 'Racket', 'Shuttlecock', 'Paddle', 'Спорткомплекс', 'Тренажерный зал', 'Стадион', 'Football/soccer', 'Basketball', 'Tennis', 'Срок завершения работы',
                                          'Заголовок документа', 'Резюме', 'Продвижение', 'Производство', 'Перемещение', 'Клиент', 'Коллега', 'Конкурент', 'Рабочее место', 'Собеседование по работе',
                                          'Профессиональный опыт', 'Employment', 'Enjoyment', 'Endorsement', 'Волнение',
                                          'Развлечение', 'Образование', 'Художественная галерея', 'Клуб комиков',
                                          'Библиотека', 'Популярный и успешный фильм', 'Мультфильм',
                                          'Фильм с низким бюджетом', 'Монополия', 'Скраббл', 'Шахматы',
                                          'Обслуживание еды и напитков', 'Предоставление захватывающих аттракционов',
                                          'Проведение художественных выставок'])
def handle_answer(message):
    user_id = message.from_user.id
    user_data = user_progress.get(user_id)

    if user_data:
        topic = user_data['topic']
        question_index = user_data['question_index']

        if topic == "Здоровье" and question_index < len(health_questions):
            question = health_questions[question_index]
        elif topic == "Спорт" and question_index < len(sport_questions):
            question = sport_questions[question_index]
        elif topic == "Работа" and question_index < len(job_questions):
            question = job_questions[question_index]
        elif topic == "Развлечения" and question_index < len(entertainment_questions):
            question = entertainment_questions[question_index]
        else:
            bot.send_message(message.chat.id, "Произошла ошибка. Пожалуйста, выберите тему снова.")
            return

        correct_option = question['correct_option']

        if message.text == question['options'][correct_option]:
            bot.send_message(message.chat.id, "Правильный ответ!")
            user_scores[user_id] += 1  # Увеличиваем баллы пользователя на 1
        else:
            bot.send_message(message.chat.id, "Неправильный ответ!")

        # Increment the question index and send the next question.
        user_progress[user_id]['question_index'] += 1
        send_next_question(user_id, message.chat.id)
    else:
        bot.send_message(message.chat.id, "Произошла ошибка. Пожалуйста, выберите тему снова.")


def display_results(user_id, chat_id):
    if user_id in user_scores:
        score = user_scores[user_id]
        bot.send_message(chat_id, f'Ваш результат: {score} баллов')
        del user_scores[user_id]  # Удалите баллы пользователя после отображения результата


@bot.message_handler(func=lambda message: message.text == "Вернуться к темам")
def return_to_topics(message):
    user_id = message.from_user.id
    if user_id in user_progress:
        del user_progress[user_id]
    bot.send_message(message.chat.id, "Вы вернулись к выбору тем.", reply_markup=topic_markup)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name}, выберите тему:'
    bot.send_message(message.chat.id, mess, reply_markup=topic_markup)


@bot.message_handler(func=lambda message: message.text in ['Здоровье', 'Спорт', 'Работа', 'Развлечения'])
def handle_topic(message):
    bot.send_message(message.chat.id, f'Вы выбрали тему: {message.text}')


@bot.message_handler()
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "Hello", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой id: {message.from_user.id}", parse_mode='html')
    elif message.text == "porn":
        bot.send_video(message.chat.id, anim)
    else:
        bot.send_message(message.chat.id, "Я не знаю о чем ты", parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_photo(message.chat.id, sticker)


bot.polling(none_stop=True)
