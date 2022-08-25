'''Step1: Lead data
    step2: Merge the data
    Stpe3: Filter
    Step4: store in DB'''

'''Types of logg level is 5
    1. NOTSET   : 0
    2. DEBUG    : 10
    3. INFO     : 20
    4. WARNING  : 30
    5. ERROR    : 40
    6. CRITICAL : 50'''

import logging as logs
formt = ('%(asctime)s | %(name)s | %(levelname)s | %(msecs)d | %(levelno)s | %(process)d | %(message)s')
logs.basicConfig(filename='test.log', level=logs.NOTSET, filemode='w',format = formt)
logs.debug('This is a notset message.')
logs.info('This is info message.')
logs.warning('This is a warning')

logs.shutdown()