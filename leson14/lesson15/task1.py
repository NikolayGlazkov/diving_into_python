import logging

logging.basicConfig(level=logging.NOTSET,filename="info_log")

logger = logging.getLogger(__name__)
logger.info("")
logger.error("")

def zero_devide(num1,num2):
    try:
        result = num1/num2
    except ZeroDivisionError as e:
        logger.exception("Произошла ошибка деления на ноль: %s", e)