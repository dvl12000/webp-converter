import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os
import sys
from moviepy.editor import ImageSequenceClip, VideoFileClip, ImageClip
import tempfile
import numpy as np
import platform

class FormatConverter(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Определяем, на какой ОС запущено приложение
        self.is_mac = platform.system() == "Darwin"
        
        # Настройка окна
        self.title("WebP Converter")
        self.geometry("800x700")  # Увеличим размер для списка файлов
        
        # Устанавливаем тему
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Если это Mac, настраиваем специфичные для Mac параметры
        if self.is_mac:
            self.configure(padx=20, pady=20)  # Добавляем отступы для соответствия macOS guidelines
            
        # Флаг для отмены конвертации
        self.cancel_conversion = False

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=25, pady=25)

        # Заголовок
        self.title_label = ctk.CTkLabel(
            self.main_frame, 
            text="WebP Converter", 
            font=("SF Pro Display" if self.is_mac else "Segoe UI", 32, "bold")
        )
        self.title_label.pack(pady=(0, 30))

        # Фрейм для выбора входных файлов
        self.input_frame = ctk.CTkFrame(self.main_frame)
        self.input_frame.pack(fill="x", pady=(0, 15))

        self.input_label = ctk.CTkLabel(
            self.input_frame, 
            text="Выберите WebP файлы:",
            font=("SF Pro Display" if self.is_mac else "Segoe UI", 14, "bold")
        )
        self.input_label.pack(side="left", padx=15)

        # Создаем кнопки с учетом стиля macOS
        button_height = 32 if self.is_mac else 35  # Mac использует меньшую высоту кнопок
        
        self.browse_button = ctk.CTkButton(
            self.input_frame,
            text="Обзор",
            command=self.browse_input_files,  
            width=120,
            height=button_height,
            font=("SF Pro Display" if self.is_mac else "Segoe UI", 13, "bold")
        )
        self.browse_button.pack(side="right", padx=15)

        # Список выбранных файлов
        self.files_frame = ctk.CTkFrame(self.main_frame)
        self.files_frame.pack(fill="both", expand=True, pady=(0, 15))

        self.files_label = ctk.CTkLabel(
            self.files_frame,
            text="Выбранные файлы:",
            font=("SF Pro Display" if self.is_mac else "Segoe UI", 14, "bold")
        )
        self.files_label.pack(anchor="w", padx=15, pady=(10, 5))

        # Создаем текстовое поле для отображения списка файлов
        self.files_text = ctk.CTkTextbox(
            self.files_frame,
            font=("SF Pro Display" if self.is_mac else "Segoe UI", 12),
            height=150
        )
        self.files_text.pack(fill="both", expand=True, padx=15, pady=(0, 10))
        
        # Кнопка очистки списка
        self.clear_button = ctk.CTkButton(
            self.files_frame,
            text="Очистить список",
            command=self.clear_files,
            width=120,
            height=button_height,
            font=("SF Pro Display" if self.is_mac else "Segoe UI", 13)
        )
        self.clear_button.pack(anchor="e", padx=15, pady=(0, 10))

        # Фрейм для выбора выходной директории
        self.output_frame = ctk.CTkFrame(self.main_frame)
        self.output_frame.pack(fill="x", pady=(0, 15))

        self.output_label = ctk.CTkLabel(
            self.output_frame, 
            text="Сохранить в:",
            font=("SF Pro Display" if self.is_mac else "Segoe UI", 14, "bold")
        )
        self.output_label.pack(side="left", padx=15)

        self.output_entry = ctk.CTkEntry(
            self.output_frame,
            placeholder_text="Папка для сохранения конвертированных файлов...",
            width=350,
            font=("SF Pro Display" if self.is_mac else "Segoe UI", 13),
            height=35
        )
        self.output_entry.pack(side="left", padx=15, fill="x", expand=True)

        self.output_button = ctk.CTkButton(
            self.output_frame,
            text="Обзор",
            command=self.browse_output_dir,
            width=120,
            height=button_height,
            font=("SF Pro Display" if self.is_mac else "Segoe UI", 13, "bold")
        )
        self.output_button.pack(side="right", padx=15)

        # Фрейм для настроек конвертации
        self.settings_frame = ctk.CTkFrame(self.main_frame)
        self.settings_frame.pack(fill="x", pady=(0, 25))

        # Левая часть настроек (формат)
        self.format_frame = ctk.CTkFrame(self.settings_frame)
        self.format_frame.pack(side="left", fill="x", expand=True, padx=(15, 7), pady=15)

        self.format_label = ctk.CTkLabel(
            self.format_frame,
            text="Формат:",
            font=("SF Pro Display" if self.is_mac else "Segoe UI", 14, "bold")
        )
        self.format_label.pack(side="left", padx=15)

        self.formats = {
            "MP4 (H.264)": ".mp4",
            "ProRes 422": ".mov",
            "ProRes 4444": ".mov",
            "GIF": ".gif",
            "WebM": ".webm",
            "AVI": ".avi"
        }

        self.format_var = ctk.StringVar(value="MP4 (H.264)")
        self.format_menu = ctk.CTkOptionMenu(
            self.format_frame,
            values=list(self.formats.keys()),
            variable=self.format_var,
            width=200,
            height=35,
            font=("SF Pro Display" if self.is_mac else "Segoe UI", 13)
        )
        self.format_menu.pack(side="left", padx=15)

        # Правая часть настроек (FPS)
        self.fps_frame = ctk.CTkFrame(self.settings_frame)
        self.fps_frame.pack(side="right", fill="x", expand=True, padx=(7, 15), pady=15)

        self.fps_label = ctk.CTkLabel(
            self.fps_frame,
            text="Частота кадров (FPS):",
            font=("SF Pro Display" if self.is_mac else "Segoe UI", 13)
        )
        self.fps_label.pack(side="left", padx=15)

        self.fps_var = tk.StringVar(value="24")  
        self.fps_entry = ctk.CTkEntry(
            self.fps_frame,
            width=60,  
            textvariable=self.fps_var
        )
        self.fps_entry.pack(side="left")

        self.fps_slider = ctk.CTkSlider(
            self.fps_frame,
            from_=1,
            to=120,
            number_of_steps=119,
            width=200,
            command=self.update_fps_from_slider
        )
        self.fps_slider.pack(side="left", padx=15)
        self.fps_slider.set(24)  

        # Прогресс бар
        self.progress = ctk.CTkProgressBar(self.main_frame)
        self.progress.pack(fill="x", padx=15, pady=(0, 15))
        self.progress.set(0)
        self.progress.pack_forget()  

        # Фрейм для кнопок
        self.buttons_frame = ctk.CTkFrame(self.main_frame)
        self.buttons_frame.pack(fill="x", pady=(0, 15))

        # Центрируем кнопки
        self.buttons_frame.grid_columnconfigure(0, weight=1)
        self.buttons_frame.grid_columnconfigure(3, weight=1)

        # Кнопка конвертации
        self.convert_button = ctk.CTkButton(
            self.buttons_frame,
            text="Конвертировать",
            command=self.convert_files,
            height=45,
            width=200,
            font=("SF Pro Display" if self.is_mac else "Segoe UI", 15, "bold")
        )
        self.convert_button.grid(row=0, column=1, padx=5)

        # Кнопка отмены
        self.cancel_button = ctk.CTkButton(
            self.buttons_frame,
            text="Отмена",
            command=self.cancel_conversion_process,
            height=45,
            width=120,
            font=("SF Pro Display" if self.is_mac else "Segoe UI", 15),
            fg_color="#FF5252",
            hover_color="#FF1744"
        )
        self.cancel_button.grid(row=0, column=2, padx=5)

        # Статус
        self.status_label = ctk.CTkLabel(
            self.main_frame,
            text="Готов к работе",
            font=("SF Pro Display" if self.is_mac else "Segoe UI", 13)
        )
        self.status_label.pack()

        # Нижний фрейм для подписи
        self.bottom_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent", height=30)
        self.bottom_frame.pack(fill="x", pady=(5, 0))
        self.bottom_frame.pack_propagate(False)  

        # Подпись (справа внизу)
        self.signature = ctk.CTkLabel(
            self.bottom_frame,
            text="by Emil Haybullin",
            font=("SF Pro Display" if self.is_mac else "Segoe UI", 12),
            text_color="#8e929a"
        )
        self.signature.pack(side="right", padx=(0, 15))

        # Список для хранения путей к файлам
        self.input_files = []

    def cancel_conversion_process(self):
        self.cancel_conversion = True
        self.status_label.configure(text="Отмена конвертации...")
        self.cancel_button.configure(state="disabled")

    def browse_input_files(self):
        filetypes = (
            ("WebP файлы", "*.webp"),
        )
        
        # На Mac используем NSOpenPanel через tkinter
        if self.is_mac:
            files = filedialog.askopenfilenames(
                title="Выберите WebP файлы",
                filetypes=filetypes,
                initialdir="~/Desktop"  # Начальная директория для Mac
            )
        else:
            files = filedialog.askopenfilenames(
                title="Выберите WebP файлы",
                filetypes=filetypes
            )
        
        if files:
            self.input_files = list(files)
            self.update_files_list()

    def update_files_list(self):
        self.files_text.delete("1.0", "end")
        for i, file in enumerate(self.input_files, 1):
            self.files_text.insert("end", f"{i}. {os.path.basename(file)}\n")

    def clear_files(self):
        self.input_files = []
        self.update_files_list()

    def browse_output_dir(self):
        directory = filedialog.askdirectory(
            title="Выберите папку для сохранения"
        )
        if directory:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, directory)

    def update_fps_from_slider(self, value):
        self.fps_var.set(str(int(value)))

    def get_fps(self):
        try:
            fps = int(self.fps_var.get())
            if 1 <= fps <= 120:
                return fps
            raise ValueError
        except ValueError:
            messagebox.showerror("Ошибка", "Частота кадров должна быть числом от 1 до 120")
            return None

    def convert_to_gif(self, input_path, output_path, fps):
        """Конвертирует файл в GIF с сохранением анимации и максимальным качеством"""
        try:
            # Для WebP файлов используем Pillow
            if input_path.lower().endswith('.webp'):
                with Image.open(input_path) as img:
                    # Проверяем, является ли изображение анимированным
                    try:
                        frames = []
                        duration = []
                        while True:
                            # Преобразуем каждый кадр в RGB для лучшего качества
                            frame = img.convert('RGB')
                            frames.append(frame)
                            duration.append(img.info.get('duration', 1000 // fps))
                            img.seek(img.tell() + 1)
                    except EOFError:
                        pass

                    if len(frames) > 1:  # Если это анимация
                        frames[0].save(
                            output_path,
                            save_all=True,
                            append_images=frames[1:],
                            duration=duration,
                            loop=0,
                            optimize=False,  # Отключаем оптимизацию размера
                            quality=100,     # Максимальное качество
                            dither=None      # Отключаем дизеринг для сохранения четкости
                        )
                    else:  # Если это статичное изображение
                        img.convert('RGB').save(
                            output_path,
                            'GIF',
                            quality=100,
                            dither=None
                        )
        except Exception as e:
            raise Exception(f"Ошибка при конвертации в GIF: {str(e)}")

    def should_replace_file(self, filepath):
        """Спрашивает пользователя о замене существующего файла"""
        if os.path.exists(filepath):
            response = messagebox.askyesno(
                "Файл существует",
                f"Файл {os.path.basename(filepath)} уже существует. Заменить?",
                icon='warning'
            )
            return response
        return True

    def convert_files(self):
        if not self.input_files:
            messagebox.showerror("Ошибка", "Пожалуйста, выберите файлы для конвертации")
            return

        # Показываем и обнуляем прогресс бар перед началом конвертации
        self.progress.pack(fill="x", padx=15, pady=(0, 15))
        self.progress.set(0)

        fps = self.get_fps()
        if fps is None:
            return

        format_name = self.format_var.get()
        format_ext = self.formats[format_name]
        output_dir = self.output_entry.get()

        if not output_dir:
            # На Mac используем домашнюю директорию пользователя как дефолтную
            if self.is_mac:
                output_dir = os.path.expanduser("~/Desktop")
            else:
                output_dir = os.path.dirname(self.input_files[0])

        # Активируем кнопку отмены
        self.cancel_button.configure(state="normal")
        self.cancel_conversion = False

        total_files = len(self.input_files)
        converted_count = 0

        for i, input_path in enumerate(self.input_files, 1):
            if self.cancel_conversion:
                break

            try:
                # Проверяем, что это WebP файл
                if not input_path.lower().endswith('.webp'):
                    messagebox.showerror("Ошибка", f"Файл {os.path.basename(input_path)} не является WebP файлом")
                    continue

                # Формируем путь выходного файла
                output_filename = os.path.splitext(os.path.basename(input_path))[0] + format_ext
                output_path = os.path.join(output_dir, output_filename)

                # Проверяем, нужно ли заменять существующий файл
                if not self.should_replace_file(output_path):
                    continue

                self.status_label.configure(text=f"Конвертация файла {i} из {total_files}...")
                
                # Устанавливаем прогресс
                self.progress.set((i - 1) / total_files)
                self.update()

                # Конвертация в зависимости от выходного формата
                if format_ext in ['.mp4', '.mov', '.avi', '.webm']:
                    # Конвертация в видео
                    with Image.open(input_path) as img:
                        if hasattr(img, 'n_frames') and img.n_frames > 1:
                            # Анимированное изображение
                            frames = []
                            for frame in range(img.n_frames):
                                img.seek(frame)
                                frame_array = np.array(img.convert('RGB'))
                                if frame_array is not None:
                                    frames.append(frame_array)
                                else:
                                    raise ValueError("Не удалось преобразовать кадр в массив")
                            
                            if not frames:
                                raise ValueError("Не удалось извлечь кадры из анимации")
                            
                            # Проверяем, что все кадры корректны
                            if not all(frame is not None and frame.shape[2] == 3 for frame in frames):
                                raise ValueError("Некоторые кадры не удалось корректно преобразовать в RGB")
                            
                            # Создаем клип только если есть корректные кадры
                            clip = None
                            try:
                                clip = ImageSequenceClip(frames, fps=fps)
                                if clip is None:
                                    raise ValueError("Не удалось создать видеоклип из кадров")
                                    
                                # Создаем временную директорию для промежуточных файлов
                                with tempfile.TemporaryDirectory() as temp_dir:
                                    temp_output = os.path.join(temp_dir, "temp_output" + format_ext)
                                    
                                    # Для Windows всегда используем libx264
                                    if not self.is_mac:
                                        clip.write_videofile(
                                            temp_output,
                                            codec='libx264',
                                            preset='medium',
                                            audio=False,
                                            logger=None  # Отключаем логгер moviepy для избежания конфликтов
                                        )
                                    else:
                                        if format_name == "ProRes 422":
                                            clip.write_videofile(
                                                temp_output,
                                                codec='prores_ks',
                                                preset='normal',
                                                ffmpeg_params=['-profile:v', '2'],
                                                audio=False,
                                                logger=None
                                            )
                                        elif format_name == "ProRes 4444":
                                            clip.write_videofile(
                                                temp_output,
                                                codec='prores_ks',
                                                preset='normal',
                                                ffmpeg_params=['-profile:v', '4'],
                                                audio=False,
                                                logger=None
                                            )
                                        else:
                                            clip.write_videofile(
                                                temp_output,
                                                codec='libx264',
                                                preset='medium',
                                                audio=False,
                                                logger=None
                                            )
                                    
                                    # Проверяем, что файл существует и имеет размер больше 0
                                    if os.path.exists(temp_output) and os.path.getsize(temp_output) > 0:
                                        import shutil
                                        shutil.copy2(temp_output, output_path)
                                        # Проверяем успешность копирования
                                        if not os.path.exists(output_path):
                                            raise ValueError("Не удалось скопировать файл в целевую директорию")
                                    else:
                                        raise ValueError("Ошибка при создании временного файла")
                                        
                            finally:
                                # Закрываем клип и удаляем временные файлы
                                if clip is not None:
                                    try:
                                        clip.close()
                                    except:
                                        pass
                        else:
                            # Статичное изображение
                            frame_array = np.array(img.convert('RGB'))
                            if frame_array is None:
                                raise ValueError("Не удалось преобразовать изображение в массив")
                            
                            # Проверяем корректность кадра
                            if frame_array.shape[2] != 3:
                                raise ValueError("Не удалось корректно преобразовать изображение в RGB")
                            
                            # Создаем клип только если кадр корректный
                            clip = None
                            try:
                                clip = ImageClip(frame_array).set_duration(5)
                                if clip is None:
                                    raise ValueError("Не удалось создать видеоклип из изображения")
                                    
                                # Создаем временную директорию для промежуточных файлов
                                with tempfile.TemporaryDirectory() as temp_dir:
                                    temp_output = os.path.join(temp_dir, "temp_output" + format_ext)
                                    
                                    # Для Windows всегда используем libx264
                                    if not self.is_mac:
                                        clip.write_videofile(
                                            temp_output,
                                            codec='libx264',
                                            preset='medium',
                                            audio=False,
                                            logger=None  # Отключаем логгер moviepy для избежания конфликтов
                                        )
                                    else:
                                        if format_name == "ProRes 422":
                                            clip.write_videofile(
                                                temp_output,
                                                codec='prores_ks',
                                                preset='normal',
                                                ffmpeg_params=['-profile:v', '2'],
                                                audio=False,
                                                logger=None
                                            )
                                        elif format_name == "ProRes 4444":
                                            clip.write_videofile(
                                                temp_output,
                                                codec='prores_ks',
                                                preset='normal',
                                                ffmpeg_params=['-profile:v', '4'],
                                                audio=False,
                                                logger=None
                                            )
                                        else:
                                            clip.write_videofile(
                                                temp_output,
                                                codec='libx264',
                                                preset='medium',
                                                audio=False,
                                                logger=None
                                            )
                                    
                                    # Проверяем, что файл существует и имеет размер больше 0
                                    if os.path.exists(temp_output) and os.path.getsize(temp_output) > 0:
                                        import shutil
                                        shutil.copy2(temp_output, output_path)
                                        # Проверяем успешность копирования
                                        if not os.path.exists(output_path):
                                            raise ValueError("Не удалось скопировать файл в целевую директорию")
                                    else:
                                        raise ValueError("Ошибка при создании временного файла")
                                        
                            finally:
                                # Закрываем клип и удаляем временные файлы
                                if clip is not None:
                                    try:
                                        clip.close()
                                    except:
                                        pass
                elif format_ext == '.gif':
                    # Конвертация в GIF
                    self.convert_to_gif(input_path, output_path, fps)
                else:
                    # Конвертация в другой формат изображения
                    with Image.open(input_path) as img:
                        img.save(output_path)

                converted_count += 1

            except Exception as e:
                if not self.cancel_conversion:
                    messagebox.showerror("Ошибка", f"Ошибка при конвертации файла {os.path.basename(input_path)}: {str(e)}")
                continue

        # Сбрасываем интерфейс
        self.cancel_button.configure(state="disabled")
        self.progress.set(1)
        if self.cancel_conversion:
            self.status_label.configure(text=f"Конвертация отменена. Сконвертировано {converted_count} из {total_files} файлов")
        else:
            self.status_label.configure(text=f"Конвертация завершена. Сконвертировано {converted_count} из {total_files} файлов")

if __name__ == "__main__":
    app = FormatConverter()
    app.mainloop()
