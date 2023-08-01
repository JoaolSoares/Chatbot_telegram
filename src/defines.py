import  telebot
import  boto3
from	os				import getenv
from    dotenv  		import load_dotenv

load_dotenv()

# TELEGRAM
TELEGRAM_API_KEY	= getenv("TELEGRAM_API_KEY")
bot					= telebot.TeleBot(token=TELEGRAM_API_KEY)

# AWS
s3 = boto3.client(
    's3',
    aws_access_key_id		= getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key	= getenv("AWS_SECRET_KEY")
)
bucket						= "prod-luna-datalake"

# CLASSES
class User:
    id		= 0
    name	= ""

    def __init__(self, id, name):
          self.id	= id
          self.name	= name
