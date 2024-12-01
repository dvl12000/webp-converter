import PyInstaller.__main__
import os
import sys
import customtkinter
import pkg_resources

# Путь к основному скрипту
script_path = "webp_to_mp4_converter.py"

# Путь к иконке
icon_path = "icon.ico"

# Получаем путь к customtkinter
ctk_path = os.path.dirname(customtkinter.__file__)

# Параметры для PyInstaller
options = [
    script_path,
    "--onefile",
    "--windowed",
    "--icon=" + icon_path,
    "--name=WebP Converter",
    f"--add-data={ctk_path};customtkinter/",
    "--hidden-import=PIL._tkinter_finder",
    "--hidden-import=imageio",
    "--hidden-import=imageio_ffmpeg",
    "--hidden-import=moviepy",
    "--hidden-import=numpy",
    "--hidden-import=customtkinter",
    "--hidden-import=packaging.version",
    "--hidden-import=packaging.specifiers",
    "--hidden-import=packaging.requirements",
]

# Запуск сборки
PyInstaller.__main__.run(options)
