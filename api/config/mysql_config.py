import os

class DBConfig:
    USER_NAME=os.environ.get("MYSQL_ROOT_NAME")
    PASSWORD=os.environ.get("MYSQL_ROOT_PASSWORD")
    HOSTNAME=os.environ.get("MYSQL_HOSTNAME")
    PORT=os.environ.get("MYSQL_LOCAL_PORT")
    DB_NAME=os.environ.get("MYSQL_DBNAME")
    CHARSET=os.environ.get("MYSQL_CONNECTION_CHARSET")

    def __init__(self):
        self.DB_SETTING = "{0}:{1}@{2}:{3}/{4}?charset={5}".format(self.USER_NAME, self.PASSWORD, self.HOSTNAME, self.PORT, self.DB_NAME ,self.CHARSET)
        
    def __str__(self):
        return self.DB_SETTING
