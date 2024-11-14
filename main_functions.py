import os.path
from tkinter import filedialog, messagebox, Label

from employee_person import EmployeePerson
from utils import Utils, AnalyzeStatus, ANALYZE_STATUS, FIRST_FILENAME, SECOND_FILENAME
from xlsx_handler import XlsxHandler


class MainUIFunctions:

    @staticmethod
    def on_first_file_open_button_click(file_label: Label, app_label: Label, persons: list[EmployeePerson], main_variables: dict):
        file_path = filedialog.askopenfilename(
            title="Выберите файл 1",
            filetypes=(("Excel files", "*.xlsx *.xls"), ("All files", "*.*"))
        )

        if file_path:
            simple_file_name = Utils.reduce_absolute_path_to_simple_name(file_path)

            file_label.config(text=f"Загружен файл: {simple_file_name}")
            app_label.config(text="Информация об анализе файлов", fg="black")

            persons_from_xlsx = XlsxHandler.get_list_of_employee_persons_from_xlsx_file(path=file_path)
            persons.clear()
            persons.extend(persons_from_xlsx)

            main_variables[FIRST_FILENAME] = os.path.splitext(simple_file_name)[0]
            main_variables[ANALYZE_STATUS] = AnalyzeStatus.NOT_ANALYZED

    @staticmethod
    def on_second_file_open_button_click(file_label: Label, app_label: Label, persons: list[EmployeePerson], main_variables: dict):
        file_path = filedialog.askopenfilename(
            title="Выберите файл 2",
            filetypes=(("Excel files", "*.xlsx *.xls"), ("All files", "*.*"))
        )

        if file_path:
            simple_file_name = Utils.reduce_absolute_path_to_simple_name(file_path)

            file_label.config(text=f"Загружен файл: {Utils.reduce_absolute_path_to_simple_name(file_path)}")
            app_label.config(text="Информация об анализе файлов", fg="black")

            persons_from_xlsx = XlsxHandler.get_list_of_employee_persons_from_xlsx_file(path=file_path)
            persons.clear()
            persons.extend(persons_from_xlsx)

            main_variables[SECOND_FILENAME] = os.path.splitext(simple_file_name)[0]
            main_variables[ANALYZE_STATUS] = AnalyzeStatus.NOT_ANALYZED

    @staticmethod
    def on_analyze_button_click(
            first_person_list: list[EmployeePerson],
            second_person_list: list[EmployeePerson],
            label: Label,
            main_variables: dict
    ):
        if Utils.is_not_empty(first_person_list) and Utils.is_not_empty(second_person_list):

            difference_between_first_and_second_list = set(first_person_list) - set(second_person_list)
            difference_between_second_and_first_list = set(second_person_list) - set(first_person_list)

            if (Utils.is_not_empty(difference_between_first_and_second_list) and
                    Utils.is_not_empty(difference_between_second_and_first_list)):
                label.config(text="Оба файла имеют отличия.", fg="red")
                main_variables[ANALYZE_STATUS] = AnalyzeStatus.ANALYZED_ONE_TWO_READY

                Utils.mark_persons_with_difference(
                    persons=first_person_list,
                    difference_list=list(difference_between_first_and_second_list)
                )

                Utils.mark_persons_with_difference(
                    persons=second_person_list,
                    difference_list=list(difference_between_second_and_first_list)
                )

            elif Utils.is_not_empty(difference_between_first_and_second_list):
                label.config(text="Первый файл имеет отличия от второго", fg="red")
                main_variables[ANALYZE_STATUS] = AnalyzeStatus.ANALYZED_ONE_READY

                Utils.mark_persons_with_difference(
                    persons=first_person_list,
                    difference_list=list(difference_between_first_and_second_list)
                )

            elif Utils.is_not_empty(difference_between_second_and_first_list):
                label.config(text="Второй файл имеет отличия от первого", fg="red")
                main_variables[ANALYZE_STATUS] = AnalyzeStatus.ANALYZED_TWO_READY

                Utils.mark_persons_with_difference(
                    persons=second_person_list,
                    difference_list=list(difference_between_second_and_first_list)
                )

            else:
                label.config(text="Файлы идеентичны по основным графам", fg="green")
                main_variables[ANALYZE_STATUS] = AnalyzeStatus.FILES_HAVE_NOT_DIFFERENCES
        else:
            messagebox.showinfo("Информация", "Сначала откройте два файла c рабочей таблицей")

    @staticmethod
    def on_generate_new_files_click(
            first_person_list: list[EmployeePerson],
            second_person_list: list[EmployeePerson],
            main_variables: dict
    ):
        current_status = main_variables[ANALYZE_STATUS]

        if current_status == AnalyzeStatus.NOT_ANALYZED:
            messagebox.showinfo("Информация", "Перед сохранением откройте и проанализируйте файлы")
        elif current_status == AnalyzeStatus.FILES_HAVE_NOT_DIFFERENCES:
            messagebox.showinfo("Информация", "Файлы идеентичны и не требуют сохранения")
        elif current_status == AnalyzeStatus.ANALYZED_ONE_READY:
            directory_path = filedialog.askdirectory(title="Выберите папку для сохранения")

            if directory_path:
                try:
                    file_path = os.path.join(directory_path, f"{main_variables[FIRST_FILENAME]}_marked.xlsx")
                    XlsxHandler.save_employee_persons_to_xlsx_file(
                        path=file_path,
                        employees=first_person_list
                    )
                    messagebox.showinfo("Сохранение файла", f"Файл успешно сохранён в {directory_path}.")
                except Exception as e:
                    messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")
        elif current_status == AnalyzeStatus.ANALYZED_TWO_READY:
            directory_path = filedialog.askdirectory(title="Выберите папку для сохранения")

            if directory_path:
                try:
                    file_path = os.path.join(directory_path, f"{main_variables[SECOND_FILENAME]}_marked.xlsx")
                    XlsxHandler.save_employee_persons_to_xlsx_file(
                        path=file_path,
                        employees=second_person_list
                    )
                    messagebox.showinfo("Сохранение файла", f"Файл успешно сохранён в {directory_path}.")
                except Exception as e:
                    messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")
        elif current_status == AnalyzeStatus.ANALYZED_ONE_TWO_READY:

            directory_path = filedialog.askdirectory(title="Выберите папку для сохранения")

            if directory_path:
                try:
                    file_path_1 = os.path.join(directory_path, f"{main_variables[FIRST_FILENAME]}_marked.xlsx")
                    file_path_2 = os.path.join(directory_path, f"{main_variables[SECOND_FILENAME]}_marked.xlsx")

                    XlsxHandler.save_employee_persons_to_xlsx_file(
                        path=file_path_1,
                        employees=first_person_list
                    )

                    XlsxHandler.save_employee_persons_to_xlsx_file(
                        path=file_path_2,
                        employees=second_person_list
                    )
                    messagebox.showinfo("Сохранение файла", f"Файлы успешно сохранёны в {directory_path}.")
                except Exception as e:
                    messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")


