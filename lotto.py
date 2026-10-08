import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="로또 번호 생성기", page_icon="🎰", layout="centered")


# 로또 공 색상 스타일 정의 함수 (한 줄로 깔끔하게 정리하여 HTML 출력 오류 방지)
def get_ball_style(number):
    if number <= 10:
        bg_color, text_color = "#fbc400", "#000000"  # 노란색 (1~10)
    elif number <= 20:
        bg_color, text_color = "#69c6f0", "#ffffff"  # 파란색 (11~20)
    elif number <= 30:
        bg_color, text_color = "#ff6f61", "#ffffff"  # 빨간색 (21~30)
    elif number <= 40:
        bg_color, text_color = "#aaaaaa", "#ffffff"  # 회색 (31~40)
    else:
        bg_color, text_color = "#b0d840", "#000000"  # 녹색 (41~45)

    return f'<div style="display:inline-block; width:48px; height:48px; line-height:48px; border-radius:50%; background-color:{bg_color}; color:{text_color}; text-align:center; font-weight:bold; font-size:18px; margin:4px; box-shadow:2px 2px 5px rgba(0,0,0,0.2);">{number}</div>'


# Session State 초기화 (최대 5개 세트 저장용)
if "lotto_history" not in st.session_state:
    st.session_state.lotto_history = []

st.title("🎰 로또 번호 생성기")
st.write("버튼을 누르면 중복 없는 6개 번호를 추첨합니다. (최대 5개 세트 저장)")

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("🎲 로또번호 생성", use_container_width=True):
        # 1~45 중복 없는 6개 번호 추출 후 정렬
        new_numbers = sorted(random.sample(range(1, 46), 6))

        # 리스트 맨 앞에 추가
        st.session_state.lotto_history.insert(0, new_numbers)

        # 최대 5개 세트 유지
        if len(st.session_state.lotto_history) > 5:
            st.session_state.lotto_history.pop()

with col2:
    if st.button("🔄 초기화", use_container_width=True):
        st.session_state.lotto_history = []
        st.rerun()

st.divider()

# 로또 번호 출력
if st.session_state.lotto_history:
    for idx, numbers in enumerate(st.session_state.lotto_history, 1):
        st.markdown(f"### 📍 {len(st.session_state.lotto_history) - idx + 1}회차 추천 번호")

        # HTML을 통한 로또 공 시각화
        balls_html = "".join([get_ball_style(num) for num in numbers])
        st.html(balls_html)
        st.write("")
else:
    st.info("버튼을 눌러 로또 번호를 생성해 보세요!")