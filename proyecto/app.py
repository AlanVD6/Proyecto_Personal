import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
sys.path.append(os.path.join(os.path.dirname(__file__), "generated"))

import streamlit as st
from lexer_runner import obtener_tokens
from parser_runner import parsear
from semantic_checker import verificar_semantica
from evaluator import ejecutar_consulta

st.set_page_config(page_title="Mini Compilador SQL", layout="wide")
st.title("Mini Compilador de Consultas SQL")

st.write("Escribe una consulta SQL simplificada. Ejemplo: `SELECT nombre, edad FROM estudiantes WHERE edad > 18`")

consulta = st.text_area("Consulta SQL", height=100)

if st.button("Compilar"):
    if not consulta.strip():
        st.warning("Escribe una consulta antes de compilar.")
    else:
        # Fase léxica
        st.subheader("1. Análisis léxico — Tokens")
        tokens = obtener_tokens(consulta)
        st.table(tokens)

        # Fase sintáctica
        st.subheader("2. Análisis sintáctico — AST")
        ast, errores_sintacticos = parsear(consulta)

        if errores_sintacticos:
            st.subheader("Errores")
            for err in errores_sintacticos:
                st.error(err)
        else:
            st.json(ast)

            # Fase semántica
            st.subheader("3. Análisis semántico")
            errores_semanticos = verificar_semantica(ast)

            if errores_semanticos:
                st.subheader("Errores")
                for err in errores_semanticos:
                    st.error(err)
            else:
                st.success("La consulta es semánticamente válida.")

                # Fase evaluación
                st.subheader("4. Resultado de la consulta")
                resultado = ejecutar_consulta(ast)
                st.table(resultado)