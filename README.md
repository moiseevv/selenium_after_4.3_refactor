# selenium_after_4.3_refactor

Была ошибка:<br>
AttributeError: 'WebDriver' object has no attribute 'find_element_by_tag_name'

Для версии selenium после версии 4.3 нужно переписать некоторые функции
Для оптимизации процесса сделан данный скрипт

1. Читает все файлы в директории. Находит среди них .py
2. Создает директорию result_refactoring и складывает в нее переделанные файлы
