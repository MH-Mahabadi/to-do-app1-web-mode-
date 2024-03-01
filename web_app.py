import streamlit as st
import Functions

todos = Functions.read_todos()


def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo.capitalize() + '\n')
    Functions.write_todos(todos)
    st.session_state['new_todo'] = ''


st.title("Welcome To To-do App")
st.subheader("Plan Everyday")
st.write("Choose to complete:")

for todo in todos:
    check = st.checkbox(todo, key=todo)
    if check:
        todos.remove(todo)
        Functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='', placeholder='Add new todo...',
              on_change=add_todo, key='new_todo')
