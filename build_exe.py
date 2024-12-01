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
    "--hidden-import=imageio_ffmpeg.binaries",
    "--hidden-import=moviepy",
    "--hidden-import=moviepy.editor",
    "--hidden-import=moviepy.video.io.VideoFileClip",
    "--hidden-import=moviepy.video.VideoClip",
    "--hidden-import=moviepy.video.io.ffmpeg_writer",
    "--hidden-import=numpy",
    "--hidden-import=cv2",
    "--hidden-import=customtkinter",
    "--hidden-import=packaging.version",
    "--hidden-import=packaging.specifiers",
    "--hidden-import=packaging.requirements",
    "--hidden-import=tkinter",
    "--hidden-import=tkinter.filedialog",
    "--hidden-import=tkinter.messagebox",
    "--collect-data=customtkinter",
    "--collect-data=moviepy",
    "--version-file=version_info.txt"
]

# Создаем файл с информацией о версии
version_info = '''
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(1, 0, 1, 0),
    prodvers=(1, 0, 1, 0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo(
      [
        StringTable(
          u'040904B0',
          [StringStruct(u'CompanyName', u'Emil Haybullin'),
           StringStruct(u'FileDescription', u'WebP Converter'),
           StringStruct(u'FileVersion', u'1.0.1'),
           StringStruct(u'InternalName', u'WebP Converter'),
           StringStruct(u'LegalCopyright', u' 2024 Emil Haybullin. All rights reserved.'),
           StringStruct(u'OriginalFilename', u'WebP Converter.exe'),
           StringStruct(u'ProductName', u'WebP Converter'),
           StringStruct(u'ProductVersion', u'1.0.1')])
      ]
    ),
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
'''

# Записываем информацию о версии в файл
with open('version_info.txt', 'w', encoding='utf-8') as f:
    f.write(version_info)

print("Сборка Windows приложения...")
PyInstaller.__main__.run(options)
print("Сборка завершена!")
