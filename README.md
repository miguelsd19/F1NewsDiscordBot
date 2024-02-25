
# F1 News discord Bot

Un bot hecho para tomar las noticias de f1 desde google, mostrando solo las primeras 5 y luego cerrandose, este script de momento solo manda el mensaje, no recibe respuestas ni nada mas, se puede desplegar en la lambda de aws donde se puede poner un trigger para que se active cada cierto tiempo, se necesita crear una app desde el sitio de discord para desarrollador y una app desde newsapi.org para la api de google. La url que se debe usar con google es de la siguiente forma (ejemplo en python):

### https://newsapi.org/v2/everything?q={}&from={}&sortBy={}&language={}&apiKey={}&pagesize={}

donde se espera que se llenen los parametros: 
- q = tema a buscar. 
- from = fecha de consulta. 
- sortBy = orden que se toma. 
- language = lenguaje de busqueda
- apiKey = key que obtines de google al crear la app
- pagesize = numero de datos que quieres obtener (default = 20, max = 100)

## Discord

Para la conexion de discord se ocupa:
- DISCORD_TOKEN: El token de acceso que se obtiene al crear la app en discord como desarrollador.
- CHANNEL_ID: El Id del canal al que se va usar.
- SERVER_ID = El id del servidor. 
