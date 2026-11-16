import random
import streamlit as st

st.set_page_config(page_title="오늘의 점심 추천기", page_icon="🍽️")

st.title("🍽️ 오늘 뭐 먹지? 점심 메뉴 추천기")
st.write("결정 장애 해결! 아래 버튼을 눌러 오늘의 점심 메뉴를 추천받아 보세요.")

lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈가스",
    "초밥",
    "짜장면",
    "짬뽕",
    "파스타",
    "햄버거",
    "국밥",
    "비빔밥",
    "쌀국수",
    "마라탕",
    "샌드위치",
    "카레라이스",
    "냉면",
    "부대찌개",
    "닭갈비",
]

st.divider()

if st.button("🎲 오늘의 점심 메뉴 뽑기!", use_container_width=True):
  selected_menu = random.choice(lunch_menus)
  st.balloons()
  st.success(
      f"오늘의 추천 점심 메뉴는 **[{selected_menu}]** 입니다! 맛있게 드세요! 😋"
  )
