import logging
 
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')
a=4
logging.debug('This is debug message %s' %(a))
logging.info('This is info message')
logging.warning('This is warning message')
