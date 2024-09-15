# maker: pouria rezaie
# این فایل شامل کلاس‌های مربوط به کتابخونه و کتابه
class Book:
    # اینجا داریم تعریف می‌کنیم که یه کتاب چه ویژگی‌هایی داره
    def __init__(self, title, author, genre):
        self.title = title           # عنوان کتاب
        self.author = author         # نویسنده کتاب
        self.genre = genre           # ژانر کتاب
        self.is_borrowed = False     # این پرچم میگه که کتاب قرض داده شده یا نه

    # این تابع رو برای اینکه بتونیم کتاب‌ها رو راحت‌تر به صورت رشته چاپ کنیم
    def __str__(self):
        return f"{self.title} by {self.author} [{self.genre}]"

class Library:
    # اینجا داریم کتابخونه رو می‌سازیم
    def __init__(self):
        self.books = []    # یه لیست برای کتاب‌ها
        self.members = []   # یه لیست برای اعضا

    # این تابع برای اضافه کردن کتاب به کتابخونه‌ست
    def add_book(self, title, author, genre):
        book = Book(title, author, genre)   # یه کتاب جدید می‌سازیم
        self.books.append(book)             # کتاب رو به لیست کتاب‌ها اضافه می‌کنیم
        print(f"Book '{title}' added successfully.")  # پیام موفقیت چاپ می‌کنیم

    # این تابع برای جستجوی کتاب‌ها بر اساس یه کلیدواژه‌ست
    def search_books(self, keyword):
        found_books = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        if found_books:   # اگه کتابی پیدا شد
            for book in found_books:
                print(book)  # چاپش می‌کنیم
        else:
            print("No books found with that keyword.")  # اگه چیزی پیدا نشد این پیام رو می‌دیم

    # اینجا یه عضو به کتابخونه اضافه می‌کنیم
    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' added successfully.")

    # تابع برای قرض دادن کتاب به یه عضو
    def borrow_book(self, member_name, book_title):
        member = self.find_member(member_name)   # اول عضو رو پیدا می‌کنیم
        book = self.find_book(book_title)        # بعد کتاب رو پیدا می‌کنیم
        if member and book and not book.is_borrowed:  # چک می‌کنیم که کتاب قبلاً قرض داده نشده باشه
            book.is_borrowed = True              # وضعیت کتاب رو قرض داده شده می‌کنیم
            member.borrowed_books.append(book)   # کتاب رو به لیست کتاب‌های قرض گرفته شده عضو اضافه می‌کنیم
            print(f"Book '{book_title}' borrowed by {member_name}.")
        else:
            print("Unable to borrow the book. Either the member or book was not found, or the book is already borrowed.")

    # تابع برای پس گرفتن کتاب از یه عضو
    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        if member and book and book in member.borrowed_books:  # چک می‌کنیم که عضو این کتاب رو قرض گرفته باشه
            book.is_borrowed = False                           # وضعیت کتاب رو به در دسترس تغییر می‌دیم
            member.borrowed_books.remove(book)                 # کتاب رو از لیست قرض‌ها حذف می‌کنیم
            print(f"Book '{book_title}' returned by {member_name}.")
        else:
            print("Unable to return the book. Either the member or book was not found, or the book was not borrowed.")

    # اینجا یه تابع داریم که بر اساس عنوان کتاب، کتاب رو پیدا کنیم
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        print(f"Book '{title}' not found.")
        return None

    # این تابع برای پیدا کردن یه عضو بر اساس اسمشه
    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        print(f"Member '{name}' not found.")
        return None