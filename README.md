# Реализованные тесты

# 1. Тесты для метода `add_new_book`
`test_add_new_book_name_too_long_not_added` - проверка, что книга с именем длиннее 40 символов не добавляется
`test_add_new_book_empty_name_not_added` - проверка, что книга с пустым именем не добавляется  
`test_add_new_book_duplicate_not_added` - проверка, что дубликат книги не добавляется
`test_add_new_book_with_max_length_name_added_successfully` - проверка, что книга с именем ровно 40 символов добавляется успешно

# 2. Тесты для метода `set_book_genre`
`test_set_book_genre_for_existing_book` - установка жанра для существующей книги
`test_set_book_genre_for_nonexistent_book_not_set` - нельзя установить жанр для несуществующей книги
`test_set_book_genre_invalid_genre_not_set` - нельзя установить несуществующий жанр

# 3. Параметризованный тест для метода `get_books_with_specific_genre`
`test_get_books_with_specific_genre_returns_correct_books` - проверяет получение книг для всех 5 жанров: Фантастика, Ужасы, Детективы, Мультфильмы, Комедии

# 4. Тест для метода `get_books_for_children`
`test_get_books_for_children_returns_only_child_friendly_books` - возвращаются только книги без возрастного рейтинга

# 5. Тесты для работы с избранным
`test_add_book_in_favorites_adds_book_to_favorites` - добавление книги в избранное
`test_add_book_in_favorites_nonexistent_book_not_added` - нельзя добавить в избранное несуществующую книгу
`test_delete_book_from_favorites_removes_book` - удаление книги из избранного

# Параметризация
Использована в тесте `test_get_books_with_specific_genre_returns_correct_books` с помощью декоратора `@pytest.mark.parametrize`. 
Тест запускается 5 раз - по одному для каждого жанра.
