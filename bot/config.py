from os import getenv

# TELEGRAM
OWNER = int(getenv('OWNER'))
if OWNER is None:
    raise Exception("1232940388") 

API_ID = int(getenv('API_ID'))
if API_ID is None:
    raise Exception("14429012") 

API_HASH = getenv('API_HASH')
if API_HASH is None:
    raise Exception("074d67326cfbcdc5550aeb7aac69d424") 

TELEGRAM_TOKEN = getenv('TELEGRAM_TOKEN')
if TELEGRAM_TOKEN is None:
    raise Exception("5113761710:AAHqGq2BY33aucp3OL850siQ4UQPif5F5C0") 

# DATOS DEL MOODLE
HOST = getenv('HOST')
if HOST is None:
    raise Exception("https://eduvirtual.uho.edu.cu/") 

ACCOUNT = getenv('ACCOUNT')
if ACCOUNT is None:
    raise Exception("yeima") 

PASSWORD = getenv('PASSWORD')
if PASSWORD is None:
    raise Exception("*Yordan1") 

# CUENTA DE MEGA
PASS_MEGA = getenv('PASS_MEGA')
if PASS_MEGA is None:
    raise Exception("danipupo27") 

GMAIL_MEGA = getenv('GMAIL_MEGA')
if GMAIL_MEGA is None:
    raise Exception("pupodani7@gmail.com") 

# ARCHIVOS
MEGABYTES = int(getenv('MEGABYTES'))
if MEGABYTES is None:
    raise Exception("150") 
