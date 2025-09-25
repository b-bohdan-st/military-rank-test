import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import random
import os


class MilitaryRanksTrainer:
    def __init__(self):
        self.ranks_dict = {
            "image1.png": "Солдат",
            "image2.png": "Старший солдат",
            "image3.png": "Молодший сержант",
            "image4.png": "Сержант",
            "image5.png": "Старший сержант",
            "image6.png": "Головний сержант",
            "image7.png": "Штаб-сержант",
            "image8.png": "Майстер-сержант",
            "image9.png": "Старший майстер-сержант",
            "image10.png": "Головний майстер-сержант",
            "image11.png": "Молодший лейтенант",
            "image12.png": "Лейтенант",
            "image13.png": "Старший лейтенант",
            "image14.png": "Капітан",
            "image15.png": "Майор",
            "image16.png": "Підполковник",
            "image17.png": "Полковник",
            "image18.png": "Бригадний генерал",
            "image19.png": "Генерал-майор",
            "image20.png": "Генерал-лейтенант",
            "image21.png": "Генерал"
        }

        self.current_image = None
        self.current_answer = None

        self.root = tk.Tk()
        self.root.title("Тренажер військових звань")
        self.root.geometry("500x650")
        self.root.resizable(False, False)

        self.setup_ui()
        self.load_random_image()

    def setup_ui(self):
        title_label = tk.Label(self.root, text="Визначте військове звання",
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        self.image_label = tk.Label(self.root, bg="lightgray",
                                    width=150, height=400)
        self.image_label.pack(pady=10)

        instruction_label = tk.Label(self.root, text="Оберіть правильне звання:",
                                     font=("Arial", 12))
        instruction_label.pack(pady=(20, 5))

        self.rank_combobox = ttk.Combobox(self.root,
                                          values=list(self.ranks_dict.values()),
                                          state="readonly",
                                          font=("Arial", 11),
                                          width=25)
        self.rank_combobox.pack(pady=5)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        check_button = tk.Button(button_frame, text="Перевірити",
                                 command=self.check_answer,
                                 font=("Arial", 12), bg="lightblue",
                                 width=12, height=2)
        check_button.pack(side=tk.LEFT, padx=10)

        next_button = tk.Button(button_frame, text="Наступне",
                                command=self.load_random_image,
                                font=("Arial", 12), bg="lightgreen",
                                width=12, height=2)
        next_button.pack(side=tk.LEFT, padx=10)

        self.stats_label = tk.Label(self.root, text="Відповіді: 0 правильних з 0",
                                    font=("Arial", 10))
        self.stats_label.pack(pady=10)

        self.correct_answers = 0
        self.total_answers = 0

    def load_random_image(self):
        self.rank_combobox.set('')

        self.current_image = random.choice(list(self.ranks_dict.keys()))
        self.current_answer = self.ranks_dict[self.current_image]

        image_path = os.path.join("images", self.current_image)

        try:
            if os.path.exists(image_path):
                image = Image.open(image_path)
                image = image.resize((130, 350), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(image)

                self.image_label.configure(image=photo, text="")
                self.image_label.image = photo
            else:
                self.image_label.configure(image="",
                                           text=f"Зображення не знайдено:\n{self.current_image}")
        except Exception as e:
            self.image_label.configure(image="",
                                       text=f"Помилка завантаження:\n{str(e)}")

    def check_answer(self):
        selected_rank = self.rank_combobox.get()

        if not selected_rank:
            messagebox.showwarning("Увага", "Будь ласка, оберіть звання зі списку!")
            return

        self.total_answers += 1

        if selected_rank == self.current_answer:
            self.correct_answers += 1
            messagebox.showinfo("Результат", "Вірно! ✓")
        else:
            messagebox.showerror("Результат",
                                 f"Не вірно! ✗\n\nПравильна відповідь: {self.current_answer}")

        accuracy = (self.correct_answers / self.total_answers) * 100
        self.stats_label.config(
            text=f"Відповіді: {self.correct_answers} правильних з {self.total_answers} "
                 f"({accuracy:.1f}%)"
        )

        self.root.after(1000, self.load_random_image)

    def run(self):
        self.root.mainloop()


def main():
    if not os.path.exists("images"):
        messagebox.showerror("Помилка",
                             "Папка 'images' не знайдена!\n\n"
                             "Створіть папку 'images' у тій же директорії, "
                             "що й цей файл, та додайте зображення з назвами "
                             "image1.jpg, image2.jpg, ... image21.jpg")
        return

    app = MilitaryRanksTrainer()
    app.run()


if __name__ == "__main__":
    main()