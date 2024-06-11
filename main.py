import os
from modules.animales import Animales
from modules.rodeos import Rodeo
def menu_principal():
    '''Muestra el menú principal y retorna la opción seleccionada.'''
    print("\nMenú Principal:")
    print("1. Gestión de Rodeos")
    print("2. Gestión de Animales")
    print("3. Salir")

    opcion = int(input("Ingrese una opción: "))
    os.system("clear")
    return opcion
def gestion_rodeos():
  """Muestra las opciones de gestión de rodeos y retorna la opción seleccionada."""
  print("\nGestión de Rodeos:")
  print("1. Crear Rodeo")
  print("2. Modificar Rodeo")
  print("3. Eliminar Rodeo")
  print("4. Volver al menú principal")

  opcion = int(input("Ingrese una opción: "))
  return opcion

def gestion_animales():
  """Muestra las opciones de gestión de animales y retorna la opción seleccionada."""
  print("\nGestión de Animales:")
  print("1. Alta de Caravana")
  print("2. Registro de Peso")
  print("3. Baja de Caravana")
  print("4. Volver al menú principal")

  opcion = int(input("Ingrese una opción: "))
  return opcion

'''Ejecuta el menu'''
while True:
    opcion = menu_principal()
    if opcion == 1:
        opcion_getion_rodeos = gestion_rodeos()
        if opcion_getion_rodeos == 1:
            Rodeo().crear_rodeo()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
        elif opcion_getion_rodeos == 2:
            Rodeo().modificar_rodeo()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
        elif opcion_getion_rodeos == 3:
            Rodeo().eliminar_rodeo()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
        elif opcion_getion_rodeos == 4:
            os.system("clear")
            continue
        else:
            print("Opción inválida")
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
    elif opcion == 2:
        opcion_gestion_animales =  gestion_animales()
        if opcion_gestion_animales == 1:
            Animales().alta_caravana()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
        elif opcion_gestion_animales == 2:
            Animales().registro_peso()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
        elif opcion_gestion_animales == 3:
            Animales().baja_caravana()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
        elif opcion_gestion_animales == 4:
            os.system("clear")
            continue
        else:
            print("Opción inválida")
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
    elif opcion == 3:
        break
    else:
        print("Opción inválida")
        input("\nPresione ENTER para continuar")
        os.system("clear")
