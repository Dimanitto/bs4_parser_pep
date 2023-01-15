import logging
from constants import EXPECTED_STATUS
from requests import RequestException
from exceptions import ParserFindTagException


def get_response(session, url):
    try:
        response = session.get(url)
        response.encoding = 'utf-8'
        return response
    except RequestException:
        logging.exception(
            f'Возникла ошибка при загрузке страницы {url}',
            stack_info=True
        )


def find_tag(soup, tag, attrs=None):
    searched_tag = soup.find(tag, attrs=(attrs or {}))
    if searched_tag is None:
        error_msg = f'Не найден тег {tag} {attrs}'
        logging.error(error_msg, stack_info=True)
        raise ParserFindTagException(error_msg)
    return searched_tag


def check_status(preview_status, page_status, link):
    status = EXPECTED_STATUS.get(preview_status, '')
    if page_status not in status:
        different_statuses = f'''
        Несовпадающие статусы:
        {link}
        Статус в карточке: {page_status}
        Ожидаемые статусы: {status}'''
        logging.info(different_statuses)
