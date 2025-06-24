import streamlit as st

# MBTI별 이모지와 추천 직업 데이터
mbti_info = {
    "INTJ": {
        "emoji": "🧠",
        "desc": "전략적인 사고와 통찰력을 가진 완벽주의자",
        "jobs": ["전략 컨설턴트", "연구원", "데이터 과학자"]
    },
    "INTP": {
        "emoji": "🧪",
        "desc": "호기심 많은 사색가, 아이디어 탐험가",
        "jobs": ["이론물리학자", "프로그래머", "AI 엔지니어"]
    },
    "ENTJ": {
        "emoji": "🚀",
        "desc": "야망 있고 추진력 강한 리더",
        "jobs": ["경영 컨설턴트", "CEO", "프로젝트 매니저"]
    },
    "ENTP": {
        "emoji": "💡",
        "desc": "창의적이고 도전적인 혁신가",
        "jobs": ["창업가", "마케팅 기획자", "기술 분석가"]
    },
    "INFJ": {
        "emoji": "🌌",
        "desc": "이상주의적 조언자, 깊이 있는 통찰력 보유자",
        "jobs": ["상담사", "심리학자", "작가"]
    },
    "INFP": {
        "emoji": "🎨",
        "desc": "감성적 이상주의자, 진정성을 중시하는 사람",
        "jobs": ["시인", "디자이너", "인권운동가"]
    },
    "ENFJ": {
        "emoji": "🤝",
        "desc": "열정적인 중재자, 사람을 이끄는 리더",
        "jobs": ["교사", "홍보 담당자", "정치가"]
    },
    "ENFP": {
        "emoji": "🔥",
        "desc": "열정 넘치는 활동가, 아이디어 뱅크",
        "jobs": ["방송 작가", "기획자", "브랜드 매니저"]
    },
    "ISTJ": {
        "emoji": "📊",
        "desc": "신중하고 철저한 현실주의자",
        "jobs": ["회계사", "공무원", "군인"]
    },
    "ISFJ": {
        "emoji": "🌷",
        "desc": "성실하고 따뜻한 수호자",
        "jobs": ["간호사", "사회복지사", "교사"]
    },
    "ESTJ": {
        "emoji": "📈",
        "desc": "체계적이고 지도력 강한 관리자",
        "jobs": ["경영 관리자", "경찰", "프로젝트 매니저"]
    },
    "ESFJ": {
        "emoji": "🎀",
        "desc": "사교적이고 친절한 협력가",
        "jobs": ["호텔 매니저", "비서", "이벤트 플래너"]
    },
    "ISTP": {
        "emoji": "🛠️",
        "desc": "실용적이고 과묵한 문제 해결자",
        "jobs": ["기술자", "응급 구조사", "파일럿"]
    },
    "ISFP": {
        "emoji": "🎭",
        "desc": "감성적인 예술가, 자유로운 영혼",
        "jobs": ["아티스트", "요리사", "원예사"]
    },
    "ESTP": {
        "emoji": "🏍️",
        "desc": "즉흥적이고 도전적인 활동가",
        "jobs": ["세일즈 매니저", "스포츠 코치", "기업가"]
    },
    "ESFP": {
        "emoji": "🎉",
        "desc": "인생을 즐기는 엔터테이너",
        "jobs": ["연예인", "스타일리스트", "여행 가이드"]
    }
}

# 타이틀과 설명
st.title("✨ MBTI 직업 추천기")
st.caption("당신의 성격 유형에 어울리는 직업을 찾아보세요!")

# 사용자 입력
mbti_list = list(mbti_info.keys())
selected_mbti = st.selectbox("🧬 MBTI를 선택하세요:", mbti_list)

# 결과 출력
if selected_mbti:
    data = mbti_info[selected_mbti]
    st.subheader(f"{data['emoji']} {selected_mbti}형 - {data['desc']}")
    st.markdown("#### 💼 추천 직업")
    for job in data["jobs"]:
        st.write(f"- {job}")
    
    # 풍선 효과
    st.balloons()
