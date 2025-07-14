# Chapter015_log_with_config

import logging
import logging.config
import Chapter015_otherMod2

def main():
    """
    Based on https://docs.python.org/howto/logging.html#configuring-logging
    """
    logging.config.fileConfig(".\Python_study_re\Python101\Part02\logging.conf")
    logger = logging.getLogger("exampleApp")

    logger.info("Program Started")
    result = Chapter015_otherMod2.add(7, 8)
    logger.info("Done")

if __name__ == "__main__":
    main()
