# повторная проверка и импорт модулей
try:
    from colorama import init, Fore
except ModuleNotFoundError:
    # если модуля не окажется, скрипт обратно запустит bootstrapper
    bootstrap_path = "bootstrapper.py"
    subprocess.Popen(
        ["cmd", "/c", sys.executable, str(bootstrap_path)],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

# True
init(autoreset=True)
print(f"{Fore.LIGHTGREEN_EX}Проверка прошла успешно!")