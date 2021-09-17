import logging


class Generate_Log:
    @staticmethod
    def generate_log():
        logging.basicConfig(filename=".\\Logs\\automation.log", force=True,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
