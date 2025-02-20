CREATE DATABASE papelaria;

USE papelaria;

CREATE TABLE Livros(
	id_livro INT AUTO_INCREMENT PRIMARY KEY,
    liv_titulo VARCHAR(50) NOT NULL,
    liv_ISBN INT NOT NULL,
    liv_edicao VARCHAR(50) NOT NULL,
    liv_editora VARCHAR(50) NOT NULL,
    liv_ano__publicacao INT NOT NULL,
    liv_preco_da_capa FLOAT NOT NULL,
    liv_categoria VARCHAR(50) NOT NULL,
    liv_quant INT NOT NULL
    
);

CREATE TABLE Autores(
	id_autores INT AUTO_INCREMENT PRIMARY KEY,
    aut_nome VARCHAR(75),
    aut_nacionalidade VARCHAR(20),
    aut_biografia VARCHAR(50)
);

CREATE TABLE Estoque(
	id_livro INT NOT NULL,
    est_entrada DATE NOT NULL,
    est_saida DATE NOT NULL
);

CREATE TABLE Vendas (
    id_venda INT AUTO_INCREMENT PRIMARY KEY,
    id_livro INT NOT NULL,
    quantidade_vendida INT NOT NULL,
    data_venda DATE NOT NULL,
    valor_total FLOAT NOT NULL,
    CONSTRAINT fk_id_livros FOREIGN KEY (id_livro) REFERENCES Livros(id_livro)
);

ALTER TABLE Estoque
ADD CONSTRAINT fk_id_livro FOREIGN KEY (id_livro) REFERENCES Livros(id_livro);