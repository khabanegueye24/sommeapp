#Écrire un programme qui saisit deux notes d’un étudiant calcul et affiche la moyenne des notes.

import streamlit as st 
num1 =  st.number_input(" num1 : ")
num2 =  st.number_input(" num2 : ")
somme = num1 + num2

if st.button("résultat"):
  st.info( somme )
  

