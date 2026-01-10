import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    #def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        #collector = BooksCollector()

        # добавляем две книги
        #collector.add_new_book('Гордость и предубеждение и зомби')
        #collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        #assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector(

    def test_add_new_book_name_too_long_not_added(self):
        collector = BooksCollector()
        long_name = 'А' * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    def test_add_new_book_empty_name_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert '' not in collector.get_books_genre()

    def test_add_new_book_duplicate_not_added(self):
        collector = BooksCollector()
        book_name = 'Тестовая книга'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        books = collector.get_books_genre()
        count = list(books.keys()).count(book_name)
        assert count == 1

    def test_set_book_genre_for_existing_book(self):
        collector = BooksCollector()
        book_name = 'Ужасная книга'
        genre = 'Ужасы'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_set_book_genre_for_nonexistent_book_not_set(self):
        collector = BooksCollector()
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert 'Несуществующая книга' not in collector.get_books_genre()

    def test_set_book_genre_invalid_genre_not_set(self):
        collector = BooksCollector()
        book_name = 'Тестовая книга'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Несуществующий жанр')
        assert collector.get_book_genre(book_name) == ''

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_with_specific_genre_returns_correct_books(self, genre):
        collector = BooksCollector()

        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.add_new_book('Книга3')

        collector.set_book_genre('Книга1', genre)

        available_genres = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        other_genres = [g for g in available_genres if g != genre]
        other_genre = other_genres[0]
        collector.set_book_genre('Книга2', other_genre)

        collector.set_book_genre('Книга3', '')
        books_with_genre = collector.get_books_with_specific_genre(genre)
        assert 'Книга1' in books_with_genre
        assert 'Книга2' not in books_with_genre
        assert 'Книга3' not in books_with_genre

    def test_get_books_for_children_returns_only_child_friendly_books(self):
        collector = BooksCollector()
        collector.add_new_book('Детская книга')
        collector.add_new_book('Страшная книга')
        collector.add_new_book('Детективная книга')
        collector.add_new_book('Веселая книга')

        collector.set_book_genre('Детская книга', 'Мультфильмы')
        collector.set_book_genre('Страшная книга', 'Ужасы')
        collector.set_book_genre('Детективная книга', 'Детективы')
        collector.set_book_genre('Веселая книга', 'Комедии')

        children_books = collector.get_books_for_children()
        assert 'Детская книга' in children_books
        assert 'Веселая книга' in children_books
        assert 'Страшная книга' not in children_books
        assert 'Детективная книга' not in children_books

    def test_add_book_in_favorites_adds_book_to_favorites(self):
        collector = BooksCollector()
        book_name = 'Любимая книга'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_nonexistent_book_not_added(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        book_name = 'Книга для удаления'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    def test_add_new_book_with_max_length_name_added_successfully(self):
        collector = BooksCollector()
        max_length_name = 'К' * 40
        collector.add_new_book(max_length_name)
        assert max_length_name in collector.get_books_genre()



