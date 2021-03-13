# -*- coding: utf-8 -*-

from task_4 import Test, log, configure_logging
import os

import psutil


class TestTwo(Test):

    def prep(self):
        log.debug('Starting test preparing')
        one_gb_to_byte = 1073741824
        if psutil.virtual_memory().available < one_gb_to_byte:
            raise MemoryError('RAM less than 1Gb')
        log.info('The preparing is successfully completed')

    def run(self):
        log.debug('Test execution')
        with open('./test.txt', 'wb') as file:
            size = 1024 * 1024 - 1
            file.write(os.urandom(size))
        log.info('Created a 1024 KB file with random content')

    def clean_up(self):
        log.debug('Completing the test')
        file_path = os.path.abspath('./test.txt')
        os.remove(file_path)
        log.info('File deleted')


if __name__ == '__main__':
    configure_logging()
    test = TestTwo(tc_id=2, name='Random File')
    test.execute()
