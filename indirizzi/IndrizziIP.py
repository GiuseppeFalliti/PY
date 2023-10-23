
def get_ip_class(ip_address):
    first_octet = int(ip_address.split('.')[0])

    if 1 <= first_octet <= 126:
        return 'Classe A'
    elif 128 <= first_octet <= 191:
        return 'Classe B'
    elif 192 <= first_octet <= 223:
        return 'Classe C'
    elif 224 <= first_octet <= 239:
        return 'Classe D (Multicast)'
    elif 240 <= first_octet <= 255:
        return 'Classe E (Riservato)'
    else:
        return 'Indirizzo IP non valido'

print("inserisci l'indizzo ip")
ip_address =input() 
ip_class = get_ip_class(ip_address)
print(f"L'indirizzo IP {ip_address} appartiene alla {ip_class}")
