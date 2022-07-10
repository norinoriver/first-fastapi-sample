import os

class DBConfig:
    USER_NAME=os.environ.get("REDIS_USER_NAME")
    PASSWORD=os.environ.get("REDIS_DEFAULT_PASSWORD")
    HOSTNAME=os.environ.get("REDIS_HOSTNAME")
    PORT=os.environ.get("REDIS_LOCAL_PORT")
    DB_NUMBER=os.environ.get("REDIS_DB_NUMBER")

    def __init__(self):
        self.DB_SETTING = "redis://{0}:{1}@{2}:{3}/{4}".format(self.USER_NAME, self.PASSWORD, self.HOSTNAME, self.PORT, self.DB_NUMBER)

    def __str__(self):
        return self.DB_SETTING