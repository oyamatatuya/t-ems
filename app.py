import streamlit as st
st.title('アプリ')
st.caption('エネルギーマネジメントシステム')
st.subheader('T-epco,EMS Service')


demand_point=st.number_input('要求ポイント',0,100,1,1,None,'demand_point')
st.caption(f'あなたの現在ポイントは{demand_point}です')