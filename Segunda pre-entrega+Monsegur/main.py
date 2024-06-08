import clientes

cliente1 = clientes.Cliente(1, "Juan", "Perez", "juan.perez@gmail.com")
cliente2 = clientes.Cliente(2, "María", "García", "maria.garcia@gmail.com")

print(cliente1) 
cliente1.actualizar_email("juan.perez2@gmail.com")
print(cliente1) 

cliente2.agregar_compra("Celular", 500)
cliente2.agregar_compra("Camisa", 30)
