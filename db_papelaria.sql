CREATE DATABASE Papelaria;

USE Papelaria;

-- Tabela de Autores
CREATE TABLE autores (
    id_autor INT AUTO_INCREMENT PRIMARY KEY,
    nome_completo VARCHAR(255) NOT NULL,
    nacionalidade VARCHAR(100),
    biografia TEXT
);

-- Tabela de Livros
CREATE TABLE livros (
    id_livro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    edicao VARCHAR(50),
    editora VARCHAR(255),
    ano_publicacao YEAR,
    preco_capa DECIMAL(10,2),
    categoria VARCHAR(100)
);

-- Tabela de Relacionamento entre Livros e Autores (M:N)
CREATE TABLE livro_autor (
    id_livro INT,
    id_autor INT,
    PRIMARY KEY (id_livro, id_autor),
    FOREIGN KEY (id_livro) REFERENCES livros(id_livro) ON DELETE CASCADE,
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor) ON DELETE CASCADE
);

-- Tabela de Controle de Estoque
CREATE TABLE estoque (
    id_estoque INT AUTO_INCREMENT PRIMARY KEY,
    id_livro INT NOT NULL,
    tipo_movimento ENUM('entrada', 'saida') NOT NULL,
    quantidade INT NOT NULL DEFAULT 0,
    data_movimento DATE NOT NULL,
    FOREIGN KEY (id_livro) REFERENCES livros(id_livro) ON DELETE CASCADE
);
