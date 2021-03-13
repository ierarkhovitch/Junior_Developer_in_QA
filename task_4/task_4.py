# -*- coding: utf-8 -*-

import logging
import sys

log = logging.getLogger()


def configure_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(fmt="%(asctime)s %(levelname)s: %(message)s",
                                                  datefmt="%d-%m-%Y %H:%M:%S"))
    stream_handler.setLevel(logging.DEBUG)
    log.addHandler(stream_handler)

    log.setLevel(logging.DEBUG)


class Test:
    def __init__(self, tc_id, name):
        self.tc_id = tc_id
        self.name = name

    def prep(self):
        pass

    def run(self):
        pass

    def clean_up(self):
        pass

    def execute(self):
        log.debug(f'Running a test case - id:{self.tc_id}, name:{self.name}')
        try:
            self.prep()
            self.run()
            self.clean_up()
        except Exception as exc:
            log.error(exc)
            sys.exit()
        log.info(f'Successful completion of the test case - id:{self.tc_id}, name:{self.name}')
