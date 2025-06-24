import streamlit as st
import pandas as pd

# CSV 파일 경로
file_path = "Nvidia_stock_data.csv"

# 데이터 불러오기
df = pd.read_csv(file_path)

# 날짜 형식 변환
df['Date'] = pd.to_datetime(df['Date'])

# 페이지 기본 정보
st.title("📈 NVIDIA 주가 추이 시각화")
st.caption("CSV 데이터를 기반으로 NVIDIA의 주가 흐름을 확인할 수 있습니다.")

# 날짜 범위 선택
min_date = df['Date'].min()
max_date = df['Date'].max()
date_range = st.date_input("조회할 날짜 범위 선택", (min_date, max_date), min_value=min_date, max_value=max_date)

# 날짜 필터 적용
filtered_df = df[(df['Date'] >= pd.to_datetime(date_range[0])) & (df['Date'] <= pd.to_datetime(date_range[1]))]

# 선 그래프 출력
st.subheader("📊 종가(Close) 기준 주가 추이")
st.line_chart(filtered_df.set_index('Date')['Close'])

# 원본 데이터 일부 출력
st.markdown("---")
st.subheader("🗂️ 원본 데이터 (일부)")
st.dataframe(filtered_df.head(50))
