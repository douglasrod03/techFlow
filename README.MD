# TechFlow Solutions - Sistema Ágil de Gestão de Tarefas

## Objetivo do Projeto
Este repositório contém o desenvolvimento de um sistema web de gerenciamento de tarefas encomendado pela **TechFlow Solutions** para atender uma startup do setor de logística. O objetivo principal do software é fornecer uma plataforma onde a equipe possa acompanhar o fluxo de trabalho em tempo real, priorizar demandas críticas da logística e monitorar o desempenho operacional da equipe.

## Escopo Inicial
O escopo base do sistema abrange o desenvolvimento de um CRUD (Create, Read, Update, Delete) de tarefas. O software entregará as seguintes funcionalidades essenciais para a startup:
- **Create:** Criação de novos cartões de tarefas detalhando a demanda.
- **Read:** Visualização de todas as tarefas cadastradas em um formato de quadro.
- **Update:** Atualização do status de progresso das tarefas (ex: A Fazer, Em Progresso, Concluído).
- **Delete:** Exclusão de tarefas cadastradas incorretamente ou canceladas.

## Metodologia Ágil Adotada
Para garantir entregas contínuas e alinhamento com as necessidades do cliente, o projeto está sendo conduzido sob a metodologia **Kanban**. 
O fluxo de trabalho e o controle do backlog estão estruturados diretamente na aba *Projects* deste repositório, dividindo as atividades de desenvolvimento nas colunas **A Fazer**, **Em Progresso** e **Concluído**. Isso permite transparência total sobre o que está sendo desenvolvido no momento e evita gargalos na produção.

## Estrutura do Repositório e Execução
A arquitetura do projeto está dividida da seguinte forma:
- `/src`: Código-fonte principal da aplicação e rotas do CRUD.
- `/tests`: Scripts de testes automatizados para controle de qualidade.
- `/docs`: Documentação teórica e diagramas UML.

## ⚠️ Justificativa de Mudança de Escopo
Durante o ciclo de desenvolvimento, o cliente solicitou uma alteração de escopo: **A adição de um sistema de prioridades (Alta, Normal, Baixa) para as tarefas**. 
**Justificativa:** A startup de logística percebeu gargalos na operação porque a equipe não sabia quais demandas atacar primeiro. A adaptação ágil permitiu a inclusão rápida do campo "Prioridade" na estrutura da tarefa, sem interromper o fluxo de entregas.
