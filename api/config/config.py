class DBConfig:
    USER_NAME="root"
    PASSWORD="test-passwd"
    HOSTNAME="localhost"
    PORT="33306"
    CHARSET="utf8"

    def __init__(self):
        self.DB_SETTING = "{0}:{1}@{2}:{3}/demo?charset={4}".format(self.USER_NAME, self.PASSWORD, self.HOSTNAME, self.PORT, self.CHARSET)
        

    def __str__(self):
        return self.DB_SETTING
