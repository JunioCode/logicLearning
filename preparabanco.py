import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='admin'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuário ou senha')
    else:
        print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `logiclearning`;")

cursor.execute("CREATE DATABASE `logiclearning`;")

cursor.execute("USE `logiclearning`;")

# criando tabelas



TABLES = {}

TABLES['emp_config'] = ('''
      CREATE TABLE `emp_config` (
      `id_emp` int(10) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `cnpj` varchar(50) NOT NULL,
      `telefone` varchar(15) NOT NULL,
      `dominio` varchar(40) NOT NULL,
      `cores` varchar(40) NOT NULL,
      PRIMARY KEY (`id_emp`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['usuario'] = ('''
      CREATE TABLE `usuario` (
      `id_usuario` int(10) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `email` varchar(50) NOT NULL,
      `senha` varchar(15) NOT NULL,
      `data_nascimento` date NOT NULL,
      `area` varchar(40) NOT NULL,
      `id_empresa` int(10) NOT NULL,
      `id_perfil` smallint NOT NULL,
      PRIMARY KEY (`id_usuario`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['cursos'] = ('''
      CREATE TABLE `cursos` (
      `id_curso` int(10) NOT NULL AUTO_INCREMENT,
      `nome_curso` varchar(50) NOT NULL,
      `descricao` varchar(100),
      `data_criação` date NOT NULL,
      PRIMARY KEY (`id_curso`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['perfil'] = ('''
      CREATE TABLE `perfil` (
      `id_perfil` int(10) NOT NULL AUTO_INCREMENT,
      `nome_perfil` varchar(50) NOT NULL,
      `detalhe` varchar(100),
      `edicao` int NOT NULL,
      `cadastro` int NOT NULL,
      `exclusão` int NOT NULL,
      PRIMARY KEY (`id_perfil`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['hist_curso_usuario'] = ('''
      CREATE TABLE `hist_curso_usuario` (
      `id_curso` int(10) NOT NULL AUTO_INCREMENT,
      `id_usuario` varchar(50) NOT NULL,
      `status` varchar(100),
      `certificado` varchar(100)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')


TABLES['emp_cursos'] = ('''
      CREATE TABLE `hist_curso_usuario` (
      `id_empresa` int(10) NOT NULL AUTO_INCREMENT,
      `id_curso` varchar(50) NOT NULL,
      `ativo` int(1)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')


TABLES['usuario'] = ('''
    ALTER TABLE 'usuario' (
    ADD CONSTRAINT FK_Usuario_1
    FOREIGN KEY(id_empresa) 
    REFERENCES emp_config(id_emp)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['usuario'] = ('''
    ALTER TABLE 'usuario' (
    ADD CONSTRAINT FK_Usuario_2
    FOREIGN KEY(id_perfil) 
    REFERENCES perfil(id_perfil)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['hist_curso_usuario'] = ('''
    ALTER TABLE 'hist_curso_usuario' (
    ADD CONSTRAINT Fk_usuario
    FOREIGN KEY(id_usuario) 
    REFERENCES usuario(id_usuario)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['hist_curso_usuario'] = ('''
    ALTER TABLE 'hist_curso_usuario' (
    ADD CONSTRAINT Fk_curso
    FOREIGN KEY(id_curso) 
    REFERENCES curso(id_curso)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['emp_cursos'] = ('''
    ALTER TABLE 'emp_curso' (
    ADD CONSTRAINT Fk_disponivel
    FOREIGN KEY(id_empresa) 
    REFERENCES emp_config(id_emp)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['emp_cursos'] = ('''
    ALTER TABLE 'emp_curso' (
    ADD CONSTRAINT Fk_disponivel_curso
    FOREIGN KEY(id_curso) 
    REFERENCES curso(id_curso)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')


# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()