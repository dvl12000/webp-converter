# WebP Converter

A modern, cross-platform application for converting WebP files to various formats with a clean and intuitive interface.

![GitHub release (latest by date)](https://img.shields.io/github/v/release/dvl12000/webp-converter)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS-lightgrey)
![Python version](https://img.shields.io/badge/python-3.10-blue)

## 📸 Screenshots
![Main Window](https://raw.githubusercontent.com/dvl12000/webp-converter/main/screenshots/main-window.png)

*Main application window with dark theme*

![Files Added](https://raw.githubusercontent.com/dvl12000/webp-converter/main/screenshots/files-added.png)

*File selection and queue management*

## Features

- **Specialized WebP Conversion**: Convert both static and animated WebP files
- **Multiple Output Formats**:
  - MP4 (H.264)
  - ProRes 422
  - ProRes 4444
  - GIF
  - WebM
  - AVI
- **Batch Processing**: Convert multiple files at once
- **Modern Interface**: Clean and intuitive design using CustomTkinter
- **Configurable Settings**: Adjust FPS (1-120) for animated conversions
- **Cross-Platform**: Runs natively on Windows and macOS
- **Progress Tracking**: Real-time conversion progress display
- **Cancellable Operations**: Stop conversions at any time

## Installation

### Вариант 1: Запуск из исходного кода

1. Установите Python 3.10 или новее
2. Склонируйте репозиторий
3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Запустите программу:
```bash
python webp_to_mp4_converter.py
```

### Вариант 2: Использование готового файла

   WebP Converter
 - Для Windows - https://github.com/dvl12000/webp-converter/releases/download/v1.0.1/WebP.Converter.exe
 - Для MacOS - https://github.com/dvl12000/webp-converter/releases/download/v1.0.1/WebP-Converter-macOS.dmg

## Usage

1. Launch WebP Converter
2. Click "Add Files" or drag and drop WebP files into the application
3. Select your desired output format
4. Adjust FPS if needed (for animated WebP files)
5. Click "Convert" to start the conversion process

## Development

### Requirements
- Python 3.10+
- Required packages (install via pip):
  ```
  pip install -r requirements.txt
  ```

### Building from Source

#### Windows
```bash
python build_exe.py
```

#### macOS
```bash
python build_mac.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for the modern UI components
- [MoviePy](https://zulko.github.io/moviepy/) for video processing
- [Pillow](https://python-pillow.org/) for image processing

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Автор

Emil Haybullin
