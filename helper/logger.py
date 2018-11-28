import logging

def main():
    """
        The main entry point of the application
    """
    logger = logging.getLogger('LoggerApp')
    logger.setLevel(logging.INFO)

    # create the logging file handler
    fh = logging.FileHandler("error.txt")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)

    logger.info("Program started")
    logger.info("Done!")


if __name__ == "__main__":
    main()