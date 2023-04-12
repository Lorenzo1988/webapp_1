import streamlit as st
import modules.functions as functions
#il comando per fare run di una web app è: --> streamlit run /home/lorenzo/pythonProjects/webapp_1/web.py

def add_item():
    item = st.session_state["new_item"] + "\n"
    items.append(item)
    functions.write_items(items)


#WIDGET
st.title("Lista Spesa")
st.subheader("Lista di articoli")
st.text("\n Inserire qui sotto gli articoli da comprare."
        "\n Facendo Check su una cosa la si cancella")

verifica_item= functions.verify_if_exist_file()

items = functions.get_items()

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

st.text_input(label=""
              , placeholder="Add new todo.."
              ,on_change=add_item,key="new_item")


print ("Hello")
st.session_state