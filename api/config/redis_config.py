class DBConfig:
    USER_NAME="default"
    PASSWORD="test-passwd"
    HOSTNAME="localhost"
    PORT="26380"
    DB_NUMBER=0

    def __init__(self):
        self.DB_SETTING = "redis://{0}:{1}@{2}:{3}/{4}".format(self.USER_NAME, self.PASSWORD, self.HOSTNAME, self.PORT, self.DB_NUMBER)

    def __str__(self):
        return self.DB_SETTING