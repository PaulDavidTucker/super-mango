#importing the module 
import logging
import os

#gets the path of the logfile regardless of system.
originalPath = os.path.abspath(os.curdir)
pathToLogFile = os.getcwd()
os.chdir(originalPath)



#now we will Create and configure logger 
logging.basicConfig(filename=pathToLogFile+"/logsruntime.log", format='%(asctime)s %(message)s', filemode='w')

#new logger instance
log = logging.getLogger()
log.setLevel(logging.DEBUG)

