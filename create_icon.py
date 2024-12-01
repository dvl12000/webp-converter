from PIL import Image, ImageDraw

def create_icon(size=(256, 256)):
    # Создаем новое изображение с прозрачным фоном
    image = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    # Рисуем синий круг
    circle_color = (33, 150, 243)  # Material Blue
    circle_bounds = (20, 20, 236, 236)
    draw.ellipse(circle_bounds, fill=circle_color)

    # Рисуем белую стрелку конвертации
    arrow_color = (255, 255, 255)
    arrow_width = 20

    # Горизонтальная линия
    draw.rectangle((78, 118, 178, 138), fill=arrow_color)

    # Наконечник стрелки
    arrow_points = [
        (178, 128),  # Центр
        (148, 88),   # Верхний угол
        (148, 168)   # Нижний угол
    ]
    draw.polygon(arrow_points, fill=arrow_color)

    # Сохраняем как ICO
    image.save('icon.ico', format='ICO', sizes=[(256, 256)])

if __name__ == '__main__':
    create_icon()
