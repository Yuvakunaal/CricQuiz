import streamlit as st
st.set_page_config(page_title = "Cricket Quiz",page_icon="🏏")

st.markdown('''
<style>
.st-emotion-cache-6q9sum
{
    visibility : hidden;
}
.st-emotion-cache-cio0dv
{
    visibility : hidden;
}
.st-emotion-cache-1wbqy5l
{
    visibility : hidden;
}
</style>
''',unsafe_allow_html=True)

#st.markdown("[Streamlit removing footer video](https://youtu.be/_b6nfGNcTdw?si=qyGuB2tqyKFVGf_J)")

#state1 = st.checkbox("This website looking good",value = False,key="check1")
#if st.session_state.check1 == True:
#    st.write("Thank you")

st.title("Cric Quiz")
marks = 0
radio_btn1 = st.radio("1. Who achieved 70+ centuries in his career ?",("Virat Kohli","Rohit Sharma","Shreyas iyer"),index=None,key="opt1")
radio_btn2 = st.radio("2. Who scored more than 500 sixers in his career ?",("Virat Kohli","Rohit Sharma","Shreyas iyer"),index=None,key="opt2")
radio_btn3 = st.radio("3. Who is the successfull captain amongst all ?",("M.S.Dhoni","K.L Rahul","Yuzvendra Chahal"),index=None,key="opt3")
radio_btn4 = st.radio("4. Who is known as Indian swing king bowler ?",("Jasprit Bumrah","David Warner","Bhuvneshwar Kumar"),index=None,key="opt4")
radio_btn5 = st.radio("5. When did India won a world cup after 2001 ?",(2007,2011,2019),index=None,key="opt5")
if st.session_state.opt1 == "Virat Kohli":
    marks+=1
if st.session_state.opt2 == "Rohit Sharma":
    marks+=1
if st.session_state.opt3 == "M.S.Dhoni":
    marks+=1
if st.session_state.opt4 == "Bhuvneshwar Kumar":
    marks+=1
if st.session_state.opt5 == 2011:
    marks+=1
a = st.button("Submit")
if a is True:
    st.write("Your score :",marks,"/",5)





