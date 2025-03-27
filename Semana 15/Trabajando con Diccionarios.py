# Crea un diccionario llamado informacion_personal
informacion_personal = {"nombre":"Gabreiela", "edad":21, "ciudad": "Quito", "profesion":"contadora"}
# Accede al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente.
informacion_personal["ciudad"] = "cuenca"
# Agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona
informacion_personal["contadora"] = "especialidad"
# Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala con un número de teléfono ficticio.
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987842122"
# Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.
del informacion_personal["edad"]
# Imprime el diccionario resultante después de realizar todas las operaciones.
print(informacion_personal)
