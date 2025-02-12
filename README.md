# LiveSyntaxPrinter

**LiveSyntaxPrinter** — это Python-скрипт, который демонстрирует код с синтаксической подсветкой в консоли и позволяет выполнить его, если пользователь этого желает.

## Описание

Этот скрипт выполняет следующие функции:

1. **Очистка консоли**: В зависимости от операционной системы (Windows или Unix-подобная), консоль очищается перед выводом кода.
2. **Синтаксическая подсветка**: Код на Python подсвечивается с использованием библиотеки Pygments для улучшения читаемости.
3. **Постепенный вывод**: Подсвеченный код выводится в консоль постепенно, создавая эффект "печатного" текста.
4. **Запуск кода**: После показа синтаксически окрашенного кода, скрипт запрашивает у пользователя, хочет ли он выполнить этот код. В зависимости от ответа пользователя, код выполняется или программа завершает работу.

## Версия

Текущая версия: **0.1**

## Как использовать

1. Убедитесь, что у вас установлены необходимые зависимости. Скрипт требует библиотеку Pygments. Установите её с помощью pip:

    ```bash
    pip install pygments
    ```

2. Сохраните скрипт в файл, например `live_syntax_printer.py`.

3. Запустите скрипт:

    ```bash
    python live_syntax_printer.py
    ```

4. Следуйте инструкциям в консоли. Введите `да` или `yes`, чтобы выполнить код, или `нет` или `no`, чтобы завершить программу.

## Пример работы

При запуске скрипта консоль будет очищена, и код:

```python
#for exemple
print("Hello, world!")
