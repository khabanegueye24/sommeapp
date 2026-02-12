#Écrire un programme qui saisit deux notes d’un étudiant calcul et affiche la moyenne des notes.

import streamlit as st 
num1 =  st.input_number(" num1 : ")
num2 =  st.input_number(" num2 : ")
somme = num1 + num2

if st.button("résultat"):
  st.info( somme )
  
