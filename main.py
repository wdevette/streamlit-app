import streamlit as st
import pandas as pd

#st.text('Ola, DEUS te ama.')

st.set_page_config(page_title='Finanças', page_icon='💰')

st.markdown('''
# Boas Vindas!
            
## Nosso App de Financas
            
Espero que esteja gostando e curtindo a experiencia da solucao para organizacao fincanceiras.

''')

#Importacao/upload de arquivo/dados
file_upload = st.file_uploader(label='Faca o upload dos dados aqui.', type=['csv'])

#Verifca se foi feito upload de algum arquivo
if file_upload:

    #Leitura dos dados
    df = pd.read_csv(file_upload)
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y').dt.date

    #Exibicao dos dados
    exp1 = st.expander("Dados Brutos")
    columns_fmt = {"Valor":st.column_config.NumberColumn("Valor", format="R$ %.2f")}
    exp1.dataframe(df, hide_index=True, column_config=columns_fmt)

    #Visão institucional
    exp2 = st.expander("Instituições")
    df_instituiao = df.pivot_table(index='Data', columns='Instituição', values='Valor')

    #Abas para diferentes visualizações
    tab_data, tab_histoty, tab_share = exp2.tabs(["Dados", "Histórico", "Distribuição"])

    #Exubi DataFrame
    with tab_data:
        st.dataframe(df_instituiao)

    #Exibe histórico
    with tab_histoty:
        st.line_chart(df_instituiao)

    #Exibe distribuição
    with tab_share:

        #Filtro de datas
        date = st.selectbox("Filtro de Datas", options=df_instituiao.index)

        #Gráfico de distribuição 
        st.bar_chart(df_instituiao.loc[date])

    # with tab_share:
    #     #obtenção da última data de dados
    #     last_dt = df_instituiao.sort_index().iloc[-1]
    #     st.bar_chart(last_dt)
    
    
    # with tab_share:
    #     #Criando a possibilidade se escolher a data
    #     date = st.date_input("Data para distribuição: ",
    #                          min_value=df_instituiao.index.min(),
    #                          max_value=df_instituiao.index.max())
    #     if date not in df_instituiao.index:
    #         st.warning("Escolha uma data válida.")
    #     else:
    #         st.bar_chart(df_instituiao.loc[date])
        