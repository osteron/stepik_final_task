# Финальное задание по курсу [Автоматизация тестирования с помощью Selenium и Python](https://stepik.org/course/575)
Здесь расположено решение финального задания курса, описание находится по [ссылке](https://stepik.org/lesson/201964/step/15?unit=176022).\
Список требований к решению задания находится [здесь](https://stepik.org/lesson/201964/step/14?unit=176022).
## Список основным команд в терминале (выполнять в корне директории тестов)
Для запуска всех тестов:\
`pytest -s -v`
\
\
Для запуска тестов с меткой __need_review__:\
`pytest -v --tb=line -m need_review`
\
\
Для запуска тестов с меткой __login_guest__:\
`pytest -v --tb=line -m login_guest`
\
\
Для запуска тестов с меткой __register_user__:\
`pytest -v --tb=line -m register_user`
