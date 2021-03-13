# -*- coding: utf-8 -*-

from task_4 import Test, log, configure_logging
import time
import os


class TestOne(Test):

    def prep(self):
        log.debug('Starting test preparing')
        if round(time.time()) % 2 != 0:
            raise RuntimeError('System time is not a multiple of 2')
        log.info('The preparing is successfully completed')

    def run(self):
        log.debug('Test execution')
        print(os.listdir())
        log.info('The list of contents of the current directory is received')

    def clean_up(self):
        log.debug('Completing the test')
        log.info('Test completed successfully')


if __name__ == '__main__':
    configure_logging()
    test = TestOne(tc_id=1, name='List of files')
    test.execute()
