def criar_grafo():
    grafo_lista = {}
    return grafo_lista

def inserir_vertice(grafo, vertice):
    if vertice in grafo:
        print(f"O vértice {vertice} já está presente.")
    else:
        grafo[vertice] = []
        print(f"Vértice {vertice} inserido.")

def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem not in grafo:
        inserir_vertice(grafo, origem)

    if destino not in grafo:
        inserir_vertice(grafo, destino)

    if destino not in grafo[origem]:
        grafo[origem].append(destino)
        print(f"Aresta {origem} -> {destino} inserida.")
    else:
        print(f"Aresta {origem} -> {destino} já existe.")

    if nao_direcionado:
      if origem not in grafo[destino]:
        grafo[destino].append(origem)
        print(f"Aresta entre {origem} e {destino} inserida.")
    
def vizinhos(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]
    
    else:
        print(f"O vértice {vertice} não existe")
        return []

def listar_vizinhos(grafo, vertice):
    lista = vizinhos(grafo,vertice)

    if vertice in grafo:
        print(f"Vizinhos de {vertice}: {lista}")

def exibir_grafo(grafo):
    if not grafo:
        print("Grafo vazio.")

    else:
        for vertice in grafo:
            print(f"{vertice} -> {grafo[vertice]}")

def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem not in grafo:
        print(f"Vértice {origem} não encontrado no grafo.")
        return

    if destino in grafo[origem]:
        grafo[origem].remove(destino)
        print(f"Aresta ({origem} -> {destino}) removida.")
    else:
        print(f"Aresta ({origem} -> {destino}) não encontrada.")

    if nao_direcionado:
        if destino in grafo and origem in grafo[destino]:
            grafo[destino].remove(origem)
            print(f"Aresta ({destino} -> {origem}) removida.")
        elif destino in grafo:
            print(f"Aresta ({destino} -> {origem}) não encontrada.")

def remover_vertice(grafo, vertice):
    if vertice not in grafo:
        print(f"Vértice {vertice} não encontrado no grafo.")
        return
    
    else:
      for outro_vertice in list(grafo.keys()):
          if vertice in grafo[outro_vertice]:
              grafo[outro_vertice].remove(vertice)

      del grafo[vertice]

      print(f"Vértice {vertice} removido.")

def existe_aresta(grafo, origem, destino):
    if origem not in grafo:
        return False
    
    else:
      if destino in grafo[origem]:
        return True
      
      else:
        return False

def grau_vertices(grafo, nao_direcionado=False):
    graus = {}
    
    for vertice in grafo:
            graus[vertice] = [0, 0, 0]

    if nao_direcionado:
        for vertice in grafo:
            grau = len(grafo[vertice])
            graus[vertice] = [grau, grau, grau]

    else:
        for u in grafo:
            graus[u][0] = len(grafo[u]) 
            
            for v in grafo[u]: 
                if v in graus:
                    graus[v][1] += 1 
        
        for vertice in graus:
            graus[vertice][2] = graus[vertice][0] + graus[vertice][1]

    return graus

def percurso_valido(grafo, caminho):
    if len(caminho) < 2:
        return True
    
    for i in range(len(caminho)-1):
        origem = caminho[i]
        destino = caminho[i+1]

        if not existe_aresta(grafo,origem,destino):
            return False
      
    return True

def BFS_Padrao(grafo, vertice):  
    fila = []
    visitados = [] 

    if vertice not in grafo:
        print(f"Vértice inicial {vertice} não encontrado no grafo.")
        return visitados

    fila.append(vertice)  

    while fila:  
        visitado = fila.pop(0) 

        if visitado not in visitados:
            visitados.append(visitado) 
            vizinhos_do_visitado = vizinhos(grafo, visitado)

            if vizinhos_do_visitado:  
                for vizinho in vizinhos_do_visitado:
                    
                    if vizinho not in fila and vizinho not in visitados:
                        fila.append(vizinho)
                        
    return visitados 

def BFS_menor_caminho(grafo, origem, destino):
    if origem not in grafo or destino not in grafo:
        print("Vértice de origem ou destino não encontrado.")
        return [] 

    fila = []
    fila.append([origem]) 

    visitados = set()
    visitados.add(origem)

    while fila:
        caminho_atual = fila.pop(0)  
        vertice_atual = caminho_atual[-1]

        if vertice_atual == destino:
            return caminho_atual
        
        vizinhos_do_vertice = vizinhos(grafo, vertice_atual)

        if vizinhos_do_vertice:
            for vizinho in vizinhos_do_vertice:
                if vizinho not in visitados:
                    visitados.add(vizinho) 
                    novo_caminho = list(caminho_atual) 
                    novo_caminho.append(vizinho)     
                    fila.append(novo_caminho) 
    return []

def sair():
    print("Saindo...")
    exit()

def main():
    def menu(grafo, eh_nao_direcionado):
        while True:
            print("\nMenu")
            print("1 - Mostrar o Grafo")
            print("2 - Inserir vértice")
            print("3 - Inserir aresta")
            print("4 - Remover vértice")
            print("5 - Remover aresta")
            print("6 - Listar vizinhos")
            print("7 - Grau dos vértices")
            print("8 - Percurso válido")
            print("9 - Busca em Largura Padrão")
            print("10 - Busca em Largura para encontrar Menor Caminho")
            print("0 - Sair")

            escolha = input("Escolha uma opção: ").strip()

            if escolha == "1":
                exibir_grafo(grafo)

            elif escolha == "2":
                vertice = input("Digite o nome do vértice a ser inserido: ").strip()
                inserir_vertice(grafo, vertice)

            elif escolha == "3":
                origem = input("Digite o vértice de origem: ").strip()
                destino = input("Digite o vértice de destino: ").strip()
                inserir_aresta(grafo, origem, destino, nao_direcionado=eh_nao_direcionado)

            elif escolha == "4":
                vertice = input("Digite o nome do vértice a ser removido: ").strip()
                remover_vertice(grafo, vertice)

            elif escolha == "5":
                origem = input("Digite o vértice de origem da aresta a ser removida: ").strip()
                destino = input("Digite o vértice de destino da aresta a ser removida: ").strip()
                remover_aresta(grafo, origem, destino, nao_direcionado=eh_nao_direcionado)

            elif escolha == "6":
                vertice = input("Digite o nome do vértice para listar vizinhos: ").strip()
                listar_vizinhos(grafo, vertice)

            elif escolha == "7":
                graus = grau_vertices(grafo, nao_direcionado=eh_nao_direcionado)
                print("\nGrau dos Vértices (out, in, total):")
                
                for vertice, grau in graus.items():
                    print(f"{vertice}: {grau}")

            elif escolha == "8":
                caminho_str = input("Digite o caminho a ser verificado (vértices separados por espaço): ").strip()
                caminho = caminho_str.split()

                if percurso_valido(grafo, caminho):
                    print("O percurso é válido.")
                else:
                    print("O percurso não é válido.")

            elif escolha == "9":
                vertice_inicial = input("Digite o vértice inicial: ").strip()
                ordem_fila = BFS_Padrao(grafo, vertice_inicial) 
        
                if ordem_fila:
                    print(f"Ordem BFS: {ordem_fila}") 
            elif escolha == "10":
                vertice_inicial = input("Digite o vértice inicial: ").strip()
                vertice_destino = input("Digite o vértice destino: ").strip()
            
                menor_caminho = BFS_menor_caminho(grafo, vertice_inicial, vertice_destino) 
            
                if menor_caminho:
                    print(f"O menor caminho é: {menor_caminho}")
                else:
                    print(f"Não foi encontrado um caminho de {vertice_inicial} até {vertice_destino}.")

            elif escolha == "0":
                sair()
                break
          
            else:
                print("Opção inválida. Tente novamente.")

    grafo = criar_grafo()

    resposta = input("O grafo será Não-Direcionado? (s/n): ").strip().lower()
    if resposta == 's':
        eh_nao_direcionado = True
    else:
        eh_nao_direcionado = False
    menu(grafo, eh_nao_direcionado)

if __name__ == "__main__":
    main()