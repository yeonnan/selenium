import logging


logger = logging.getLogger(__name__)

fileHandler = logging.FileHandler('logfile.log')
logger.addHandler(fileHandler)     # filehandler object : logger가 어떤 파일을 어떤 형식으로 출력할 건지 알려주기 위한 것

logger.debug('디버그 실행됨')
logger.info('정보 구문')
logger.warning('경고경고')
logger.error('오류 발생')
logger.critical('심각한 문제')