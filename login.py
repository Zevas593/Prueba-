from tkinter import *
from tkinter import simpledialog, messagebox
from pymongo import MongoClient

# Configuración de la conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['login']
users_collection = db['usuarios']

class GUI:
    def __init__(self):
        self.current_user = None
        self.root = Tk()
        self.root.title("Usuarios")

        self.create_widgets()

    def create_widgets(self):
        Label(self.root, text="LOGIN", font=("Helvetica", 20)).pack(pady=10)

        username_frame = Frame(self.root)
        username_frame.pack(pady=5)
        Label(username_frame, text="Usuario:").pack(side=LEFT, padx=5)
        self.username_entry = Entry(username_frame)
        self.username_entry.pack(side=LEFT)

        password_frame = Frame(self.root)
        password_frame.pack(pady=5)
        Label(password_frame, text="Contraseña:").pack(side=LEFT, padx=5)
        self.password_entry = Entry(password_frame, show='*')
        self.password_entry.pack(side=LEFT)

        Button(self.root, text="Guardar", command=self.save_user).pack(pady=5)
        Button(self.root, text="Salir", command=self.root.destroy).pack()

    def save_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username and password:
            if self.user_exists(username):
                self.display_message('El usuario ya existe. Intente con otro nombre de usuario.')
            else:
                user_id = self.create_user(username, password)
                self.current_user = {'_id': user_id, 'username': username, 'password': password}
                self.display_message('Usuario guardado correctamente.')
                self.clear_fields()
        else:
            self.display_message('Por favor, ingrese usuario y contraseña.')

    def create_user(self, username, password):
        user_data = {'username': username, 'password': password}
        result = users_collection.insert_one(user_data)
        return result.inserted_id

    def user_exists(self, username):
        return users_collection.find_one({'username': username}) is not None

    def display_message(self, message):
        messagebox.showinfo("Message", message)

    def clear_fields(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = GUI()
    gui.run()
