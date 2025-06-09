#Teste de salvamento
def linha():
    print("--------------------------------------")
def inscrever_atleta(lista_de_inscritos):
    num = input("Numero de peito: ")
    nom = input("Nome: ")  
    cat = input("Categoria: ")
    se = input("Masculino ou femino? Por favor digitar M ou F: ")
    atleta = {'Numero de peito': num, 'Nome': nom,'Categoria': cat, 'Genero': se}
    lista_de_inscritos.append(atleta)
    linha()
    print("Atleta inscrito")
    linha()
def listar_atleta(lista_de_inscritos):
    if not inscritos:
        linha()  
        print("Nenhum atleta registrado")
        linha()
    else:
        linha()
        print("ATLETAS")
        linha()
        for corredor in inscritos:
            peito = corredor['Numero de peito']
            nome = corredor['Nome']
            ca = corredor['Categoria']
            s = corredor['Genero']
            print(f"{peito}: Nome: {nome} // Categoria: {ca} // Genero: {s}")
        linha()
        print("FIM DA LISTA")
        linha()
def buscar_atleta(lista_de_inscritos):
    numero_a_procurar = input("Insira o numero de peito que deseja procurar: ")  
    encontrado = False
    for atleta_atual in lista_de_inscritos: 
        if atleta_atual['Numero de peito'] == numero_a_procurar:
            linha()
            print("--- Atleta Encontrado! ---")
            linha()
            print(f"Peito: {atleta_atual['Numero de peito']}")
            print(f"Nome: {atleta_atual['Nome']}")
            print(f"Categoria: {atleta_atual['Categoria']}")
            print(f"Gênero: {atleta_atual['Genero']}")  
            linha()
            encontrado = True
            break
    if not encontrado:
        linha()
        print("Atleta com este número de peito não foi encontrado.")
        linha()
def remover_atleta(lista_de_inscritos):
    nn_remover = input("Digite o numero de peito do atleta que deseja remover:  ")  
    at_remover = None
    for atl_remover in inscritos:
        if atl_remover['Numero de peito'] == nn_remover:
            at_remover = atl_remover
            break
    if at_remover is not None:
        lista_de_inscritos.remove(at_remover)
        linha()
        print(F"O atleta de numero: {nn_remover} foi removido")
        linha()
    else:
        linha()
        print("Atleta não encontrado")
        linha()
inscritos = []
while True:
    comando = input("Menu: [Inscrever], [Listar], [Buscar], [Remover], [Sair] ").strip().lower()
    if comando == 'sair':
        print("Tchau")
        break
    elif comando == "inscrever":
        inscrever_atleta(inscritos)
    elif comando == 'listar':
        listar_atleta(inscritos)
    elif comando == 'buscar':
        buscar_atleta(inscritos)
    elif comando == 'remover':
        remover_atleta(inscritos)
    else:
        linha()
        linha()
        print("Comando não reconhecido.")
        linha()
        linha()