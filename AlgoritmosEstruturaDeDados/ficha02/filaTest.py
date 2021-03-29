# Custom queue implementation in Python
class Queue:
 
    # 2.1. Crie uma estrutura de dados tipo “fila”
    def __init__(self, size):
        self.q =self.items = []     # Lista para armazenar os elementos da fila
        self.capacidade = size        # max capacidade da fila
        self.primeiro = 0              # pontos da frente para o elemento da frente na fila
        self.ultimo = -1              # "ultimo" aponta para o último elemento da fila
        self.total = 0              # tamanho atual da fila
    
    # 2.2. Crie uma função para ver se a “fila” está vazia
    # Funcao que retorna o tamanho da fila
    def size(self):
        return self.total
    # ver se a “fila” está vazia
    def isEmpty(self):
        return self.size() == 0
    
    # 2.3. Crie uma função para adicionar um elemento na “fila”
    # Funcao que checa se a fila está cheia
    def isFull(self):
        return self.size() == self.capacidade

    def append(self, value):
        # check for queue overflow
        if self.isFull():
            print("Overflow!! Terminating process.")
            exit(1)
 
        print("Inserting element…", value)
 
        self.ultimo = (self.ultimo + 1) % self.capacidade
        self.q[self.ultimo] = value
        self.total = self.total + 1
 
 
    # 2.4. Crie uma função para retirar o PRIMEIRO elemento na “fila”
    def pop(self):
        # checa se haverá underflow
        if self.isEmpty():
            print("Underflow!! Processo terminado.")
            exit(1)
 
        print("Removendo elemento…", self.q[self.primeiro])
 
        self.primeiro = (self.primeiro + 1) % self.capacidade
        self.total = self.total - 1
    # 2.5. Crie uma função para listar todos os elementos da “fila” 
    
    def display(self):
        print("Elementos da fila: ", self.q)

    # 2.6. Crie uma função para testar se um determinado valor,
    #  passado por parâmetro, está na “fila”
    def find(self, target):
        encontrado = False
        for items in self.q:
            if items is target:                
                print("Item encontrado na pilha")
                encontrado = True                                           
        if encontrado == False:     
            print("Item não encontrado na pilha")
    
    # Retorna o elemento da frente da pilha
    def peek(self):
        if self.isEmpty():
            print("Queue UnderFlow!! Terminating process.")
            exit(1)
 
        return self.q[self.primeiro]

 
if __name__ == '__main__':
 
    # Cria uma fila com capacidade de 5
    q = Queue(5)
 
    q.append(5)
    q.append(2)
    q.append(3)
 
    print("O tamanho da fila é", q.size())   
    q.pop()  
    print("O elemento da frente é ", q.peek())    
  
    if q.isEmpty():
        print("A fila está vazia")
    else:
        print("A fila não está vazia")