import streamlit as st
import sqlite3
from datetime import datetime
import os  # اضافه کردن ماژول os

# تنظیمات صفحه و استایل کلی
st.set_page_config(page_title="وبلاگ من", page_icon="✍️", layout="wide")
st.markdown("""
<style>
body {
    direction: rtl;
    font-family: "IRANSans", sans-serif;
     text-align: right;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    font-size: 16px;
    border-radius: 5px;
}
.stTextInput>div>input, .stTextArea>div>textarea {
    font-size: 16px;
}
.stImage>img {
    border-radius: 10px;
}
.highlight-text {
        color: black; /* رنگ متن */
        font-weight: bold; /* برای برجسته‌تر کردن، اختیاری */
    }
</style>
""", unsafe_allow_html=True)

# اتصال به پایگاه داده
def get_db_connection():
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    return conn

# ایجاد جدول مقالات اگر وجود نداشته باشد
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author TEXT NOT NULL,
            image_path TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.close()

# تابع برای افزودن مقاله جدید
def add_article(title, content, author, image):
    os.makedirs('uploads', exist_ok=True)  # ایجاد پوشه uploads اگر وجود ندارد

    conn = get_db_connection()
    image_path = None
    if image:
        # ذخیره عکس در پوشه
        image_path = f"uploads/{image.name}"
        with open(image_path, "wb") as f:
            f.write(image.getbuffer())

    conn.execute('''
        INSERT INTO articles (title, content, author, image_path) 
        VALUES (?, ?, ?, ?)
    ''', (title, content, author, image_path))
    conn.commit()
    conn.close()

# تابع برای دریافت مقالات
def get_articles():
    conn = get_db_connection()
    articles = conn.execute('SELECT * FROM articles ORDER BY created_at DESC').fetchall()
    conn.close()
    return articles

# اجرای مقداردهی اولیه پایگاه داده
init_db()

# صفحه اصلی
def main():
    st.title("🌟 وبلاگ شخصی 🌟")
    st.markdown("""
    <div style="background-color: #f0f0f5; padding: 10px; border-radius: 10px; font-size: 18px;">
        به وبلاگ من خوش آمدید! اینجا می‌توانید نوشته‌های من را بخوانید و مقاله‌های خود را ارسال کنید. 😊
    </div>
    """, unsafe_allow_html=True)

    # تب‌بندی
    tab1, tab2 = st.tabs(["📖 مقالات", "✍️ ایجاد مقاله جدید"])

    with tab1:
        st.header("آخرین مقالات")
        articles = get_articles()

        if articles:
            for article in articles:
                # کارت برای هر مقاله
                with st.container():
                    col1, col2 = st.columns([1, 3], gap="medium")

                    with col1:
                        if article['image_path']:
                            st.image(article['image_path'])
                    with col2:
                        st.subheader(article['title'])
                        st.markdown(f"<p style='font-size:14px; color:gray;'>✍️ نویسنده: {article['author']} | 📅 تاریخ: {article['created_at']}</p>", unsafe_allow_html=True)
                        st.write(article['content'][:200] + "...")

                    st.divider()
        else:
            st.info("هنوز هیچ مقاله‌ای ثبت نشده است. اولین مقاله را شما ثبت کنید!")

    with tab2:
        st.header("✍️ ایجاد مقاله جدید")
        st.markdown("<p style='color:gray; font-size:14px;'>لطفاً اطلاعات زیر را برای ارسال مقاله وارد کنید:</p>", unsafe_allow_html=True)

        # فرم ایجاد مقاله
        with st.form("new_article_form", clear_on_submit=True):
            title = st.text_input("عنوان مقاله", placeholder="عنوان مقاله را وارد کنید")
            author = st.text_input("نام نویسنده", placeholder="نام خود را وارد کنید")
            content = st.text_area("متن مقاله", placeholder="محتوای مقاله را اینجا بنویسید", height=200)
            image = st.file_uploader("آپلود تصویر (اختیاری)", type=['jpg', 'jpeg', 'png'])

            submit = st.form_submit_button("📥 ثبت مقاله")

            if submit:
                if title and content and author:
                    add_article(title, content, author, image)
                    st.success("✅ مقاله با موفقیت ثبت شد!")
                else:
                    st.error("❌ لطفاً تمام فیلدهای الزامی را تکمیل کنید.")

# اجرای برنامه
if __name__ == "__main__":
    main()





# streamlit run blog.py