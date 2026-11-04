# 📘 Tarefa: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Aprenda os fundamentos de APIs REST usando FastAPI. Você irá criar uma API para gerenciar tarefas, praticando rotas HTTP, validação de dados com modelos Pydantic e respostas apropriadas para cada operação.

## ⚙️ Preparação

- Tenha Python 3.10 ou superior instalado.
- Instale as dependências com `python -m pip install fastapi uvicorn`.
- Inicie o servidor na pasta da atividade com `python -m uvicorn main:app --reload`.
- Acesse `http://127.0.0.1:8000/docs` para testar a API pela documentação interativa do FastAPI.
- Use o arquivo `main.py` como ponto de partida. Os dados podem ficar em memória; não é necessário configurar um banco de dados.

## 📝 Tarefas

### 🛠️ Consultar tarefas

#### Descrição

Complete a API para que clientes possam consultar todas as tarefas ou buscar uma tarefa específica pelo seu ID. Use os modelos Pydantic e o armazenamento em memória fornecidos no código inicial.

#### Requisitos

A API concluída deve:

- Retornar a lista de tarefas em `GET /tasks`.
- Implementar `GET /tasks/{task_id}` para buscar uma tarefa pelo ID.
- Responder com status `404 Not Found` quando o ID solicitado não existir.

### 🛠️ Criar tarefas

#### Descrição

Adicione uma rota para criar tarefas. Cada tarefa deve ter um título e pode incluir uma descrição e indicar se está concluída.

#### Requisitos

A API concluída deve:

- Implementar `POST /tasks` e receber os dados no corpo da requisição.
- Validar os dados de entrada com o modelo Pydantic fornecido.
- Gerar um ID para cada tarefa e retornar a tarefa criada com status `201 Created`.

### 🛠️ Atualizar e remover tarefas

#### Descrição

Complete as operações de atualização e remoção, mantendo respostas consistentes quando uma tarefa não existir.

#### Requisitos

A API concluída deve:

- Implementar `PUT /tasks/{task_id}` para substituir os dados de uma tarefa existente.
- Implementar `DELETE /tasks/{task_id}` e retornar status `204 No Content` quando a remoção for bem-sucedida.
- Retornar status `404 Not Found` ao tentar atualizar ou remover um ID inexistente.
- Testar os fluxos de consulta, criação, atualização, remoção e erro pela página `/docs`.
