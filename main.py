

if __name__ == "__main__":
    from textSummarizer.logging import logger
    try:
        x = 1/0
        logger.info('division not possible')
    except Exception as ex:
        logger.error(f'division not possible by :: {ex}')
