# -*- coding: utf-8 -*-
import logging


def handler(event, context):
    logger = logging.getLogger()
    logger.info('hello function invoked by FnF')
    return '{"name": "hello world"}'
