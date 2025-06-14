import logging

def test_logging():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    # s를 붙여야 문자열로 취급되어 최종적으로 모두 연결 가능
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)     # filehandler object : logger가 어떤 파일을 어떤 형식으로 출력할 건지 알려주기 위한 것

    logger.setLevel(logging.DEBUG)
    logger.debug('디버그 실행됨')
    logger.info('정보 구문')
    logger.debug('디버그 실행됨')
    logger.warning('경고경고')
    logger.error('오류 발생')
    logger.critical('심각한 문제')