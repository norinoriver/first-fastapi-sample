from importlib.resources import path
import os

class ServerConfig:
    protcol = os.environ.get("API_PROTCOL")
    host = os.environ.get("API_HOST")
    port = os.environ.get("API_PORT")
    path = "/users/permit/"

    def __str__(self):
        return_str = ""
        if self.port == 80 and self.protcol == "http":
            return_str += self.protcol + "://" + self.host
        elif self.port == 443 and self.protcol == "https":
            return_str += self.protcol + "://" + self.host
        else:
            return_str += self.protcol + "://" + self.host + ":" + self.port

        return_str += self.path

        return return_str