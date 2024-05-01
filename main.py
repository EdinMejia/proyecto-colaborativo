def calcular_vuelto(precio, cantidad_recibida):
 vuelto = cantidad_recibida - precio
 return vuelto

def desglosar_cambio(vuelto): 
  billetes = [200, 100, 50, 20, 10, 5, 1, 0.50, 0.25, 0.10, 0.05]
  desglose = {}
  
  for billete in billetes:
      cantidad = int(vuelto // billete)
      if cantidad > 0:
           desglose[billete] = cantidad
      vuelto %= billete

  return desglose
  
# completar el mensaje de bienvenida y las respectivas instrucciones de que tiene que hacer el usuario

# se tiene que agregar el precio del producto y la cantidad con la que paga el usuario

# tambien se tiene que mostrar el cambio por devolver al usuario

# se tiene que mostrar el desglose del cambio en monedas y billetes cuantas moneas y billetes se devuelven