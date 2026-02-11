from pytm import TM, Actor, Process, Dataflow, Datastore, Boundary

# CREATE MODEL 
name = "Web Api Authentication Threat Model"
description = "Threat Model para web api de autenticacion"
tm = TM(name=name)
tm.description = description

# DEFINIR LOS LIMITES DE CONFIANZA
limits = ["Internet", "Cloud", "Token"]

boundaries = {}

for limit in limits: 
    boundaries[limit] = Boundary(limit)

# DEFINIR ACTORES
client = Actor("Client")
client.inBoundary = boundaries["Internet"]

# PROCESOS 
web_api = Process("Web Api")
web_api.inBoundary = boundaries["Internet"]
engine_encrypted = Process("Engine_encrypted")
engine_encrypted.inBoundary = boundaries["Token"]



# ALMACENES DE DATOS 
database = Datastore("Database")
database.inBoundary = boundaries["Cloud"]
database.isSQL = True
database.hasWriteAccess = True
database.onAWS = True

# DEFINIR FLUJO DE DATOS
user_to_web_api = Dataflow(client, web_api, "Sign to platform")
user_to_web_api.protocol = "HTTPS"
user_to_web_api.controls.isEncrypted = True
user_to_web_api.controls.authenticatesSource = True
user_to_web_api.usesSessionTokens = True
user_to_web_api.order = 1

web_api_to_engine_encrypted = Dataflow(web_api, engine_encrypted, "Encrypt data")
web_api_to_engine_encrypted.protocol = "HTTPS"
web_api_to_engine_encrypted.controls.isEncrypted = True
web_api_to_engine_encrypted.controls.authenticatesSource = False

engine_encrypted_to_database = Dataflow(engine_encrypted, database, "Send data encrypted")
engine_encrypted_to_database.protocol = "HTTPS"
engine_encrypted_to_database.controls.isEncrypted = True
engine_encrypted_to_database.controls.authenticatesSource = True

web_api_to_user = Dataflow(web_api, client, "Response Data")
web_api_to_user.protocol = "HTTPS"
web_api_to_user.controls.isEncrypted = True
web_api_to_user.controls.authenticatesSource = True
web_api_to_user.usesSessionTokens = True
web_api_to_user.order = 2

tm.process()