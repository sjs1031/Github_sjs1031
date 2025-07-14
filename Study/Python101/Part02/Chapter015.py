'''
Logging
    Creating a simple logger
    How to log from multiple modules
    Log formation
    Log configuration
'''

# Creating a simple logger
'''
import logging
# add ilfemode="w" to overwrite
logging.basicConfig(filename=".\Python_study_re\Python101\Part02\sample.log", level=logging.INFO)

logging.debug("this is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")
'''

'''
import logging

logging.basicConfig(filename=".\Python_study_re\Python101\Part02\sample.log", level=logging.INFO)
log = logging.getLogger("ex")

try:
    raise RuntimeError
except RuntimeError:
    log.exception("Error")
'''

'''
# How to log From multiple Modules
import logging
import Chapter015_otherMod

def main():
    """
    The main entry point of the application
    """
    logging.basicConfig(filename=".\Python_study_re\Python101\Part02\mySnake.log", level=logging.INFO)
    logging.info("Program Started")
    result = Chapter015_otherMod.add(7,8)
    logging.info("Done")

if __name__ == "__main__":
    main()
'''

# Chapter015_exampleApp.py

# Configuring Logs for work and Pleasure

