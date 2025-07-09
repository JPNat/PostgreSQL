CREATE SCHEMA IF NOT EXISTS mydb;
SET search_path TO mydb;

CREATE TABLE IF NOT EXISTS usuario
(
    email        VARCHAR(45)    NOT NULL,
    nome         VARCHAR(45)    NOT NULL,
    telefone     VARCHAR(15)[]  NOT NULL,
    credito      NUMERIC(10, 2) NOT NULL,
    senha        VARCHAR(45)    NOT NULL,
    tipo_usuario INT            NOT NULL,
    PRIMARY KEY (email)
);

CREATE TABLE IF NOT EXISTS pessoa_fisica
(
    usuario_email VARCHAR(45) PRIMARY KEY,
    cpf           VARCHAR(45) NOT NULL,
    cargo         VARCHAR(45) NOT NULL,
    FOREIGN KEY (usuario_email)
        REFERENCES usuario (email)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS pessoa_juridica
(
    usuario_email VARCHAR(45) NOT NULL,
    cnpj          VARCHAR(45) NOT NULL,
    PRIMARY KEY (usuario_email),
    FOREIGN KEY (usuario_email)
        REFERENCES usuario (email)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);


CREATE TABLE IF NOT EXISTS pagamento
(
    id             SERIAL PRIMARY KEY,
    status         VARCHAR(45) NOT NULL,
    numero_extrato VARCHAR(10) NOT NULL,
    data_inicial   TIMESTAMP   NOT NULL,
    data_pago      TIMESTAMP
);

CREATE TABLE IF NOT EXISTS produto
(
    id           SERIAL         NOT NULL PRIMARY KEY,
    preco        NUMERIC(10, 2) NOT NULL,
    extras       VARCHAR(45),
    nome         VARCHAR(45)    NOT NULL,
    estoque      INT            NOT NULL,
    tipo_produto INT            NOT NULL,
    dono         VARCHAR(45),
    FOREIGN KEY (dono)
        REFERENCES usuario (email)
);

CREATE TABLE IF NOT EXISTS transacao
(
    id              SERIAL PRIMARY KEY,
    status          VARCHAR(45) NOT NULL,
    produto_id      INT         NOT NULL,
    comprador_email VARCHAR(45) NOT NULL,
    vendedor_email  VARCHAR(45) NOT NULL,
    pagamento_id    INT         NOT NULL,
    FOREIGN KEY (pagamento_id)
        REFERENCES pagamento (id),
    FOREIGN KEY (comprador_email)
        REFERENCES usuario (email),
    FOREIGN KEY (vendedor_email)
        REFERENCES usuario (email),
    FOREIGN KEY (produto_id)
        REFERENCES produto (id)
);

CREATE TABLE IF NOT EXISTS feedback
(
    numero_feedback  INT         NOT NULL,
    comentario       TEXT,
    nota             INT         NOT NULL,
    transacao_id     INT         NOT NULL,
    usuario_avaliado VARCHAR(45) NOT NULL,
    PRIMARY KEY (numero_feedback, transacao_id),
    FOREIGN KEY (transacao_id)
        REFERENCES transacao (id),
    FOREIGN KEY (usuario_avaliado)
        REFERENCES usuario (email)
);

CREATE TABLE IF NOT EXISTS carteira_digital
(
    usuario_email    VARCHAR(45) NOT NULL,
    bandeira         VARCHAR(20) NOT NULL,
    numero_cartao    VARCHAR(16) NOT NULL,
    codigo_seguranca VARCHAR(3)  NOT NULL,
    PRIMARY KEY (usuario_email),
    FOREIGN KEY (usuario_email)
        REFERENCES usuario (email)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS endereco
(
    id            SERIAL,
    usuario_email VARCHAR(45) NOT NULL,
    numero        VARCHAR(4)  NOT NULL,
    cep           VARCHAR(8)  NOT NULL,
    complemento   VARCHAR(45) NOT NULL,
    estado        VARCHAR(45) NOT NULL,
    cidade        VARCHAR(45) NOT NULL,
    rua           VARCHAR(45) NOT NULL,
    PRIMARY KEY (id, usuario_email),
    FOREIGN KEY (usuario_email)
        REFERENCES usuario (email)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);


CREATE TABLE IF NOT EXISTS folhas
(
    produto_id INT NOT NULL PRIMARY KEY,
    capacidade INT NOT NULL,
    FOREIGN KEY (produto_id)
        REFERENCES produto (id)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS fichario
(
    produto_id INT            NOT NULL PRIMARY KEY,
    proporcao  VARCHAR(5)     NOT NULL,
    argola     DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (produto_id)
        REFERENCES produto (id)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS deckbox
(
    produto_id INT         NOT NULL PRIMARY KEY,
    material   VARCHAR(45) NOT NULL,
    capacidade INT         NOT NULL,
    FOREIGN KEY (produto_id)
        REFERENCES produto (id)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS playmat
(
    produto_id INT         NOT NULL PRIMARY KEY,
    skin       VARCHAR(15) NOT NULL,
    borda      DECIMAL (10, 2)    NOT NULL,
    tamanho    VARCHAR(10) NOT NULL,
    FOREIGN KEY (produto_id)
        REFERENCES produto (id)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS sleeves
(
    produto_id INT         NOT NULL PRIMARY KEY,
    tamanho    VARCHAR(20) NOT NULL,
    textura    VARCHAR(30) NOT NULL,
    FOREIGN KEY (produto_id)
        REFERENCES produto (id)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS marcadores
(
    produto_id INT NOT NULL PRIMARY KEY,
    tipo VARCHAR(45) NOT NULL,
    FOREIGN KEY (produto_id)
        REFERENCES produto (id)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS cartas
(
    produto_id  INT         NOT NULL PRIMARY KEY,
    raridade    VARCHAR(15) NOT NULL,
    edicao      VARCHAR(45) NOT NULL,
    conservacao VARCHAR(20) NOT NULL,
    idioma      VARCHAR(20) NOT NULL,
    FOREIGN KEY (produto_id)
        REFERENCES produto (id)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS oferta
(
    pessoa_juridica_email VARCHAR(45),
    produto_id            INT,
    PRIMARY KEY (pessoa_juridica_email, produto_id),
    FOREIGN KEY (pessoa_juridica_email)
        REFERENCES pessoa_juridica (usuario_email)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION,
    FOREIGN KEY (produto_id)
        REFERENCES produto (id)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS compra
(
    produto_id   INT         NOT NULL,
    pagamento_id INT         NOT NULL,
    comprador    VARCHAR(45) NOT NULL,
    PRIMARY KEY (produto_id),
    FOREIGN KEY (produto_id)
        REFERENCES produto (id),
    FOREIGN KEY (pagamento_id)
        REFERENCES pagamento (id),
    FOREIGN KEY (comprador)
        REFERENCES usuario (email)
);
