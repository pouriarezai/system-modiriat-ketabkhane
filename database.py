# maker: pouria rezaie
# این فایل مسئول مدیریت دیتابیس کتابخونه‌ست. با استفاده از SQLite یه دیتابیس می‌سازیم تا اطلاعات کتاب‌ها و اعضا ذخیره بشه.
import sqlite3

# این کلاس برای مدیریت ارتباط با دیتابیسه
class Database:
    # وقتی این کلاس رو صدا می‌کنیم، به دیتابیس وصل می‌شیم و اگه جدول‌های لازم نبودن، اونا رو می‌سازیم
    def __init__(self, db_name="library.db"):
        self.conn = sqlite3.connect(db_name)   # اتصال به دیتابیس (یا ساختن اگه وجود نداره)
        self.cursor = self.conn.cursor()       # برای اجرای کوئری‌ها از این استفاده می‌کنیم
        self.create_tables()                   # تابع برای ساخت جدول‌ها رو صدا می‌زنیم

    # اینجا جدول‌های کتاب‌ها و اعضا رو می‌سازیم
    def create_tables(self):
        # ساخت جدول کتاب‌ها
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                               id INTEGER PRIMARY KEY,
                               title TEXT NOT NULL,
                               author TEXT NOT NULL,
                               genre TEXT NOT NULL,
                               is_borrowed INTEGER NOT NULL)''')
        
        # ساخت جدول اعضا
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS members (
                               id INTEGER PRIMARY KEY,
                               name TEXT NOT NULL)''')
        self.conn.commit()   # بعد از هر تغییر تو دیتابیس باید اینو صدا بزنیم که تغییرات ذخیره بشه

    # اضافه کردن یه کتاب جدید به دیتابیس
    def add_book(self, title, author, genre):
        self.cursor.execute("INSERT INTO books (title, author, genre, is_borrowed) VALUES (?, ?, ?, ?)", 
                            (title, author, genre, 0))   # 0 یعنی کتاب قرض داده نشده
        self.conn.commit()   # ذخیره تغییرات
        print(f"Book '{title}' added to the database.")

    # جستجوی کتاب‌ها بر اساس کلیدواژه
    def search_books(self, keyword):
        self.cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", 
                            ('%' + keyword + '%', '%' + keyword + '%'))  # کوئری جستجو در عنوان یا نویسنده
        books = self.cursor.fetchall()   # نتیجه کوئری رو می‌گیریم
        return books                     # برمی‌گردونیمشون

    # اضافه کردن یه عضو جدید به دیتابیس
    def add_member(self, name):
        self.cursor.execute("INSERT INTO members (name) VALUES (?)", (name,))
        self.conn.commit()
        print(f"Member '{name}' added to the database.")

    # قرض گرفتن کتاب (بروزرسانی وضعیت کتاب به قرض داده شده)
    def borrow_book(self, book_id):
        self.cursor.execute("UPDATE books SET is_borrowed = 1 WHERE id = ?", (book_id,))
        self.conn.commit()
        print(f"Book with ID {book_id} borrowed.")

    # پس دادن کتاب (بروزرسانی وضعیت کتاب به در دسترس)
    def return_book(self, book_id):
        self.cursor.execute("UPDATE books SET is_borrowed = 0 WHERE id = ?", (book_id,))
        self.conn.commit()
        print(f"Book with ID {book_id} returned.")

    # بستن اتصال به دیتابیس
    def close(self):
        self.conn.close()