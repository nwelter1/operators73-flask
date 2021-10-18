import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Gives Flask access to relative filepath regardless of OS.
# Allows outside files/folders to be imported as well
# can consider this a 'roadmap' we're giving flask for our operating system
