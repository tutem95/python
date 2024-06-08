def registrar_usuario():

  nombre_usuario = input("Ingrese su nombre de usuario: ").lower()
  contrasena = input("Ingrese su contraseña: ")

  if nombre_usuario in usuarios:
    print("El nombre de usuario ya existe. Intente nuevamente.")
    return

  usuarios[nombre_usuario] = contrasena
  print(f"Usuario '{nombre_usuario}' registrado con exito!")


def iniciar_sesion():

  nombre_usuario = input("Ingrese su nombre de usuario: ").lower()
  contrasena_ingresada = input("Ingrese su contraseña: ")

  if nombre_usuario not in usuarios:
    print("Usuario no encontrado. Intente nuevamente.")
    return

  contrasena_correcta = usuarios[nombre_usuario] == contrasena_ingresada
  if contrasena_correcta:
    print(f"Bienvenido/a {nombre_usuario}! Ha iniciado sesión correctamente.")
  else:
    print("Contraseña incorrecta. Intente nuevamente.")


def mostrar_usuarios():

  if not usuarios:
    print("No hay usuarios registrados.")
    return

  print("\nUsuarios registrados:")
  for usuario, contrasena in usuarios.items():
    print(f"- {usuario} / {contrasena}")


usuarios = {}


# Indice - Menu principal - Lo que ve el usuario
while True:
  print("\nMenu principal") 
  print("1. Registrarse")
  print("2. Iniciar sesión")
  print("3. Mostrar usuarios")
  print("4. Salir")

  opcion = input("Seleccione una opcion: ")

  if opcion == "1":
    registrar_usuario()
  elif opcion == "2":
    iniciar_sesion()
  elif opcion == "3":
    mostrar_usuarios()
  elif opcion == "4":
    print("Hasta luego!")
    break
  else:
    print("Opcion no valida. Intente nuevamente.")