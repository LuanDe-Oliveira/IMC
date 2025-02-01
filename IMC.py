import streamlit as st
st.title("CALCULO DO :red[*IMC*]")
st.subheader("O :red[*IMC*] é uma forma de avaliar se uma pessoa está com o peso ideal, abaixo do peso, acima do peso ou :red[OBESA].")
st.markdown("---")


peso = st.number_input(label = "Insira seu :red[peso](kg):", placeholder="ex:68.23")
altura = st.number_input(label = "Insira sua :red[altura]:", placeholder="ex:1.70")

st.markdown("---")

imc = float(peso/(altura**2))
imc = round(imc,2)

if st.button(":red[CONFIRMAR]"):
    st.markdown("---")

    st.subheader(f"O valor do seu :red[IMC] é: {imc}")
    if imc <= 18.5:
        st.subheader("Muito magro, está :red[abaixo do peso]")
        st.image("./python/magreloso.webp", caption = 'Slk capa de grilo')
    elif 18.5 < imc <= 24.9:
        st.subheader(":red[Excelente], está no peso ideal")
        st.image("./python/NO Hype.jpg", caption = 'Fortão, grandão, gostosão')
    elif 25 <= imc <= 29.9:
        st.subheader("Cuidado, está :red[acima do peso]")
        st.image("./python/quase gordo.jpg", caption = 'abre o zóio fio')
    elif 30 <= imc <= 34.9:
        st.subheader("CUIDADO! Você tem :red[obesidade grau 1]")
        st.image("./python/gordo.jpg", caption = 'bora pa academia fiote')
    elif 35 <= imc <= 39.9:
        st.subheader("CUIDADO! Você tem :red[obesidade grau 2]")
        st.image("./python/gordão.jpg", caption = 'Selokoo fi, academia ja n da mais')
    elif imc > 40:
        st.subheader(":red[EMAGRECIMENTO URGENTE, PROCURE UM MÉDICO, VOCÊ TEM OBESIDADE GRAU 3]")
        st.image("./python/THAISO CARLO.webp", caption = 'MERMÃO BORA FAZER UMA DIETA')