import os
import subprocess
from PIL import Image

def create_icns():
    # Создаем временную директорию для иконок
    if not os.path.exists('icon.iconset'):
        os.makedirs('icon.iconset')

    # Загружаем исходную иконку
    img = Image.open('app_icon.ico')

    # Размеры, необходимые для macOS
    sizes = [16, 32, 64, 128, 256, 512, 1024]

    # Создаем иконки разных размеров
    for size in sizes:
        # Нормальное разрешение
        resized = img.resize((size, size), Image.Resampling.LANCZOS)
        resized.save(f'icon.iconset/icon_{size}x{size}.png')
        
        # Retina разрешение (2x)
        if size * 2 <= 1024:  # Проверяем, чтобы размер не превышал 1024
            resized = img.resize((size * 2, size * 2), Image.Resampling.LANCZOS)
            resized.save(f'icon.iconset/icon_{size}x{size}@2x.png')

    # На macOS используем iconutil для создания .icns
    print("На Mac выполните команду:")
    print("iconutil -c icns icon.iconset")

if __name__ == '__main__':
    create_icns()
