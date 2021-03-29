class Pilha:
    #__init__ inicializa uma nova pilha vazia
    def __init__(self):
        #1.1. Crie uma estrutura de dados tipo “pilha”
        self.pilha = []

    #1.2. Crie uma função para ver se a “pilha” está vazia
    def vazia(self):
        return self.pilha == []

    #1.3. Crie uma função para adicionar um elemento na “pilha”
    def inserir(self, item):
        self.pilha.append(item)

    #1.4. Crie uma função para retirar o último elemento na “pilha”
    def excluir(self):
        return self.pilha.pop()

    # 1.5. Crie uma função para listar todos os elementos da “pilha”
    def mostrar(self):
        print(self.pilha)

    # 1.6. Crie uma função para testar se um determinado valor,
    # passado por parâmetro, está na “pilha”
    def procurar(self, alvo):
        encontrado = False
        for pilha in self.pilha:
            if pilha is alvo:                
                print("Item", alvo, "encontrado na pilha")
                encontrado = True                                           
        if encontrado == False:     
            print("Item", alvo, "não encontrado na pilha")

    # 1.7. Crie uma função para ordenar uma “pilha” por ordem crescente ou decrescente (tipo de ordenação passado por parâmetro)
    def ordenar(self, ordenacao):
        if ordenacao == "crescente":
            print("Pilha ordenada em ordem crescente")
            return self.pilha.sort()
        if ordenacao == "decrescente":
            print("Pilha ordenada em ordem decrescente")
            return self.pilha.reverse()


pilha = Pilha()
print(pilha.vazia())
pilha.inserir(4)
pilha.inserir(6)
pilha.inserir(7)
pilha.inserir(8)
pilha.excluir()
pilha.mostrar()
pilha.procurar(9)

pilha.ordenar("crescente")
pilha.mostrar()
pilha.ordenar("decrescente")
pilha.mostrar()
