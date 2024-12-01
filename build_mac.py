import PyInstaller.__main__
import os
import pkg_resources
import sys

# Получаем путь к CustomTkinter
customtkinter_path = pkg_resources.resource_filename('customtkinter', '')

# Создаем .spec файл для macOS
spec_content = f'''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['webp_to_mp4_converter.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('{customtkinter_path}', 'customtkinter/'),
    ],
    hiddenimports=[
        'PIL._tkinter_finder',
        'imageio',
        'imageio_ffmpeg',
        'imageio_ffmpeg.binaries',
        'moviepy',
        'moviepy.editor',
        'moviepy.video.io.VideoFileClip',
        'moviepy.video.VideoClip',
        'moviepy.video.io.ffmpeg_writer',
        'numpy',
        'cv2',
        'tkinter',
        'tkinter.filedialog',
        'tkinter.messagebox'
    ],
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='WebP Converter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=True,
    target_arch=None,  
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='WebP Converter',
)

app = BUNDLE(
    coll,
    name='WebP Converter.app',
    icon='icon.icns',
    bundle_identifier='com.emilhaybullin.webpconverter',
    info_plist={{
        'NSHighResolutionCapable': True,
        'LSMinimumSystemVersion': '10.15.0',
        'NSRequiresAquaSystemAppearance': False,
        'CFBundleShortVersionString': '1.0.1',
        'CFBundleVersion': '1.0.1',
    }},
)
'''

# Записываем .spec файл
with open('WebP Converter Mac.spec', 'w', encoding='utf-8') as f:
    f.write(spec_content)

print("Для сборки на Mac выполните следующие команды:")
print("\n1. Создайте иконку:")
print("python make_icns.py")
print("iconutil -c icns icon.iconset")
print("\n2. Соберите приложение:")
print("python -m PyInstaller 'WebP Converter Mac.spec'")
print("\n3. Подпишите приложение (опционально):")
print("codesign --deep --force --sign 'Apple Development' 'dist/WebP Converter.app'")
