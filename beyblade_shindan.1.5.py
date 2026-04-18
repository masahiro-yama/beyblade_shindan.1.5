# ------------------------
# 結果画面（売れる版）
# ------------------------
else:
    result = get_result(st.session_state.answers)

    st.title("🎉 けっか！")

    if result == "アタック":
        st.header("💥 アタックタイプ！")
        st.subheader("キミは…こうげきマスター！")
        st.write("いっしゅんで勝負をきめるスピードタイプ！ドカンと決めよう！🔥")

        st.image("https://m.media-amazon.com/images/I/61MpAh-qOsL._AC_SY450_.jpg", width=200)
        st.write("🔥 ドランソード")
        st.link_button("👉 キミにおすすめ！チェックする", "https://www.amazon.co.jp/dp/B0C52R16P1")

        st.image("https://m.media-amazon.com/images/I/715NtHVPy-L._AC_SY450_.jpg", width=200)
        st.write("🔥 フェニックスウイング")
        st.link_button("👉 もうひとつの強いベイを見る", "https://www.amazon.co.jp/dp/B0CMZSRJ3Q")

    elif result == "ディフェンス":
        st.header("🛡 ディフェンスタイプ！")
        st.subheader("キミは…まもりのたつじん！")
        st.write("どんなこうげきもはねかえす！さいごに勝つのはキミだ！💪")

        st.image("https://m.media-amazon.com/images/I/61N7ksTpjhL._AC_SY450_.jpg", width=200)
        st.write("🛡 ナイトフォートレス")
        st.link_button("👉 キミにおすすめ！チェックする", "https://www.amazon.co.jp/dp/B0GMDYS21K")

        st.image("https://m.media-amazon.com/images/I/71AMNY-FmqL._AC_SY450_.jpg", width=200)
        st.write("🛡 レオンクレスト")
        st.link_button("👉 もうひとつの強いベイを見る", "https://www.amazon.co.jp/dp/B0D91K2WMS")

    elif result == "スタミナ":
        st.header("🔄 スタミナタイプ！")
        st.subheader("キミは…ねばりの王さま！")
        st.write("さいごまでぐるぐる！あきらめない力で勝とう！🔥")

        st.image("https://m.media-amazon.com/images/I/61qO6OBNzBL._AC_SY450_.jpg", width=200)
        st.write("🔄 ウィザードアーク")
        st.link_button("👉 キミにおすすめ！チェックする", "https://www.amazon.co.jp/dp/B0DWSRHP7J")

        st.image("https://m.media-amazon.com/images/I/61aJExH96+L._AC_SY450_.jpg", width=200)
        st.write("🔄 ヘルズサイズ")
        st.link_button("👉 もうひとつの強いベイを見る", "https://www.amazon.co.jp/dp/B0C52C4L3T")

    else:
        st.header("⚡ バランスタイプ！")
        st.subheader("キミは…オールラウンダー！")
        st.write("なんでもできる最強タイプ！あいてにあわせて勝とう！✨")

        st.image("https://m.media-amazon.com/images/I/61WEAT7WNKL._AC_SY450_.jpg", width=200)
        st.write("⚡ エンペラーマイト")
        st.link_button("👉 キミにおすすめ！チェックする", "https://www.amazon.co.jp/dp/B0FV6Y4MH4")

        st.image("https://m.media-amazon.com/images/I/712keT+tMML._AC_SY450_.jpg", width=200)
        st.write("⚡ スコーピオスピア")
        st.link_button("👉 もうひとつの強いベイを見る", "https://www.amazon.co.jp/dp/B0F47G3QJT")

    st.divider()

    st.write("👇 ほかのタイプも見てみる？")

    if st.button("🔁 もういちどやる"):
        st.session_state.step = 0
        st.rerun()