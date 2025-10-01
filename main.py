from funcoes import contar_palavra_na_frase

def main():
    frase = input("Digite uma frase: ")
    palavra = input("Digite uma palavra para buscar: ")
    
    quantidade = contar_palavra_na_frase(frase, palavra)
    
    print(f"A palavra '{palavra}' aparece {quantidade} vez(es) na frase.")

if __name__ == "__main__":
    main()
