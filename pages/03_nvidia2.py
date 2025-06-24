import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# CSV 로드
df = pd.read_csv("Nvidia_stock_data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df = df[['Date', 'Close']].dropna().sort_values('Date')

# 날짜를 숫자로 변환
df['Days'] = (df['Date'] - df['Date'].min()).dt.days

# 선형 회귀 모델 학습
X = df[['Days']]
y = df['Close']
model = LinearRegression()
model.fit(X, y)

# 미래 4년 예측 (365일 x 4년)
future_days = 365 * 4
last_day = df['Days'].max()
future_X = pd.DataFrame({'Days': np.arange(last_day + 1, last_day + future_days + 1)})
future_y = model.predict(future_X)

# 날짜로 복원
future_dates = df['Date'].max() + pd.to_timedelta(future_X['Days'] - last_day, unit='D')
future_df = pd.DataFrame({
    'Date': future_dates,
    'Predicted Close': future_y
})

# 기존 데이터와 예측 데이터 합치기
past_df = df[['Date', 'Close']].rename(columns={'Close': 'Predicted Close'})
combined_df = pd.concat([past_df, future_df], ignore_index=True)

# Streamlit UI 구성
st.title("🔮 NVIDIA 주가 예측 (향후 4년)")
st.caption("과거 데이터를 기반으로 선형 회귀로 예측한 NVIDIA 주가 추이")

# 선 그래프 출력
st.line_chart(data=combined_df.set_index('Date')['Predicted Close'])

# 데이터 일부 출력
st.markdown("### 📄 예측 포함 전체 데이터 (일부)")
st.dataframe(combined_df.tail(20))

