import streamlit as st
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# CSV 데이터 불러오기
df = pd.read_csv("Nvidia_stock_data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df = df[['Date', 'Close']].dropna().sort_values('Date')

# Prophet 형식에 맞게 컬럼명 변경
df_prophet = df.rename(columns={'Date': 'ds', 'Close': 'y'})

# 앱 타이틀
st.title("📈 NVIDIA 주가 시계열 예측")
st.caption("Prophet 시계열 모델로 향후 4년간의 주가를 예측합니다.")

# Prophet 모델 정의 및 학습
model = Prophet(daily_seasonality=True)
model.fit(df_prophet)

# 미래 4년치 데이터 생성 및 예측
future = model.make_future_dataframe(periods=365 * 4)
forecast = model.predict(future)

# 라인 그래프 출력
st.subheader("🔮 예측 주가 추이")
fig1 = model.plot(forecast)
st.pyplot(fig1)

# 구성 요소 추세 그래프 출력
st.subheader("📊 추세 및 시즌 성분")
fig2 = model.plot_components(forecast)
st.pyplot(fig2)

# 예측 데이터 일부 표시
st.subheader("📄 예측 데이터 (일부)")
st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(20))
