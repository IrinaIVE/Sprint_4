from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len (collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    import pytest
    @pytest.mark.parametrize('film', ['Первое название фильма длиной больше 40 символов', 'Второе название фильма длиной больше 40 символов', 'Третье название фильма длиной больше 40 символов'])
    def test_add_new_book_add_books_negative_len(self, film):
        collector = BooksCollector()
        collector.add_new_book(film)
        assert len(collector.books_genre) == 0

    def test_add_new_book_add_two_books_negative_double_name(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Гордость и предубеждение')
        assert len(collector.books_genre) == 1

    def test_set_book_genre_smoke(self):
        collector = BooksCollector()
        collector.add_new_book('Ликвидация')
        collector.set_book_genre('Ликвидация','Детективы')
        assert collector.get_book_genre('Ликвидация') == 'Детективы'

    def test_get_book_genre_smoke(self):
        collector = BooksCollector()
        collector.books_genre = {'Ликвидация':'Детективы','Звёздные войны':'Фантастика','Чужой':'Фантастика'}
        assert collector.get_book_genre('Ликвидация') == 'Детективы'

    def test_get_books_with_specific_genre_smoke(self):
        collector = BooksCollector()
        collector.books_genre = {'Ликвидация':'Детективы','Звёздные войны':'Фантастика','Чужой':'Фантастика'}
        assert collector.get_books_with_specific_genre('Фантастика') == ['Звёздные войны' , 'Чужой']

    def test_get_books_genre_smoke(self):
        collector = BooksCollector()
        collector.books_genre = {'Ликвидация': 'Детективы', 'Звёздные войны': 'Фантастика', 'Чужой': 'Фантастика'}
        assert collector.get_books_genre() == {'Ликвидация': 'Детективы', 'Звёздные войны': 'Фантастика', 'Чужой': 'Фантастика'}

    def test_get_books_for_children_smoke(self):
        collector = BooksCollector()
        collector.books_genre = {'Ликвидация': 'Детективы', 'Звёздные войны': 'Фантастика', 'Чужой': 'Фантастика'}
        assert collector.get_books_for_children() == ['Звёздные войны', 'Чужой']

    def test_add_book_in_favorites_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert len (collector.favorites) == 2

    def test_get_list_of_favorites_books_smoke(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']

    def test_delete_book_from_favorites_smoke(self):
        collector = BooksCollector()
        collector.favorites = ['Ликвидация', 'Чужой']
        collector.delete_book_from_favorites('Ликвидация')
        assert collector.favorites == ['Чужой']
        