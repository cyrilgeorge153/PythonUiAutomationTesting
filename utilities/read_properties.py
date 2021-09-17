import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class Read_Config:
    @staticmethod
    def getApplicationURL():
        url = config.get('common', 'aut_url')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common', 'password')
        return password
