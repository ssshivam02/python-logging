import logging #default is name is root
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
datefmt='%m/%d/%y %H:%M:%S')
# logging.debug("this is debug")
# logging.info("this is info")
# logging.warning("this waring")
# logging.error("this is error")
# logging.critical("this is critical")

# output:-
# 08/20/22 23:54:32 - root - DEBUG - this is debug
# 08/20/22 23:54:32 - root - INFO - this is info
# 08/20/22 23:54:32 - root - WARNING - this waring
# 08/20/22 23:54:32 - root - ERROR - this is error
# 08/20/22 23:54:32 - root - CRITICAL - this is critical
import helper
