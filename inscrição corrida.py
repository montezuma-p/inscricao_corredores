inscritos = []
while True:
    comando = input("Menu: [inscrever], [listar], [sair], [buscar], [remover] ").strip().lower()
    if comando == 'sair':
        print("tchau")
        break
    elif comando == 'inscrever':
        num = input("Numero de peito: ")
        nom = input("Nome: ")
        cat = input("Categoria: ")
        se = input("Masculino ou femino? Por favor digitar M ou F: ")
        atleta = {'Numero de peito': num, 'Nome': nom,'Categoria': cat, 'genero': se}
        inscritos.append(atleta)
        print("Atleta inscrito")
    elif comando == 'listar':
        if not inscritos:
            print("Nenhum atleta registrado")
        else:
            print("__________ATLETAS__________")
            print(".")
            for corredor in inscritos:
                peito = corredor['Numero de peito']
                nome = corredor['Nome']
                ca = corredor['Categoria']
                s = corredor['genero']
                print(f"{peito}: Nome: {nome} // Categoria: {ca} // Genero: {s}")
            print('.')
            print("_____________FIM DA LISTA_______________")
    elif comando == 'buscar':
        numero_a_procurar = input("Insira o numero de peito que deseja procurar: ")
        encontrado = False
        for atleta_atual in inscritos: 
            if atleta_atual['Numero de peito'] == numero_a_procurar:
                print("--- Atleta Encontrado! ---")
                print(f"Peito: {atleta_atual['Numero de peito']}")
                print(f"Nome: {atleta_atual['Nome']}")
                print(f"Categoria: {atleta_atual['Categoria']}")
                print(f"Gênero: {atleta_atual['genero']}")
                encontrado = True
                break
        if not encontrado:
            print("Atleta com este número de peito não foi encontrado.")
    elif comando == 'remover':
        nn_remover = input("Digite o numero de peito do atleta que deseja remover:  ")
        at_remover = None
        for atl_remover in inscritos:
            if atl_remover['Numero de peito'] == nn_remover:
                at_remover = atl_remover
                break
        if at_remover is not None:
            inscritos.remove(at_remover)
            print(F"O atleta de numero: {nn_remover} foi removido")
        else:
            print("Atleta não encontrado")
    else:
        print("Comando não reconhecido")