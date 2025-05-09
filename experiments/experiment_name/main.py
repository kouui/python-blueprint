from risk_based_auth import logging

logger = logging.setup_logger(level=logging.DEBUG)

def main() -> None:

    logger.info("Executing the main function...")
    return None

if __name__ == "__main__":
    main()
