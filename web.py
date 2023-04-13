import streamlit as st
import modules.functions as functions
#il comando per fare run di una web app è: --> streamlit run /home/lorenzo/pythonProjects/webapp_1/web.py

def add_item():
    item = st.session_state["key_new_item_on_text_input"] + "\n"
    items.append(item)
    functions.write_items(items)
    print(f"Ho dato ENTER sul nuovo item --> inserito item: {item}")
    item = ''

#WIDGET
st.title("Lista Spesa")
st.subheader("Lista di articoli")
st.text("\n Inserire qui sotto gli articoli da comprare."
        "\n Facendo Check su una cosa la si cancella")

verifica_item= functions.verify_if_exist_file()

items = functions.get_items()

##### CHECKBOX LIST
# Qui creo le checkbox a partire dagli elementi di items
# quindi un ciclo for gira su items e crea le check box
for item_index,item_value in enumerate(items):
    checkbox = st.checkbox(item_value,key=item_value)
    if checkbox:
        items.pop(item_index)
        functions.write_items(items)
        del st.session_state[item_value]
        st._rerun()

# VERIFICA SE ESISTE IL FILE items.txt altrimenti lo crea
verifica_item= functions.verify_if_exist_file()
print(verifica_item)

#### TEXT INPUT
st.text_input(label="  "
              , placeholder="Add new item.."
              ,on_change=add_item,key="key_new_item_on_text_input") #on_change è una funzione callback

print ("Hello")

st.subheader("Qui sotto posso vedere il st.session_state:")
st.text("è una sorta di dizionario ottimizzato con tutte le coppie \n key:value della sessione in quel momento")

st.session_state

