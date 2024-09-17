"""Add initial book data

Revision ID: 0ac647fe2057
Revises: 856c2b823d4b
Create Date: 2024-09-17 23:57:59.950684

"""
from typing import Sequence, Union

from alembic import op

revision: str = "0ac647fe2057"
down_revision: Union[str, None] = "856c2b823d4b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


SQL_SCRIPT = '''
    INSERT INTO books (
        id, category, genre, title, pages, summary
    ) VALUES(1, 'any', 'algo', 'Грокаем алгоритмы', 273, 'Nice book');
    
    INSERT INTO chapters VALUES(1, 'Глава 1. Знакомство с алгоритмами', 1, 18, 39);
    INSERT INTO chapters VALUES(2, 'Глава 2. Сортировка выбором', 1, 40, 58);
    INSERT INTO chapters VALUES(3, 'Глава 3. Рекурсия', 1, 59, 74);
    INSERT INTO chapters VALUES(4, 'Глава 4. Быстрая сортировка', 1, 75, 99);
    INSERT INTO chapters VALUES(5, 'Глава 5. Хэш-таблицы', 1, 100, 126);
    INSERT INTO chapters VALUES(6, 'Глава 6. Поиск в ширину', 1, 127, 150);
    INSERT INTO chapters VALUES(7, 'Глава 7. Алгоритм Дейкстры', 1, 151, 181);
    INSERT INTO chapters VALUES(8, 'Глава 8. Жадные алгоритмы', 1, 182, 205);
    INSERT INTO chapters VALUES(9, 'Глава 9. Динамическое программирование', 1, 206, 235);
    INSERT INTO chapters VALUES(10, 'Глава 10. Алгоритм k ближайших соседей', 1, 236, 252);
    INSERT INTO chapters VALUES(11, 'Глава 11. Что дальше?', 1, 254, 273);
    
    INSERT INTO users (id, full_name, login, password) VALUES(1, 'Скуфзимир', 'skuf26', 'beer');
    INSERT INTO users (id, full_name, login, password) VALUES(2, 'Юрий', 'contraskuf', 'knowledge');
'''

def upgrade() -> None:
    op.execute(SQL_SCRIPT)


def downgrade() -> None:
    op.execute("DELETE FROM users")
    op.execute("DELETE FROM chapters")
    op.execute("DELETE FROM books")

