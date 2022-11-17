# Rocketbot Logs
  
Módulo para enviar registros a Rocketbot Orchestrator y alertas a los correos electrónicos configurados en el proceso  

*Read this in other languages: [English](Manual_RocketLog.md), [Español](Manual_RocketLog.es.md)*
  
![banner](imgs/Banner_rocketlog.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



## Descripción de los comandos

### Login NOC
  
Login NOC
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta Archivo .ini|Ruta Archivo .ini del NOC|C:/Users/User/Desktop/archivo.ini|

### Enviar log
  
Enviar log personalizado
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Token del proceso|Token del proceso que se desea enviar el log|8YWUW8AXAV3UPNKY|
|Mensaje|Mensaje que se desea enviar|Log personalizado|

### Enviar Alerta
  
Envia un alerta al email configurado en el proceso
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Token del proceso|Token del proceso que se desea enviar la alerta|8YWUW8AXAV3UPNKY|
|Mensaje de alerta|Mensaje que se desea enviar en la alerta|Alerta!|
