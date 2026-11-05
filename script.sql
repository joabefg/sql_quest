-- 1.: Se cadastrar como aventureiro (com guilda e classe válida)
-- 2.: O Rei irá lhe entregar um item aleatório (pode ser algo bom ou não >:^D)
-- 3.: Escolher uma quest (verificar se ele tem o nível e item requerido)
	-- Cada quest dropa um item, sorteado ou fixo (itens lendários).
-- 4.: Repetir até conseguir os requisitos para fazer a fase final do Boss que requer:
    -- A espada lendária
    -- Uma fada
    -- Um escudo
    -- Um cavalo
-- 5.: Ao derrotar o Boss Final a filha do Rei será salva.
CREATE DATABASE RPG;
USE RPG;

CREATE TABLE classe (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100)
);

-- não esquecer de adicionar validação
-- add um select para ver se a guilda que ele está tentando inserir está com o estado CONTRATANDO
CREATE TABLE guilda (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    estado VARCHAR(25) -- CONTRATANDO, FECHADA
);
    

CREATE TABLE item (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    raridade INT -- 0 A 10, vai servir como porcentagem no sorteio, 0 para itens lendários
);

CREATE TABLE quest (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(25),
    descricao VARCHAR(255),
    nivel_requerido INT,
    item_requerido INT,
    item_dropado INT,
    FOREIGN KEY (item_requerido)
		REFERENCES item(id)
);

CREATE TABLE aventureiro (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) UNIQUE NOT NULL,
    nivel INT, -- DEIXA ELE ESCOLHER, MAS COLOCA 1 NO FINAL hehe... easter egg
    classe_fk INT,
    guilda_fk INT,
    quest_fk INT,
    FOREIGN KEY (classe_fk) 
		REFERENCES classe(id),
	FOREIGN KEY (guilda_fk)
		REFERENCES guilda(id),
	FOREIGN KEY (quest_fk)
		REFERENCES quest(id)
);

CREATE TABLE inventario (
	id INT PRIMARY KEY AUTO_INCREMENT,
    -- estado? talvez futuramente: QUEBRADO, EVOLUÍDO, NORMAL
    item_fk INT,
    aventureiro_fk INT,
    FOREIGN KEY (item_fk)
		REFERENCES item(id),
	FOREIGN KEY (aventureiro_fk)
		REFERENCES aventureiro(id)
);

CREATE TABLE inimigo (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    nivel INT
);

-- POPULANDO
INSERT INTO classe VALUES 
(DEFAULT, 'Guerreiro'),
(DEFAULT, 'Mago'),
(DEFAULT, 'Arqueiro');

INSERT INTO guilda VALUES 
(DEFAULT, 'Guilda dos Heróis', 'CONTRATANDO'),
(DEFAULT, 'Guilda dos Forasteiros', 'CONTRATANDO'),
(DEFAULT, 'Guilda dos Mercenários', 'FECHADA');

INSERT INTO inimigo VALUES 
(DEFAULT, 'Gárgula', 5),
(DEFAULT, 'Bruxa', 7),
(DEFAULT, 'Cérberus', 10),
(DEFAULT, 'Hydra', 9),
(DEFAULT, 'Zumbi', 1),
(DEFAULT, 'Mago corrompido', 20);

