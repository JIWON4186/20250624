import streamlit as st
import pandas as pd

# CSV 파일 로드
file_path = "202505_202505_연령별인구현황_월간.csv"
df = pd.read_csv(file_path, encoding='euc-kr')

# 총인구수 열
total_col = '2025년05월_계_총인구수'

# 연령별 인구수 열 추출 및 이름 정제
age_cols = [col for col in df.columns if col.startswith('2025년05월_계_') and ('세' in col or '100세 이상' in col)]
def clean_age(col):
    if '100세 이상' in col:
        return '100+'
    return col.split('_')[-1].replace('세', '')
age_col_map = {col: clean_age(col) for col in age_cols}
df.rename(columns=age_col_map, inplace=True)

# 총인구수 숫자형 변환
df[total_col] = df[total_col].str.replace(",", "").astype(int)

# 총인구수 기준 상위 5개 지역 추출
top5_df = df.sort_values(by=total_col, ascending=False).head(5)

# 연령 데이터 추출 및 숫자형으로 변환
plot_df = top5_df[['행정구역'] + list(age_col_map.values())].copy()
for col in age_col_map.values():
    if plot_df[col].dtype == 'object':
        plot_df[col] = plot_df[col].str.replace(",", "").astype(int)

# 행정구역을 인덱스로 설정하고 transpose
plot_df.set_index('행정구역', inplace=True)
plot_df = plot_df.transpose()
plot_df.index.name = '연령'

# Streamlit 앱 구성
st.title("📊 2025년 5월 연령별 인구 현황 분석")
st.subheader("상위 5개 행정구역 기준 연령별 인구 변화")
st.line_chart(plot_df)

st.markdown("---")
st.subheader("📄 원본 데이터 (상위 5개 지역)")
st.dataframe(top5_df)
