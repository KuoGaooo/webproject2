# set key for login
SECRET_KEY = "zheshibenxiangmudemiyao"


# set database
HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "web_project2"
DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
SQLALCHEMY_DATABASE_URI = DB_URI

# set email
MAIL_SERVER = "smtp.163.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "gxt23318508@163.com"
MAIL_PASSWORD = "YWFZZWCECLHGXVIT"
MAIL_DEFAULT_SENDER = "gxt23318508@163.com"
