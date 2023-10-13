import openai 
import streamlit as st

# pip install streamlit-chat  
from streamlit_chat import message

openai.api_key = st.secrets["OPENAI_API_KEY"]
openai.api_base = st.secrets["OPENAI_API_BASE"]
openai.api_version = st.secrets["OPENAI_API_VERSION"]
openai.api_type = st.secrets["OPENAI_API_TYPE"]

def generate_response(prompt):
    response = openai.ChatCompletion.create(
      engine="dev-gpt-4",
      messages = [{"role": "user", "content": prompt}],
      temperature=0.05,
      max_tokens=800,
      top_p=0.95,
      frequency_penalty=0,
      presence_penalty=0,
      stop=None
    )
    return response.choices[0].message["content"]

#Creating the chatbot interface
st.title("chatBot : Streamlit + openAI")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# We will get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = generate_response(user_input)
    # store the output 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')