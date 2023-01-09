import streamlit as st
import pandas as pd
import plotly_express as px

st.title('特定医療費受給者証の所持者数')

master_df = pd.read_excel(r"C:\Users\yshio\Documents\Sandbox\Python\RareDisease\koufu.xlsx", sheet_name=0, index_col=0)
year_list=master_df['年度'].unique()
disease_list = master_df['疾患名'].unique()

year_selected=st.sidebar.selectbox(
    '確認したい年度を選択下さい',
    year_list
    )

disease_selected = st.sidebar.selectbox(
    '確認したい疾患名を選択下さい',
    disease_list
    )

st.write(disease_selected, 'の', year_selected,'年度末時点における受給者証保持者数')

df = master_df[(master_df['年度']==year_selected) & (master_df['疾患名']==disease_selected)]
df = df.iloc[:,4:13] #年齢帯データのみを抽出
st.dataframe(df)

df = df.T #グラフ描画用に行列変換
st.write(
    px.bar(df),
    showlegend="False"
)

st.write(disease_selected, 'の受給者証保持者数の年次推移')

chart_df=master_df[master_df['疾患名']==disease_selected]
chart_df=chart_df.iloc[:,[2,4,5,6,7,8,9,10,11,12]]
chart_df= chart_df.sort_values(by="年度",ascending=True)
chart_df = chart_df.set_index("年度")
st.write(
    px.bar(chart_df,
    color_discrete_sequence=px.colors.qualitative.Vivid
    )
)
st.write('Datasource:https://www.nanbyou.or.jp/entry/5354')