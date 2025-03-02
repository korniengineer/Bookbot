import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}

# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    stop = [',', '.', '!', ':', ';', '?']
    end = start + size
    
    if len(text) >= end-1:
        if text[end-1] in stop and (text[end-2] not in stop or text[end] not in stop):
            return text[start:end], size
        else:
            while text[end-1] not in stop or (text[end-2] in stop or text[end] in stop):
                end -= 1
                size -= 1
            return text[start:end], size
    else:
        return text[start:], len(text) - start

# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    pass

# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))