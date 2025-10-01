import logging

# logging.basicConfig(filename='log_demo', level=logging.DEBUG)
# logging.disable(), if we do not want to print our logging messages

# logging.basicConfig(filename='log_demo', filemode='w')
# logging.basicConfig(filename='log_demo', filemode='w', level=logging.ERROR)
# logging.basicConfig(filename='log_demo',
#                     filemode='w',
#                     level=logging.INFO,
#                     format='%(asctime)s - %(levelname)s - %(message)s')

logging.basicConfig(filename='log_demo',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


# 3rd
logging.debug("This is a DEBUG message!")
logging.info("This is a INFO message!")
logging.warning("This is a WARNING message!")
logging.error("This is a ERROR message!")
logging.critical("This ia a CRITICAL message!")


# 2nd
# def nameCheck(name):

#     if len(name) < 2:
#         logging.debug("Checking for name length...")
#         return "Invalid name!!"
#     elif name.isspace():
#         logging.debug("checking if name is a space...")
#         return "Invalid name!!"
#     elif name.isalpha():
#         logging.debug("Checking if name is an alphabet...")
#         return "Name is valid"
#     elif name.replace(" ", '').isalpha():
#         logging.debug("checking for full name...")
#         return "Name is valid"
#     else:
#         logging.debug("Failed all checks...")
#         return "Invalid name!!"


# 1st
# def nameCheck(name):

#     if len(name) < 2:
#         print("Checking for name length...")
#         return "Invalid name!!"
#     elif name.isspace():
#         print("checking if name is a space...")
#         return "Invalid name!!"
#     elif name.isalpha():
#         print("Checking if name is an alphabet...")
#         return "Name is valid"
#     elif name.replace(" ", '').isalpha():
#         print("checking for full name...")
#         return "Name is valid"
#     else:
#         print("Failed all checks...")
#         return "Invalid name!!"


# print(nameCheck("K"))
