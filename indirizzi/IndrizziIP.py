def get_ip_class(ip_address):
    first_octet = int(ip_address.split('.')[0])

    if 1 <= first_octet <= 126:
        ip_class = 'Classe A'
    elif 128 <= first_octet <= 191:
        ip_class = 'Classe B'
    elif 192 <= first_octet <= 223:
        ip_class = 'Classe C'
    elif 224 <= first_octet <= 239:
        ip_class = 'Classe D (Multicast)'
    elif 240 <= first_octet <= 255:
        ip_class = 'Classe E (Riservato)'
    else:
        ip_class = 'Indirizzo IP non valido'

    binary_first_octet = bin(first_octet).lstrip('0b').zfill(8) 
    
    return ip_class, binary_first_octet

print("Inserisci l'indirizzo IP:")
ip_address = input()
ip_class, binary_first_octet = get_ip_class(ip_address)
print(f"L'indirizzo IP {ip_address} appartiene alla {ip_class}")
print(f"Primo ottetto in binario: {binary_first_octet}")
