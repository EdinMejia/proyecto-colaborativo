def calcular_vuelto(precio, cantidad_recibida):
  # Calcula el vuelto restando el precio del producto del dinero recibido
  vuelto = cantidad_recibida - precio
  return vuelto


def desglosar_cambio(vuelto):
  # Lista de los diferentes tipos de billetes y monedas disponibles en el pais
  billetes = [200, 100, 50, 20, 10, 5, 1, 0.50, 0.25, 0.10, 0.05]
  desglose = {
  }  # Para almacenar la cantidad de cada billete o moneda en el vuelto

  # Itera sobre cada billete o moneda para determinar su cantidad en el vuelto
  for billete in billetes:
    # Calcula la cantidad de billetes o monedas necesarios para el vuelto
    cantidad = int(vuelto // billete)
    if cantidad > 0:
      # Si la cantidad es mayor que cero, agrega el billete o moneda al desglose
      desglose[billete] = cantidad
    # Actualiza el valor del vuelto restante después de considerar un billete o moneda
    vuelto %= billete

  return desglose

#PARTE DEL COLABORADOR 

# completar el mensaje de bienvenida y las respectivas instrucciones de que tiene que hacer el usuario

# se tiene que agregar el precio del producto y la cantidad con la que paga el usuario

# tambien se tiene que mostrar el cambio por devolver al usuario

# se tiene que mostrar el desglose del cambio en monedas y billetes cuantas moneas y billetes se devuelven
