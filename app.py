import platform
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
 rc('font', family='NanumGothic')
# 스트림릿 앱 생성
st.title("데이터 프로파일링 실습")
# 파일 업로드 위젯
uploaded_file = st.file_uploader("데이터 파일 업로드", type=["csv","xlsx"])
if uploaded_file is not None:
 # 업로드한 파일을 DataFrame 으로 변환
 df = pd.read_csv(uploaded_file) # 엑셀 파일일 경우 pd.read_excel 사용

 # 데이터 프로파일링
 st.header("데이터 미리보기")
 st.write(df.head())
 st.header("기본 정보")
 st.write("행 수:", df.shape[0])
 st.write("열 수:", df.shape[1])
 st.header("누락된 값")
 missing_data = df.isnull().sum()
 st.write(missing_data)
 st.header("중복된 행 수")
 duplicated_rows = df.duplicated().sum()
 st.write(duplicated_rows)
 st.header("수치형 데이터 기술 통계량")
 numerical_stats = df.describe()
 st.write(numerical_stats)
 st.header("이상치 탐지 (상자 그림)")
 plt.figure(figsize=(10, 6))
 plt.boxplot(df.select_dtypes(include=['number']).values)
 plt.xticks(range(1, len(df.columns) + 1), df.columns, rotation=45)
 plt.title("Outlier detection (box plot)")
 st.pyplot(plt)
 st.header("데이터 분포 시각화")
 column_to_plot = st.selectbox("열 선택", df.columns)
 plt.figure(figsize=(10, 6))
 plt.hist(df[column_to_plot], bins=20, edgecolor='k')
 plt.xlabel(column_to_plot)
 plt.ylabel("빈도")
 plt.title(f"{column_to_plot} Data Distribution")
 st.pyplot(plt)
