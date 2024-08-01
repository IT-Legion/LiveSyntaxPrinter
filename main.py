from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter
import time
import os
import platform

def clear_console():
    # Определяем команду для очистки консоли в зависимости от ОС
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def get_syntax_highlighted_text(code: str, lexer, formatter) -> str:
    return highlight(code, lexer, formatter)


code = ("""\
#for exemple
print("Hello, world!")
""")

# Очищаем консоль
clear_console()
highlighted_text = get_syntax_highlighted_text(code, PythonLexer(), TerminalFormatter())

print("", flush=True)
for i in highlighted_text:
    time.sleep(0.025)
    print(i, end="", flush=True)

move = input("Выполнить: Да/нет\n>>> ").strip().lower()
if move in ['да', 'д', 'yes', 'y']:
    try:
        exec(code)
    except Exception as e:
        print(f"Произошла ошибка при выполнении кода: {e}")

elif move in ['нет', 'н', 'no', 'n']:
    exit()

else:
    exit()


