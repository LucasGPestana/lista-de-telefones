lista_telefones = dict()

def incluirNovoNome(nome_pessoa, telefones):

    lista_telefones[nome_pessoa] = telefones


def incluirTelefone(nome_pessoa, telefone):
    
    if lista_telefones.get(nome_pessoa) == None:
        
        resposta = input(f"Nome {nome_pessoa} não encontrado! Deseja incluir esse nome na lista de telefones(S/N)? ").upper()
        
        if resposta == 'S':
            incluirNovoNome(nome_pessoa, [telefone])

    else:
        
        telefones = lista_telefones.get(nome_pessoa)
        telefones.append(telefone)

        lista_telefones[nome_pessoa] = telefones

def excluirTelefone(nome_pessoa, telefone):
    
    if lista_telefones.get(nome_pessoa) == None:
        
        print("Nome não encontrado!")
    
    elif len(lista_telefones[nome_pessoa]) == 1:
        
        excluirNome(nome_pessoa)
    
    else:
        
        telefones = lista_telefones.get(nome_pessoa)
        telefones.remove(telefone)

        lista_telefones[nome_pessoa] = telefones

def excluirNome(nome_pessoa):
    
    if lista_telefones.get(nome_pessoa) == None:
        
        print("Nome não encontrado!")
    
    else:
        
        lista_telefones.pop(nome_pessoa)

if __name__ == "__main__":
    
    incluirNovoNome("Rafael", ["8888-8888", "9181-7161"])
    incluirNovoNome("Leonardo", ["1234-5678", "8765-4321"])
    incluirNovoNome("Donatello", ["2468-1012"])

    incluirTelefone("Michelangelo", "5555-5555")
    incluirTelefone("Donatello", "9090-9090")

    excluirTelefone("Leonardo", "8765-4321")
    excluirTelefone("Michelangelo", "5555-5555")
    excluirTelefone("Splinter", "4141-4141")

    excluirNome("Rafael")
    excluirNome("Destruidor")

    for nome, telefones in lista_telefones.items():
        print(nome, telefones)