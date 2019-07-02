import os
import sys
import logging
from datatime import datatime

logger = logging.getLogger(__name__)

class DataLogger(object):

  def __init__(self, config, debug=False):
    self.config = config
    self.plugins = []

    if debug:
      logger.setLevel(logging.DEBUG)
