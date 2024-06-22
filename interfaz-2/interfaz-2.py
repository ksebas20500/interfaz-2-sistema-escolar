import tkinter as tk
from tkinter import ttk, messagebox

# Modelo de clases (se mantiene igual al código anterior)

class Curso:
    def __init__(self, nombre, profesor, horario):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []
        self.horario = horario

    def mostrar_info(self):
        print(f"Nombre del curso: {self.nombre}")
        self.profesor.mostrar_info()
        self.horario.mostrar_info()
        print("Estudiantes inscritos:")
        for estudiante in self.estudiantes:
            print(f"{estudiante.nombre} {estudiante.apellido}")

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        estudiante.cursos.append(self)

class Profesor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.asignaturas = []

    def mostrar_info(self):
        print(f"Nombre del maestro: {self.nombre} {self.apellido}")
        for asignatura in self.asignaturas:
            print(f"Asignatura: {asignatura.nombre}")

class Estudiante:
    def __init__(self, nombre, apellido, id_estudiante):
        self.nombre = nombre
        self.apellido = apellido
        self.id_estudiante = id_estudiante
        self.cursos = []

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} {self.apellido}, Id del estudiante: {self.id_estudiante}")
        for curso in self.cursos:
            print(f"Curso: {curso.nombre}")

class Asignatura:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        profesor.asignaturas.append(self)

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Profesor: {self.profesor.nombre} {self.profesor.apellido}")

class Evaluacion:
    def __init__(self, curso, estudiante, nota):
        self.curso = curso
        self.estudiante = estudiante
        self.nota = nota

    def mostrar_info(self):
        print(f"Evaluacion del curso: {self.curso.nombre}")
        print(f"Estudiante: {self.estudiante.nombre} {self.estudiante.apellido}, {self.estudiante.id_estudiante}")
        print(f"Nota: {self.nota}")

class Horario:
    def __init__(self, dia, hora_inicio, hora_fin):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def mostrar_info(self):
        print(f"Horario: {self.dia}, De {self.hora_inicio} a {self.hora_fin}")

# Interfaz gráfica

class SchoolApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión Escolar")
        self.root.geometry("900x600")

        # Colores
        self.bg_color = "#2c3e50"
        self.fg_color = "#ecf0f1"
        self.highlight_color = "#3498db"

        # Marco del menú
        self.menu_frame = tk.Frame(self.root, bg=self.bg_color, width=200)
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Opciones del menú
        menu_items = [
            ("Inicio", self.show_home),
            ("Cursos", self.show_courses),
            ("Estudiantes", self.show_students),
            ("Registrar Notas", self.show_register_grades),
            ("Ver Notas", self.show_view_grades),
            ("Ver Cursos", self.show_view_courses),
            ("Salir", self.root.quit)
        ]

        for item in menu_items:
            button = tk.Button(
                self.menu_frame, text=item[0], command=item[1], bg=self.bg_color,
                fg=self.fg_color, activebackground=self.highlight_color, activeforeground=self.fg_color,
                relief=tk.FLAT, padx=10, pady=5
            )
            button.pack(fill=tk.X)

        # Marco principal para contenido
        self.content_frame = tk.Frame(self.root, bg=self.fg_color)
        self.content_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Inicializar las pestañas
        self.setup_tabs()

        # Mostrar la pantalla de inicio por defecto
        self.show_home()

    def setup_tabs(self):
        # Crear una variable para almacenar la pestaña actual
        self.current_tab = None

        # Crear un widget Notebook para gestionar las pestañas
        self.tab_control = ttk.Notebook(self.content_frame)

        # Pestañas de la aplicación
        self.home_tab = ttk.Frame(self.tab_control)
        self.course_tab = ttk.Frame(self.tab_control)
        self.student_tab = ttk.Frame(self.tab_control)
        self.grade_tab = ttk.Frame(self.tab_control)
        self.view_grades_tab = ttk.Frame(self.tab_control)
        self.view_courses_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.home_tab, text="Inicio")
        self.tab_control.add(self.course_tab, text="Cursos")
        self.tab_control.add(self.student_tab, text="Estudiantes")
        self.tab_control.add(self.grade_tab, text="Registrar Notas")
        self.tab_control.add(self.view_grades_tab, text="Ver Notas")
        self.tab_control.add(self.view_courses_tab, text="Ver Cursos")

        self.tab_control.pack(expand=1, fill="both")

        # Configurar el contenido de cada pestaña
        self.setup_home_tab()
        self.setup_course_tab()
        self.setup_student_tab()
        self.setup_grade_tab()
        self.setup_view_grades_tab()
        self.setup_view_courses_tab()

    def show_home(self):
        self.tab_control.select(self.home_tab)

    def show_courses(self):
        self.tab_control.select(self.course_tab)

    def show_students(self):
        self.tab_control.select(self.student_tab)

    def show_register_grades(self):
        self.tab_control.select(self.grade_tab)

    def show_view_grades(self):
        self.tab_control.select(self.view_grades_tab)

    def show_view_courses(self):
        self.tab_control.select(self.view_courses_tab)

    def setup_home_tab(self):
        home_label = tk.Label(self.home_tab, text="Bienvenido al Sistema de Gestión Escolar", font=("Helvetica", 18))
        home_label.pack(pady=20)

    def setup_course_tab(self):
        # Course Name
        self.course_name_label = ttk.Label(self.course_tab, text="Nombre del Curso:")
        self.course_name_label.grid(column=0, row=0, padx=10, pady=10)
        self.course_name_entry = ttk.Entry(self.course_tab)
        self.course_name_entry.grid(column=1, row=0, padx=10, pady=10)

        # Professor
        self.professor_name_label = ttk.Label(self.course_tab, text="Nombre del Profesor:")
        self.professor_name_label.grid(column=0, row=1, padx=10, pady=10)
        self.professor_name_entry = ttk.Entry(self.course_tab)
        self.professor_name_entry.grid(column=1, row=1, padx=10, pady=10)

        self.professor_lastname_label = ttk.Label(self.course_tab, text="Apellido del Profesor:")
        self.professor_lastname_label.grid(column=0, row=2, padx=10, pady=10)
        self.professor_lastname_entry = ttk.Entry(self.course_tab)
        self.professor_lastname_entry.grid(column=1, row=2, padx=10, pady=10)

        # Course Schedule
        self.course_schedule_label = ttk.Label(self.course_tab, text="Horario del Curso (Día, Hora Inicio, Hora Fin):")
        self.course_schedule_label.grid(column=0, row=3, padx=10, pady=10)
        self.course_schedule_entry = ttk.Entry(self.course_tab)
        self.course_schedule_entry.grid(column=1, row=3, padx=10, pady=10)

        # Add Course Button
        self.add_course_button = ttk.Button(self.course_tab, text="Añadir Curso", command=self.add_course)
        self.add_course_button.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

    def setup_student_tab(self):
        # Student Name
        self.student_name_label = ttk.Label(self.student_tab, text="Nombre del Estudiante:")
        self.student_name_label.grid(column=0, row=0, padx=10, pady=10)
        self.student_name_entry = ttk.Entry(self.student_tab)
        self.student_name_entry.grid(column=1, row=0, padx=10, pady=10)

        # Student Lastname
        self.student_lastname_label = ttk.Label(self.student_tab, text="Apellido del Estudiante:")
        self.student_lastname_label.grid(column=0, row=1, padx=10, pady=10)
        self.student_lastname_entry = ttk.Entry(self.student_tab)
        self.student_lastname_entry.grid(column=1, row=1, padx=10, pady=10)

        # Student ID
        self.student_id_label = ttk.Label(self.student_tab, text="ID del Estudiante:")
        self.student_id_label.grid(column=0, row=2, padx=10, pady=10)
        self.student_id_entry = ttk.Entry(self.student_tab)
        self.student_id_entry.grid(column=1, row=2, padx=10, pady=10)

        # Add Student Button
        self.add_student_button = ttk.Button(self.student_tab, text="Añadir Estudiante", command=self.add_student)
        self.add_student_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

    def setup_grade_tab(self):
        # Course Combobox
        self.grade_course_label = ttk.Label(self.grade_tab, text="Curso:")
        self.grade_course_label.grid(column=0, row=0, padx=10, pady=10)
        self.grade_course_combobox = ttk.Combobox(self.grade_tab)
        self.grade_course_combobox.grid(column=1, row=0, padx=10, pady=10)

        # Student Combobox
        self.grade_student_label = ttk.Label(self.grade_tab, text="Estudiante:")
        self.grade_student_label.grid(column=0, row=1, padx=10, pady=10)
        self.grade_student_combobox = ttk.Combobox(self.grade_tab)
        self.grade_student_combobox.grid(column=1, row=1, padx=10, pady=10)

        # Grade Entry
        self.grade_label = ttk.Label(self.grade_tab, text="Nota:")
        self.grade_label.grid(column=0, row=2, padx=10, pady=10)
        self.grade_entry = ttk.Entry(self.grade_tab)
        self.grade_entry.grid(column=1, row=2, padx=10, pady=10)

        # Register Grade Button
        self.register_grade_button = ttk.Button(self.grade_tab, text="Registrar Nota", command=self.register_grade)
        self.register_grade_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

    def setup_view_grades_tab(self):
        # Student Combobox for Viewing Grades
        self.view_grades_student_label = ttk.Label(self.view_grades_tab, text="Estudiante:")
        self.view_grades_student_label.grid(column=0, row=0, padx=10, pady=10)
        self.view_grades_student_combobox = ttk.Combobox(self.view_grades_tab)
        self.view_grades_student_combobox.grid(column=1, row=0, padx=10, pady=10)

        # View Grades Button
        self.view_grades_button = ttk.Button(self.view_grades_tab, text="Ver Notas", command=self.view_grades)
        self.view_grades_button.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

        # Grades Display
        self.grades_display = tk.Text(self.view_grades_tab, height=10, width=50, state='disabled')
        self.grades_display.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

    def setup_view_courses_tab(self):
        # Courses Display
        self.courses_display = tk.Text(self.view_courses_tab, height=20, width=50, state='disabled')
        self.courses_display.grid(column=0, row=0, padx=10, pady=10)

        # View Courses Button
        self.view_courses_button = ttk.Button(self.view_courses_tab, text="Ver Cursos", command=self.view_courses)
        self.view_courses_button.grid(column=0, row=1, padx=10, pady=10)

    def update_course_combobox(self):
        self.grade_course_combobox['values'] = [curso.nombre for curso in self.cursos]

    def update_student_combobox(self):
        student_names = [f"{estudiante.nombre} {estudiante.apellido}" for estudiante in self.estudiantes]
        self.grade_student_combobox['values'] = student_names
        self.view_grades_student_combobox['values'] = student_names

    def add_course(self):
        course_name = self.course_name_entry.get()
        professor_name = self.professor_name_entry.get()
        professor_lastname = self.professor_lastname_entry.get()
        course_schedule = self.course_schedule_entry.get()

        if not course_name or not professor_name or not professor_lastname or not course_schedule:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            dia, hora_inicio, hora_fin = course_schedule.split(',')
        except ValueError:
            messagebox.showerror("Error", "Formato de horario incorrecto. Use: Día, Hora Inicio, Hora Fin")
            return

        horario = Horario(dia.strip(), hora_inicio.strip(), hora_fin.strip())
        profesor = Profesor(professor_name, professor_lastname)
        curso = Curso(course_name, profesor, horario)

        self.cursos.append(curso)
        self.update_course_combobox()
        messagebox.showinfo("Éxito", "Curso añadido correctamente")

    def add_student(self):
        student_name = self.student_name_entry.get()
        student_lastname = self.student_lastname_entry.get()
        student_id = self.student_id_entry.get()

        if not student_name or not student_lastname or not student_id:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        estudiante = Estudiante(student_name, student_lastname, student_id)
        self.estudiantes.append(estudiante)
        self.update_student_combobox()
        messagebox.showinfo("Éxito", "Estudiante añadido correctamente")

    def register_grade(self):
        selected_course_name = self.grade_course_combobox.get()
        selected_student_name = self.grade_student_combobox.get()
        grade = self.grade_entry.get()

        if not selected_course_name or not selected_student_name or not grade:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        selected_course = next((curso for curso in self.cursos if curso.nombre == selected_course_name), None)
        selected_student = next((estudiante for estudiante in self.estudiantes if f"{estudiante.nombre} {estudiante.apellido}" == selected_student_name), None)

        if not selected_course or not selected_student:
            messagebox.showerror("Error", "Curso o Estudiante no encontrado")
            return

        evaluacion = Evaluacion(selected_course, selected_student, float(grade))
        self.evaluaciones.append(evaluacion)
        messagebox.showinfo("Éxito", "Nota registrada correctamente")

    def view_grades(self):
        selected_student_name = self.view_grades_student_combobox.get()

        if not selected_student_name:
            messagebox.showerror("Error", "Seleccione un estudiante")
            return

        selected_student = next((estudiante for estudiante in self.estudiantes if f"{estudiante.nombre} {estudiante.apellido}" == selected_student_name), None)

        if not selected_student:
            messagebox.showerror("Error", "Estudiante no encontrado")
            return

        self.grades_display.config(state='normal')
        self.grades_display.delete('1.0', tk.END)

        grades_text = f"Notas de {selected_student.nombre} {selected_student.apellido}:\n"
        for evaluacion in self.evaluaciones:
            if evaluacion.estudiante == selected_student:
                grades_text += f"Curso: {evaluacion.curso.nombre}, Nota: {evaluacion.nota}\n"

        self.grades_display.insert(tk.END, grades_text)
        self.grades_display.config(state='disabled')

    def view_courses(self):
        self.courses_display.config(state='normal')
        self.courses_display.delete('1.0', tk.END)

        if not self.cursos:
            self.courses_display.insert(tk.END, "No hay cursos registrados")
        else:
            courses_text = "Cursos Registrados:\n"
            for curso in self.cursos:
                courses_text += f"Nombre: {curso.nombre}, Profesor: {curso.profesor.nombre} {curso.profesor.apellido}, Horario: {curso.horario.dia} de {curso.horario.hora_inicio} a {curso.horario.hora_fin}\n"

        self.courses_display.insert(tk.END, courses_text)
        self.courses_display.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolApp(root)
    root.mainloop()
