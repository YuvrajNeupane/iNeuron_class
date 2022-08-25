import logging

formt = ('%(asctime)s | %(name)s | %(levelname)s | %(message)s ')
logging.basicConfig(filename='test2.log', level=logging.DEBUG, filemode='w',format=formt)

def divi(a,b):
    logging.info('The number user enterted by %s and %s', a,b)
    try:
        logging.info('we are into function')
        div = a/b
        logging.info('This is the ans of %s', div)
        logging.info('we are completed a division operation.')
    except Exception as e:
        logging.exception(e)
divi(3,1)