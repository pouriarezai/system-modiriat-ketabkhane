# maker: pouria rezaie
# این فایل اصلی برنامه‌ست که همه چیز از اینجا شروع میشه
from library import Library
from member import Member

# این تابع main برنامه‌ست که همه کدها اینجا اجرا میشن
def main():
    # اینجا یه کتابخونه درست می‌کنیم که توش کتاب‌ها رو ذخیره کنیم
    library = Library()
    # یه حلقه بی‌نهایت داریم که تا وقتی کاربر نخواد خارج بشه، برنامه ادامه داشته باشه
    while True:
        print("\n--- Library Management System ---")
        print("1. Add a book")      # گزینه‌ها رو به کاربر نشون میدیم
        print("2. Search for a book")
        print("3. Add a member")
        print("4. Borrow a book")
        print("5. Return a book")
        print("6. Exit")
        choice = input("Enter your choice: ")   # از کاربر یه ورودی می‌گیریم که کدوم عملیات رو می‌خواد انجام بده

        # اگه کاربر انتخاب کنه که یه کتاب اضافه کنه
        if choice == '1':
            title = input("Enter the book title: ")   # عنوان کتاب رو می‌گیریم
            author = input("Enter the book author: ") # نویسنده کتاب رو می‌گیریم
            genre = input("Enter the book genre: ")   # ژانر کتاب رو می‌گیریم
            library.add_book(title, author, genre)    # کتاب رو به کتابخونه اضافه می‌کنیم
        # اگه کاربر بخواد دنبال یه کتاب بگرده
        elif choice == '2':
            keyword = input("Enter a keyword to search: ") # کلیدواژه جستجو رو می‌گیریم
            library.search_books(keyword)                  # جستجو می‌کنیم
        # اگه بخواد یه عضو جدید اضافه کنه
        elif choice == '3':
            name = input("Enter member name: ")            # اسم عضو رو می‌گیریم
            member = Member(name)                          # عضو رو می‌سازیم
            library.add_member(member)                     # عضو رو به کتابخونه اضافه می‌کنیم
        # اگه بخواد یه کتاب قرض بگیره
        elif choice == '4':
            member_name = input("Enter the member's name: ") # اسم عضو رو می‌گیریم
            book_title = input("Enter the book title: ")     # عنوان کتاب رو می‌گیریم
            library.borrow_book(member_name, book_title)     # عملیات قرض گرفتن کتاب رو انجام می‌دیم
        # اگه بخواد کتاب رو برگردونه
        elif choice == '5':
            member_name = input("Enter the member's name: ") # اسم عضو رو می‌گیریم
            book_title = input("Enter the book title: ")     # عنوان کتاب رو می‌گیریم
            library.return_book(member_name, book_title)     # کتاب رو پس می‌دیم
        # اگه بخواد برنامه رو ببنده
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")      # اگه انتخابش اشتباه باشه این پیام رو نشون میدیم

# اینجا چک می‌کنیم که برنامه از این فایل اجرا بشه، اگه بله، تابع main رو صدا می‌کنیم
if name == "__main__":
    main()