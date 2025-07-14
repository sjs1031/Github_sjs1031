# Chapter015_otherMod2.py
import logging

module_logger = logging.getLogger("exampleApp.Chapters015_otherMod2")

def add(x,y):
    """"""
    logger = logging.getLogger("exampleApp.Chapters015_otherMod2")
    logger.info("added %s and %s to get %s" % (x, y, x+y))
    return x + y