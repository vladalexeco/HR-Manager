import tkinter as tk

from employee_person import EmployeePerson
from main_functions import MainUIFunctions
from utils import AnalyzeStatus, ANALYZE_STATUS


def mainUI():

    root = tk.Tk()
    root.title("HR Manager 1.0")
    root.minsize(400, 400)
    root.maxsize(400, 400)

    first_file_persons_list: list[EmployeePerson] = list()
    second_file_persons_list: list[EmployeePerson] = list()

    main_variables = {
        ANALYZE_STATUS: AnalyzeStatus.NOT_ANALYZED
    }

    for i in range(8):
        root.grid_rowconfigure(i, weight=1, uniform="equal")

    for j in range(2):
        root.grid_columnconfigure(j, weight=1, uniform="equal")

    root.grid_rowconfigure(6, weight=1)

    first_file_open_button = tk.Button(
        root,
        text="Файл 1",
        font=("Arial", 12),
        command=lambda: MainUIFunctions.on_first_file_open_button_click(
            first_file_information_label,
            first_file_persons_list,
            main_variables
        )
    )
    first_file_open_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    second_file_open_button = tk.Button(
        root,
        text="Файл 2",
        font=("Arial", 12),
        command=lambda: MainUIFunctions.on_second_file_open_button_click(
            second_file_information_label,
            second_file_persons_list,
            main_variables
        )
    )
    second_file_open_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    first_file_information_label = tk.Label(root, text="Информация о файле 1", font=("Arial", 12, "bold"), fg="black")
    first_file_information_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    second_file_information_label = tk.Label(root, text="Информация о файле 2", font=("Arial", 12, "bold"), fg="black")
    second_file_information_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    app_information_label = tk.Label(root, text="Информация об анализе файлов", font=("Arial", 12, "bold"), fg="black")
    app_information_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    analyze_button = tk.Button(
        root,
        text="Анализировать",
        font=("Arial", 12),
        command=lambda: MainUIFunctions.on_analyze_button_click(
            first_person_list=first_file_persons_list,
            second_person_list=second_file_persons_list,
            label=app_information_label,
            main_variables=main_variables
        )
    )
    analyze_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    save_button = tk.Button(
        root,
        text="Сохранить",
        font=("Arial", 12),
        command=lambda: MainUIFunctions.on_generate_new_files_click(
            first_person_list=first_file_persons_list,
            second_person_list=second_file_persons_list,
            main_variables=main_variables
        )
    )
    save_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    root.mainloop()

if __name__ == '__main__':
    mainUI()


