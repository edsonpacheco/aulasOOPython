def fatorial(n):
    # CASO BASE: Impede a recursão infinita
    if n <= 1:
        return 1
    
    # CASO RECURSIVO: A função chama a si mesma
    return n * fatorial(n - 1)

def main():
    numero = 5
    resultado = fatorial(numero)
    print(f"Fatorial de {numero} é {resultado}")
    # O Python não sofrerá overflow aqui
    print(f"Fatorial de 50: {fatorial(50)}")

if __name__ == "__main__":
    main()
