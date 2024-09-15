# maker: pouria rezaie
# این کلاس مربوط به اعضای کتابخونه‌ست

class Member:
    # وقتی یه عضو جدید درست می‌کنیم، اسمش رو می‌گیریم و لیست کتاب‌های قرض گرفته‌ش رو می‌سازیم
    def __init__(self, name):
        self.name = name                 # اسم عضو
        self.borrowed_books = []         # لیست کتاب‌های قرض گرفته شده

    # این تابع برای چاپ اطلاعات عضو به صورت رشته‌ایه
    def __str__(self):
        return f"Member: {self.name}, Borrowed books: {', '.join([book.title for book in self.borrowed_books])}"