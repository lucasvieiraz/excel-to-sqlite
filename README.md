📊 Excel to SQLite — Automação de Controle
🧠 Contexto

No meu trabalho, o controle de dados (como abastecimentos/controles internos) era feito inicialmente em planilhas físicas (papel).
Com o tempo, esse processo foi migrado para o Excel, o que já facilitou bastante a organização e os cálculos.

Porém, à medida que a quantidade de dados foi crescendo, surgiu a necessidade de:

Ter mais organização

Evitar erros manuais

Facilitar consultas e relatórios

Criar uma base sólida para automações

Foi então que surgiu a ideia deste projeto:
👉 Migrar o controle do Excel para um banco de dados SQLite usando Python.

🎯 Objetivo do Projeto

Automatizar o processo de:

Ler uma planilha Excel

Criar um banco de dados SQLite automaticamente

Criar uma tabela com base nos dados da planilha

Inserir todos os dados no banco

Preparar a base para consultas e relatórios futuros

⚙️ Como funciona

O script principal:

Lê o arquivo: Controle 2026.xlsx

Cria o banco: controle_2026.db

Cria a tabela: controle

Insere todos os dados automaticamente

Se a tabela já existir, ela é substituída

Ao final, o sistema exibe:

Banco de dados SQLite criado com sucesso!

🧰 Tecnologias utilizadas

Python

Pandas

SQLite3

Pytest (para testes automatizados)

GitHub Actions (CI)

🧪 Testes Automatizados

O projeto possui testes que:

Executam o script automaticamente

Verificam se ele roda sem erros

Verificam se o banco de dados foi criado corretamente

Esses testes rodam automaticamente usando GitHub Actions, ou seja:

✅ Toda vez que eu faço um push para o GitHub, o projeto é testado automaticamente.

Isso garante que:

O código continua funcionando

Nada quebre sem eu perceber

O projeto está sempre em um estado confiável

🤖 Integração Contínua (CI)

Este projeto utiliza GitHub Actions para:

Instalar as dependências

Rodar os testes com pytest

Validar automaticamente cada alteração enviada para o repositório

Isso simula um ambiente profissional de desenvolvimento.
