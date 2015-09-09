from Queue import Queue
import os

QUEUE_SIZE = 40
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DOWNLOAD_DIR = os.path.join(os.path.dirname(__file__), 'WebPages/')
HISTORY_FILE = os.path.join(DOWNLOAD_DIR, 'record.his')
LOG_FILE = os.path.join(DOWNLOAD_DIR, 'process.log')
DATABASE = os.path.join(BASE_DIR, 'data.db')

checkedProxyList = ["202.4.186.102:80","103.27.111.246:80","173.201.177.140:80","111.13.109.8:80","119.187.148.35:80",\
"98.117.210.21:80","54.178.196.171:80","210.3.4.161:80","89.43.53.37:80","108.178.184.45:80"]

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

URL_DOWNLOAD_LIST = Queue()
URL_VISITED_LIST = []
URL_VISITED_FILE_LIST = Queue()
DOWLOAD_THREAD_POOL_SIZE = 50
ANAYLIZER_THREAD_POOL_SIZE = 2
REDOWNLOAD_TIME = 5
URL_NEW_DOWNLOAD_TIMEOUT = 10
URL_NEW_EXTRACT_TIMEOUT = 20

HTTP_RESPONSE_ERROR = {
            204:"No Response", \
            400:"Bad Request", \
            401:"Unauthorized", \
            403:"Forbidden", \
            404:"Not Found", \
            405:"Method not allowed", \
            406:"Not Acceptable", \
            408:"Request Timeout", \
            409:"Conflict", \
            413:"Request Entity Too Large", \
            414:"Request URL Too Long", \
            417:"Expectition Failed", \
            444:"No Response", \
            500:"Enternal Server Error", \
            502:"Bad Gateway", \
            599:"Network Connect timeout Error" \
        }

DOWNLOAD_RESULT = {
      "SUCCESS":300, \
      "FAIL":400, \
}
accounts = [{"sxhanhao@gmail.com":"hanhaohh"}, {"io0910@live.cn":"chaojicai00"}]
