edad_profesor=40

def encriptar_url(url):
    # Función de encriptación
    encriptada = ""
    for i in range(len(url)):
        # Primer condicional
        encriptada += chr(ord(url[i]) + (i % 3) + 1)
    
    # URL encriptada para ser desencriptada después
    print(f"URL encriptada: {encriptada}")
    return encriptada

def desencriptar_url(url_encriptada, clave):
    # Verificar si la clave es igual a la edad del profesor
    if clave !=edad_profesor:
        print("Clave incorrecta. No se puede desencriptar.")
        return None
    
    # Si la clave es correcta, se desencripta
    desencriptada = ""
    for i in range(len(url_encriptada)):
        # La operación inversa a la realizada en la encriptación
        desencriptada += chr(ord(url_encriptada[i]) - (i % 3) - 1)
    
    return desencriptada

# URL
url_original = "https://github.com/mattzarate333"
url_encriptada = encriptar_url(url_original)

# Para desencriptar el mensaje, el usuario debe introducir el año del profesor como clave:
clave = int(input("Introduce la clave para desencriptar el mensaje: "))
url_desencriptada = desencriptar_url(url_encriptada, clave)

if url_desencriptada:
    print(f"URL desencriptada: {url_desencriptada}")
