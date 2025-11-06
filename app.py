import streamlit as st

# --- Initialize session state for queue ---
if "queue" not in st.session_state:
    st.session_state.queue = []
if "length_of_queue" not in st.session_state:
    st.session_state.length_of_queue = 10

# --- Streamlit App Header ---
st.title("📝 TO-DO LIST APPLICATION (Using Queue)")
st.write("Manage your daily tasks interactively using this queue-based app!")

# --- Add a new task (enqueue) ---
st.subheader("➕ Add Task of the Day")
new_task = st.text_input("Enter the task for today:")

if st.button("Add Task"):
    if len(st.session_state.queue) < st.session_state.length_of_queue:
        if new_task.strip() != "":
            st.session_state.queue.append(new_task.strip())
            st.success(f"✅ Task added: '{new_task.strip()}'")
        else:
            st.warning("⚠️ Please enter a valid task before adding.")
    else:
        st.error("❌ Today's to-do list is full (maximum 10 tasks).")

# --- Show all tasks (peek) ---
st.subheader("📋 Today's Tasks")
if len(st.session_state.queue) == 0:
    st.info("There are no tasks right now for the day.")
else:
    for i, task in enumerate(st.session_state.queue, start=1):
        st.write(f"{i}. {task}")

# --- Mark a task as done (dequeue) ---
st.subheader("✅ Mark Task as Done")
if len(st.session_state.queue) == 0:
    st.write("No tasks available to mark as done.")
else:
    task_number = st.number_input("Enter the task number to mark as done:", min_value=1, max_value=len(st.session_state.queue), step=1)
    if st.button("Mark as Done"):
        st.session_state.queue.pop(task_number - 1)
        st.success("🎯 Successfully marked as done!")

# --- Delete all tasks ---
st.subheader("🗑️ Delete All Tasks")
if len(st.session_state.queue) == 0:
    st.write("No tasks to delete.")
else:
    if st.button("Delete All"):
        st.session_state.queue.clear()
        st.success("🧹 All tasks have been successfully deleted!")

# --- Footer ---
st.markdown("---")
st.caption("Thank you for using the To-Do List Application! Made with ❤️ using Streamlit.")
