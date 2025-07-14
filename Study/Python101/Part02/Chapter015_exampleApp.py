import logging
import Chapter015_otherMod2

def main():
    """
    The main entry point of the application
    """
    logger = logging.getLogger("exampleApp")
    logger.setLevel(logging.INFO)

    # create the logging file handler
    fh = logging.FileHandler(".\Python_study_re\Python101\Part02\\new_snake.log")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # add handlers to logger object
    logger.addHandler(fh)

    logger.info("Program Started")
    result = Chapter015_otherMod2.add(7, 8)
    logger.info("Done")

if __name__ == "__main__":
    main()