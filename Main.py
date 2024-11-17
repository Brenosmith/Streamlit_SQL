import streamlit as st
from Sql import fetch_table_data, update_table_data
from Tabelas_Twister import tabelas_twister_dict, tabelas_log_dict, id_twisters_dict

if 'page' not in st.session_state:
    st.session_state.page = 'Consulta Regras'

def consulta_regras():
    # Initialize session state variables
    if 'tabela_selecionada' not in st.session_state:
        st.session_state.tabela_selecionada = None
    if 'df_atual' not in st.session_state:
        st.session_state.df_atual = None

    st.title('Consulta de Regras de Férias')
    st.write('Aqui você pode consultar as regras de férias.')

    # Parte de consulta de tabela
    # st.session_state.tabela_selecionada = st.selectbox('Consulta Regras:', tabelas_twister_dict.keys()) 
    st.session_state.tabela_selecionada = st.selectbox('Consulta Regras:', [""] + list(tabelas_twister_dict.keys())) 
    st.write(f'Você selecionou {st.session_state.tabela_selecionada}')

    if st.button('Buscar'):
        if st.session_state.tabela_selecionada != "":
            # Create a table that shows the data from a DataFrame
            table_name = tabelas_twister_dict.get(st.session_state.tabela_selecionada)
            st.session_state.df_atual = fetch_table_data(table_name)

            st.write('Data from the table:')
            st.dataframe(st.session_state.df_atual)  # Adjust the height as needed
        else:
            st.write('Por favor, selecione um Twister.')

def consulta_distribuicao():
    # Initialize session state variables
    if 'tabela_selecionada' not in st.session_state:
        st.session_state.tabela_selecionada = None
    if 'df_atual' not in st.session_state:
        st.session_state.df_atual = None
    if 'id_twister' not in st.session_state:
        st.session_state.id_twister = None
    if 'assunto_email' not in st.session_state:
        st.session_state.assunto_email = ''
    if 'data_inicio' not in st.session_state:
        st.session_state.data_inicio = None
    if 'data_fim' not in st.session_state:
        st.session_state.data_fim = None

    filtro_query = ""

    st.title('Consulta de Distribuição de E-mails')
    st.write('Aqui você pode consultar a distribuição de e-mails.')

    # Parte de consulta de tabela
    st.session_state.tabela_selecionada = st.selectbox('Selecione um Twister:', [""] + list(tabelas_twister_dict.keys()))
    if st.session_state.tabela_selecionada != "":
        st.write(f'Você selecionou {st.session_state.tabela_selecionada}')
        st.session_state.id_twister = id_twisters_dict.get(st.session_state.tabela_selecionada)
        filtro_query = f"ID_TWISTER = '{st.session_state.id_twister}'"
    else:
        st.write('Por favor, selecione um Twister.')

    # Parte de consulta de e-mail
    if st.session_state.tabela_selecionada != "":
        # Selecionar parte do assunto do e-mail para buscar
        st.session_state.assunto_email = st.text_input('Assunto do e-mail (pode ser parcial)):', 'Assunto do e-mail')
        if st.session_state.assunto_email != 'Assunto do e-mail':
            st.write(f'Você digitou: {st.session_state.assunto_email}')
            filtro_query += f" AND ASSUNTO LIKE '%{st.session_state.assunto_email}%'"
        else:
            st.write('Por favor, escreva o assunto do e-mail.')

    # Parte de filtro de data
    if st.session_state.assunto_email != 'Assunto do e-mail':
        st.session_state.data_inicio = st.date_input('Data de início:', value=None, min_value=None, max_value=None)
        st.session_state.data_fim = st.date_input('Data de fim:', value=None, min_value=None, max_value=None)

        if st.session_state.data_inicio is not None and st.session_state.data_fim is not None:
            st.write(f'Você selecionou o período de {st.session_state.data_inicio} a {st.session_state.data_fim}')
            filtro_query += f" AND DATA_EMAIL BETWEEN '{st.session_state.data_inicio}' AND '{st.session_state.data_fim}'"
        else:
            st.write('Por favor, selecione um período.')

    # Parte de busca
    if st.session_state.data_inicio is not None and st.session_state.data_fim is not None:
        if st.button('Buscar'):
            if st.session_state.tabela_selecionada != "":
                # Create a table that shows the data from a DataFrame
                st.session_state.df_atual = fetch_table_data(tabelas_log_dict.get("Log Geral"), filtro_query)

                st.write('Data from the table:')
                st.dataframe(st.session_state.df_atual)
            else:
                st.write('Por favor, selecione um Twister.')

def alteracao_ferias():
    # Initialize session state variables
    if 'tabela_selecionada' not in st.session_state:
        st.session_state.tabela_selecionada = None
    if 'analista_selecionado' not in st.session_state:
        st.session_state.analista_selecionado = None
    if 'ferias_sim_nao' not in st.session_state:
        st.session_state.ferias_sim_nao = None
    if 'df_atual' not in st.session_state:
        st.session_state.df_atual = None

    st.title('Alteração de Regras de Férias')
    st.write('Aqui você pode atualizar o status de férias dos analistas.')
    
    st.session_state.tabela_selecionada = st.selectbox('Selecione um Twister:', [""] + list(tabelas_twister_dict.keys()))  
    st.write(f'Você selecionou {st.session_state.tabela_selecionada}')

    if st.session_state.tabela_selecionada != "":
        table_name = tabelas_twister_dict.get(st.session_state.tabela_selecionada)
        st.session_state.df_atual = fetch_table_data(table_name)
    else:
        st.session_state.df_atual = None

    # Parte de alteração de tabela
    if st.session_state.df_atual is not None:
        # Create a select box with result of function fetch_table_data filtering just ANALISTA column, no duplicates
        analistas = st.session_state.df_atual['ANALISTA'].unique()
        st.session_state.analista_selecionado = st.selectbox('Selecione o analista:', [""] + list(analistas))
        st.write(f'Você selecionou {st.session_state.analista_selecionado}')

        if st.session_state.analista_selecionado != "":
            st.session_state.ferias_sim_nao = st.selectbox('Status férias:', ["", 'SIM', 'NÃO'])
            st.write(f'Você selecionou {st.session_state.ferias_sim_nao}')
        else:
            st.session_state.ferias_sim_nao = ""

        if st.session_state.ferias_sim_nao != "":
            if st.button('Atualizar na tabela'):
                # Update the table with the selected data
                table_name = tabelas_twister_dict.get(st.session_state.tabela_selecionada)
                result = update_table_data(table_name, st.session_state.ferias_sim_nao, st.session_state.analista_selecionado)

                if result == "Success":
                    st.write('Tabela atualizada com sucesso!')
                else:
                    st.write(f'Erro: {result}')
    else:
        st.write('Por favor, selecione um Twister.')

# Page navigation
page = st.sidebar.selectbox('Selecione a página', 
                            ['Consulta Regras', 'Consulta Distribuição', 'Alteração Férias'], 
                            index=['Consulta Regras', 'Consulta Distribuição', 'Alteração Férias'].index(st.session_state.page))

if page == 'Consulta Regras':
    consulta_regras()
elif page == 'Alteração Férias':
    alteracao_ferias()
elif page == 'Consulta Distribuição':
    consulta_distribuicao()
else:
    st.write('Página não encontrada.')