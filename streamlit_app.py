import streamlit as st

st.set_page_config(
    page_title='Antonio Moura',
    layout='centered'
)

st.markdown("<h1 style='text-align: center; color: darkviolet;'>Antonio Moura</h1>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: justify;'>
Cientista de Dados com experiência em desenvolver soluções de ponta a ponta, desde a análise exploratória e modelagem preditiva até a implementação de aplicações interativas. Habilidade em transformar dados complexos em insights acionáveis, utilizando ferramentas como Python, Pandas, Scikit-learn e Streamlit para criar modelos de machine learning robustos e visualizações de dados impactantes. Buscando aplicar meu conhecimento para resolver problemas de negócios desafiadores e impulsionar a tomada de decisões baseada em dados.
</div>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: darkviolet;'>Areas de Experiência</h2>", unsafe_allow_html=True)

col21, col22 = st.columns(2)

col21.markdown("<h3 style='text-align: center; color: violet;'>Habilidades</h3>", unsafe_allow_html=True)
col22.markdown("<h3 style='text-align: center; color: violet;'>Ferramentas</h3>", unsafe_allow_html=True)

c421 = col21.container(height=380, border=True)
c422 = col22.container(height=380, border=True)

c421.markdown('\nProgramação, R\n\n---\nModelagem de Dados\n\n---\nAprendizagem de Maquina\n\n---\nVisualização de Dados\n\n---\nAplicações\n\n')
c422.markdown('\nPython, R\n\n---\nPandas, Numpy\n\n---\nScykit, Statsmodels, Regressão(ridge, Lasso)\n\n---\nMatplotlib, Seaborn\n\n---\nStreamlit\n\n')

st.markdown("<h2 style='text-align: center; color: darkviolet;'>Projetos</h2>", unsafe_allow_html=True)

col31, col32 = st.columns(2)

project_container_height = 400

c531 = col31.container(height=project_container_height, border=True)
c532 = col32.container(height=project_container_height, border=True)

c531.markdown("<h5 style='text-align: center; color: violet;'>Previsão de Renda</h5>", unsafe_allow_html=True)
c531.markdown("Este projeto utiliza a metodologia CRISP-DM para desenvolver um modelo de previsão de renda de clientes. A análise e a modelagem são realizadas em um Jupyter Notebook, e a solução final é apresentada em uma aplicação interativa com Streamlit.")
c531.markdown("---")
c531.markdown("<h6>Tecnologias Utilizadas:</h6>", unsafe_allow_html=True)
c531.markdown("- Python, Pandas, Scikit-learn, Streamlit")
col31.link_button('Ver no GitHub', 'https://github.com/0ace-jk/previsao_renda', use_container_width=True)

c532.markdown("<h5 style='text-align: center; color: violet;'>Credit-Score</h5>", unsafe_allow_html=True)
c532.markdown("Este projeto foi desenvolvido como um exercício didático para o curso da EBAC, com o objetivo de aplicar técnicas de machine learning para prever a inadimplência de clientes com base em seus dados.")
c532.markdown("---")
c532.markdown("<h6>Tecnologias Utilizadas:</h6>", unsafe_allow_html=True)
c532.markdown("- Python, Pandas, Seaborn, Matplotlib, Scikit-learn")
col32.link_button('Ver no GitHub', 'https://github.com/0ace-jk/Credit-Score', use_container_width=True)

st.markdown('# :rainbow[O futuro é orientado por dados. E começa hoje!]')

st.markdown('[Linkedin](https://www.linkedin.com/in/antoniomourajr/)')
st.markdown('[Kaggle](https://www.kaggle.com/antoniojunior1998)')
st.markdown('[GitHub](https://github.com/0ace-jk)')
