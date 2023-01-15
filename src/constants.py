from pathlib import Path

MAIN_DOC_URL = 'https://docs.python.org/3/'
MAIN_PEP_URL = 'https://peps.python.org/'
BASE_DIR = Path(__file__).parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
WHATS_NEW_HEADERS = [('Ссылка на статью', 'Заголовок', 'Редактор, Автор')]
PEP_HEADERS = [('Cтатус', 'Количество')]
LATEST_VERSIONS_HEADERS = [('Ссылка на документацию', 'Версия', 'Статус')]

EXPECTED_STATUS = {
    'A': ('Active', 'Accepted'),
    'D': ('Deferred',),
    'F': ('Final',),
    'P': ('Provisional',),
    'R': ('Rejected',),
    'S': ('Superseded',),
    'W': ('Withdrawn',),
    '': ('Draft', 'Active'),
}
