import pandas as pd
import streamlit as st
import numpy as np

def dataframe_with_selections(df):
    df_with_selections = df.copy()
    df_with_selections.insert(0, "Select", False)

    # Get dataframe row-selections from user with st.data_editor
    edited_df = st.data_editor(
        df_with_selections,
        hide_index=True,
        column_config={"Select": st.column_config.CheckboxColumn(required=True)},
        disabled=df.columns,
    )

    # Filter the dataframe using the temporary column, then drop the column
    selected_rows = edited_df[edited_df.Select]
    return selected_rows.drop('Select', axis=1)

def sessionStateCallback(name):
    st.session_state[name] = True

def custom_object_list_to_df(object_list):
    attributeList = []
    for i in dir(object_list[0]):
        if "__" not in i and not callable(getattr(object_list[0], i)):
            attributeList.append(i)
    objectListDic = []
    for o in object_list:
        objectDic = {}
        for a in attributeList:
            objectDic[a] = getattr(o, a)
        objectListDic.append(objectDic)
    df = pd.DataFrame(objectListDic)
    return df
