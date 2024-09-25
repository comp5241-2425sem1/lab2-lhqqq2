import streamlit as st
import llm,json
def generate_questions(topic, num_questions):
    system_prompt = f"you are proficient quiz generator."
    with open("prompt.txt", "r") as f:
        user_prompt = f.read()
    user_prompt = user_prompt.replace("{topic}", topic)
    user_prompt = user_prompt.replace("{num_questions}", str(num_questions))

    print("User prompt:")
    print(user_prompt)

    results = llm.answer(system_prompt, user_prompt)
    return results

with st.sidebar:
    topic = st.text_input("Enter the topic to generate questions:")
    num_questions = st.selectbox("Select number of questions to generate",[1,2,3])
    button = st.button("Generate Questions")

if button:
    results = generate_questions(topic, num_questions)
    print("LLM response:")
    print(results)

    st.markdown("## Generated Questions")
    results_dict = json.loads(results)
    for question in results_dict["question"]:
        question_text = question["question_text"]
        answer = question["answer"]
        st.write("*Question:*",question_text)

        with st.expander("Show Answer"):
            st.info(answer)