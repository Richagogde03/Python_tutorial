import logging

logging.basicConfig(level=logging.INFO,
                    filename="day21/demo_log",
                    filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")
# logging.debug('debug')
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

# x = 2
# logging.info(f"the value of x is {x}")

try:
    1/0
# except ZeroDivisionError as e:
    # logging.error("ZeroDivisionError", exc_info=True)
except ZeroDivisionError:
    logging.exception("ZeroDivisionError")


logger = logging.getLogger(__name__)
handler = logging.FileHandler('day21/test.log')
formatter = logging.Formatter("""%(asctime)s - %(name)s - %(levelname)s -
                              %(message)s""")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("Test the custom logger")
