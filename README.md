# Projeto usando Streamlit para fazer consultas e alteraçoes simples em SQL

Este projeto é um sistema de consulta e alteração de regras, desenvolvido usando Streamlit e SQL Server.

## Requisitos

- Python 3.7 ou superior
- Streamlit
- pyodbc
- pandas

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/twister-sistema.git
    cd twister-sistema
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Execute a aplicação Streamlit:
    ```sh
    streamlit run Main.py
    ```

2. Acesse a aplicação no seu navegador em `http://localhost:8501`.

## Estrutura do Projeto

- `Main.py`: Arquivo principal que contém a lógica da aplicação Streamlit.
- `Sql.py`: Contém funções para interagir com o banco de dados SQL Server.
- `Tabelas_Twister.py`: Contém dicionários de mapeamento para tabelas e IDs.

## Funcionalidades

### Consulta de Regras de Férias

- Selecione uma tabela para consultar as regras de férias.
- Visualize os dados da tabela selecionada.

### Alteração de Regras de Férias

- Selecione uma tabela e um analista para atualizar o status de férias.
- Atualize o status de férias do analista selecionado.

### Consulta de Logs

- Selecione uma tabela de logs para visualizar.
- Visualize os registros de logs da tabela selecionada realizando filtrod de ID, assunto e data.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Faça o push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.