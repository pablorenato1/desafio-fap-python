create schema sistema_de_gerenciamento;

-- Criação da tabela 'empregados' (para fins de referência)
CREATE TABLE `empregados` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `id_supervisor` int,
  PRIMARY KEY (`id`)
);

-- Criação da tabela 'tarefas'
CREATE TABLE `tarefas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `descricao` text NOT NULL,
  `id_empregado` int,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`id_empregado`) REFERENCES `empregados` (`id`)
);

-- Inserção de empregados
INSERT INTO empregados (nome) VALUES ('João');
INSERT INTO empregados (nome) VALUES ('Maria');

-- Inserção de tarefas
INSERT INTO tarefas (descricao, id_empregado) VALUES ('Revisar relatório financeiro', 1);
INSERT INTO tarefas (descricao, id_empregado) VALUES ('Enviar email de follow-up', 2);
INSERT INTO tarefas (descricao, id_empregado) VALUES ('Preparar apresentação de vendas', 1);
INSERT INTO tarefas (descricao, id_empregado) VALUES ('Atualizar planilha de orçamento', 2);
INSERT INTO tarefas (descricao, id_empregado) VALUES ('Revisar contrato com fornecedor', 1);
INSERT INTO tarefas (descricao, id_empregado) VALUES ('Agendar reunião de equipe', 2);
INSERT INTO tarefas (descricao, id_empregado) VALUES ('Elaborar proposta comercial', 1);
INSERT INTO tarefas (descricao, id_empregado) VALUES ('Analisar métricas de marketing', 2);
INSERT INTO tarefas (descricao, id_empregado) VALUES ('Preparar agenda para conferência', 1);
INSERT INTO tarefas (descricao) VALUES ('Atualizar base de dados de clientes');
INSERT INTO tarefas (descricao, id_empregado) VALUES ('Criar conteúdo para redes sociais', 1);
INSERT INTO tarefas (descricao, id_empregado) VALUES ('Realizar pesquisa de mercado', 2);
INSERT INTO tarefas (descricao) VALUES ('Treinar novos funcionários');
INSERT INTO tarefas (descricao, id_empregado) VALUES ('Conduzir entrevistas de emprego', 2);
INSERT INTO tarefas (descricao, id_empregado) VALUES ('Organizar evento corporativo', 1);
INSERT INTO tarefas (descricao, id_empregado) VALUES ('Desenvolver estratégia de vendas', 2);
INSERT INTO tarefas (descricao) VALUES ('Criar campanha publicitária');
INSERT INTO tarefas (descricao, id_empregado) VALUES ('Coordenar lançamento de produto', 2);
INSERT INTO tarefas (descricao, id_empregado) VALUES ('Resolver problemas de suporte ao cliente', 1);
INSERT INTO tarefas (descricao, id_empregado) VALUES ('Realizar manutenção de sistemas', 2);
/**/

