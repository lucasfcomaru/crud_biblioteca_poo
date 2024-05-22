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


# class Usuário:
#     def __init__(self):