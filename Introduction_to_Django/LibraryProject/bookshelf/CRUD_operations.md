 all_book = Book.objects.all()
>>> for book in all_book: print(f'{book.title}, {book.author}, {book.publication_year}')
...
1984, George Orwell, 1949
>>> update_book = Book.objects.filter(title='1984').update(title='Nineteen Eighty-Four')
>>> delete_book = Book.objects.filter(publication_year=1949).delete()
>>>

