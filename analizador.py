# Contar intentos fallidos de login SSH

fallidos = 0  # contador de intentos fallidos

with open("auth.log", "r") as file:
    for linea in file:
        if "Failed password" in linea:
            fallidos += 1

print(f"Intentos fallidos de login: {fallidos}")


# Extraer las IPs de los intentos fallidos

ips_fallidas = {}

with open("auth.log", "r") as file:
    for linea in file:
        if "Failed password" in linea:
            partes = linea.split()
            ip = partes[10]  
            if ip not in ips_fallidas:
                ips_fallidas[ip] = 1
            else:
                ips_fallidas[ip] += 1

print("IPs atacantes y cantidad de intentos:")
for ip, cantidad in ips_fallidas.items():
    print(f"{ip}: {cantidad} intentos")


# Identificar la IP con más intentos (posible ataque de fuerza bruta)

if ips_fallidas:
    ip_agresiva = max(ips_fallidas, key=ips_fallidas.get)
    print("\nPosible ataque de fuerza bruta:")
    print(f"La IP más agresiva es {ip_agresiva} con {ips_fallidas[ip_agresiva]} intentos.")
else:
    print("No se encontraron intentos fallidos.")


# Contar 'invalid user'

usuarios_invalidos = {}

with open("auth.log", "r") as file:
    for linea in file:
        if "Invalid user" in linea:
            partes = linea.split()
            index_user = partes.index("user")
            usuario = partes[index_user + 1]  
            
            if usuario not in usuarios_invalidos:
                usuarios_invalidos[usuario] = 1
            else:
                usuarios_invalidos[usuario] += 1

print("\nUsuarios inválidos detectados:")
for usuario, cantidad in usuarios_invalidos.items():
    print(f"{usuario}: {cantidad} veces")



# Generar reporte final

with open("reporte_ssh.txt", "w") as reporte:
    reporte.write("REPORTE DE ANALISIS DE LOG SSH\n")
    reporte.write("-------------------------------\n\n")

    
    reporte.write(f"Intentos fallidos totales: {fallidos}\n\n")

    reporte.write("Intentos fallidos por IP:\n")
    for ip, cantidad in ips_fallidas.items():
        reporte.write(f"  {ip}: {cantidad} intentos\n")
    reporte.write("\n")
 
    if ips_fallidas:
        reporte.write(f"IP más agresiva: {ip_agresiva} ({ips_fallidas[ip_agresiva]} intentos)\n\n")

    reporte.write("Usuarios inválidos:\n")
    for usuario, cantidad in usuarios_invalidos.items():
        reporte.write(f"  {usuario}: {cantidad} apariciones\n")
