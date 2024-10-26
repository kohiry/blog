import logging

from app.config import settings

__all__ = ["get_logger"]


def get_logger(name=__name__):
    """
    Создает и возвращает логгер с заданным именем.
    По умолчанию используется имя модуля (__name__).
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, settings.LOG_LEVEL, logging.INFO))

    # Проверяем, есть ли уже обработчики
    if not logger.handlers:
        # Создаем консольный обработчик только если их нет
        ch = logging.StreamHandler()
        ch.setLevel(getattr(logging, settings.LOG_LEVEL, logging.DEBUG))

        # Форматтер для вывода сообщений
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        ch.setFormatter(formatter)

        # Добавляем обработчик к логгеру
        logger.addHandler(ch)

    return logger
