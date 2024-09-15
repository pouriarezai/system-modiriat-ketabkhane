from setuptools import setup, find_packages

setup(
    name='LibraryManagementSystem',
    version='0.1',
    description='سیستم مدیریت کتابخانه برای مدیریت کتاب‌ها، اعضا و امانت‌های کتاب.',
    author='پوریا رضایی کماسی',
    author_email='Pouriarezaie6587@gmail.com',
    packages=find_packages(),
    install_requires=[
        'sqlite3',  # اطمینان از نصب sqlite3
    ],
    entry_points={
        'console_scripts': [
            'library-manager = main:main_function',  # نقطه ورودی را مطابق نیاز تنظیم کنید
        ],
    },
    include_package_data=True,
)