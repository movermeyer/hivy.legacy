# -*- coding: utf-8 -*-
# vim:fenc=utf-8

'''
  test helpers
  ------------

  Provide some useful functions for efficient tests

  :copyright (c) 2014 Hive Tech, SAS.
  :license: Apache 2.0, see LICENSE for more details.
'''

import os
import hivy.utils as utils


def docker_required(function):
    ''' Run the provided function only if we can reach the docker server '''
    def inner(*args, **kwargs):
        ''' decorator '''
        _, status = utils.docker_check()
        if status and is_allowed('docker'):
            return function(*args, **kwargs)
        else:
            pass
    return inner


def serf_required(function):
    ''' Run the provided function only if we can reach the serf cluster '''
    def inner(*args, **kwargs):
        ''' decorator '''
        if utils.is_running('serf') and is_allowed('serf'):
            return function(*args, **kwargs)
        else:
            pass
    return inner


def is_allowed(command):
    ''' Mark "command" as available if running and allowed '''
    return os.environ.get('USE_{}'.format(command.upper()))
