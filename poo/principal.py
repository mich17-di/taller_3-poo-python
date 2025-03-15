
from cliente import cliente 
from saludo import saludo

#*creo los obejtos 
objetocilente=cliente()
objetosaludo=saludo()
#***uso los metodos de los objetos**
objetocilente.tomar_datos()
aux_mensaje=objetosaludo.hacer_saludo_formal()
objetocilente.hacer_saludo(aux_mensaje)
