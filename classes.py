class Livro:
    def __init__(self,id, autor, nome_livro, editora, ano):
        self.id = id
        self.autor = autor
        self.nome_livro = nome_livro
        self.editora = editora
        self.ano = ano

    def add_livro(self):
        livro = {"ID":self.id,
                 "Autor":self.autor,
                 "Nome do livro":self.nome_livro,
                 "Editora":self.editora,
                 "Ano":self.ano}
        return livro

    def remove_livro(self, lista_livro, indice):
        self.lista_livro = lista_livro
        # O usuário não sabe que a contagem dos índices começam do zero
        self.indice = indice - 1

        if self.indice <= len(self.lista_livro):
            try:
                self.lista_livro.pop(self.indice)
            except:
                print("O índice não existe. Tente novamente.")
            else:
                print("Livro excluído com sucesso!")
                return self.lista_livro
        else:
            print("Índice não encontrado. Tente novamente.")