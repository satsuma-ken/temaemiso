#
# Gunicorn config file
#
wsgi_app = 'temaemiso.wsgi:application'

# Server Mechanics
#========================================
# current directory
chdir = './'

# daemon mode
daemon = False

# enviroment variables
# raw_env = [
#     'ENV_TYPE=dev',
#     'HOGEHOGE_KEY=xxxxxxxxxxxxxxxxxxxxxxxxx'
# ]

# Server Socket
#========================================
bind = '0.0.0.0:8000'

# Worker Processes
#========================================
workers = 4

#  Logging
#========================================
# access log
# accesslog = '/work/python/gunic/gu/logs/access.log'
# access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# gunicorn log
# accesslog = '-'
errorlog = '-'
loglevel = 'info'