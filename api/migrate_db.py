import sys, os, dotenv, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-e", "--env", help="setting file path of environ", required=True)
args = parser.parse_args()
dotenv.load_dotenv(args.env)

from sqlalchemy import create_engine
from api.models.task import Base
from api.models.user import Base
from api.config.mysql_config import DBConfig

DB_URL="mysql+pymysql://" + DBConfig().__str__()
engine = create_engine(DB_URL, echo=True)

def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    reset_database()