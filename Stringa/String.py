
def stampa(s: str) -> str:
    return s

def length(s: str) -> int:
    return len(s)

def revStringa(s: str) -> str:
    return ''.join(reversed(s))

def onecharUpper(s: str) -> str:
    return s.title()

def vocali(s: str) -> int:
    return sum(1 for char in s if char in "aeiou")


    
s=input("inserisci una stringa\n")
while True:
    
    print("1) Stampa la stringa")
    print("2) Lunghezza stringa")
    print("3) Stringa al contrario")
    print("4) Prime lettere maiuscole")
    print("5) Vocali")
    print("6) Esci")
    print()
    scelta = input("Scegli un'opzione: ")
    print()

    if scelta == '1':
       
        print(stampa(s))
    elif scelta == '2':
        
        print(length(s))
    elif scelta == '3':
       
        print(revStringa(s))
    elif scelta == '4':
        
        print(onecharUpper(s))
    elif scelta == '5':
        
        print(vocali(s))
    elif scelta == '6':
        break
    else:
        print("Input errato riprova.")
