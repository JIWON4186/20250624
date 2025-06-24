import streamlit as st

# MBTI 별 추천 직업 사전
mbti_jobs = {
    "INTJ": ["전략 컨설턴트", "연구원", "데이터 과학자"],
    "INTP": ["이론물리학자", "프로그래머", "AI 엔지니어"],
    "ENTJ": ["경영 컨설턴트", "CEO", "프로젝트 매니저"],
    "ENTP": ["창업가", "마케팅 기획자", "기술 분석가"],
    "INFJ": ["상담사", "심리학자", "작가"],
    "INFP": ["시인", "디자이너", "인권운동가"],
    "ENFJ": ["교사", "홍보 담당자", "정치가"],
    "ENFP": ["방송 작가", "기획자", "브랜드 매니저"],
    "ISTJ": ["회계사", "공무원", "군인"],
    "ISFJ": ["간호사", "사회복지사", "교사"],
    "ESTJ": ["경영 관리자", "경찰", "프로젝트 매니저"],
    "ESFJ": ["호텔 매니저", "비서", "이벤트 플래너"],
    "ISTP": ["기술자", "응급 구조사", "파일럿"],
    "ISFP": ["아티스트", "요리사", "원예사"],
    "ESTP": ["세일즈 매니저", "스포츠 코치", "기업가"],
    "ESFP": ["연예인", "스타일리스트", "여행 가이드"]
}

# 앱 제목
st.title("💼 MBTI 기반 직업 추천기")

# MBTI 선택
mbti_types = list(mbti_jobs.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_types)

# 결과 출력
if selected_mbti:
    st.subheader(f"🧠 {selected_mbti} 유형에게 추천하는 직업")
    for job in mbti_jobs[selected_mbti]:
        st.write(f"- {job}")
