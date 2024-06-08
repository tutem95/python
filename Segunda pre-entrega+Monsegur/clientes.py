class Cliente:

    def __init__(self, id_cliente, nombre, apellido, email):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido} (ID: {self.id_cliente}) - Email: {self.email}"

    def actualizar_email(self, nuevo_email):
        self.email = nuevo_email

    def agregar_compra(self, producto, precio):
        print(f"El cliente {self.nombre} {self.apellido} ha comprado {producto} por {precio}")
        
