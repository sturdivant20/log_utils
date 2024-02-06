#======================================== simple_logger.py ========================================#
#                                                                                                  #
#   Property of Daniel Sturdivant. Unauthorized copying of this file via any medium is would be    #
#   super sad and unfortunate for me. Proprietary and confidential.                                #
#                                                                                                  #
# ------------------------------------------------------------------------------------------------ #
#                                                                                                  #
#   @file                                                                                          #
#   @brief    simple utility for logging at different levels                                       #
#   @author   Daniel Sturdivant <sturdivant20@gmail.com> <dfs0012@auburn.edu>                      #
#   @date     November 2023                                                                        #
#                                                                                                  #
#==================================================================================================#

import datetime
from enum import Enum

class LogLevel(Enum):
  Trace = 0
  Debug = 1
  Info = 2
  Warn = 3
  Error = 4

class Color(Enum):
  Bold = "\u001b[1m"
  Reset = "\u001b[0m"
  White = "\u001b[37m"
  Trace = "\u001b[35m"  # magenta
  Debug = "\u001b[36m"  # cyan
  Info = "\u001b[32m"   # green
  Warn = "\u001b[33m"   # yellow
  Error = "\u001b[31m"  # red

class Logger:
  def __init__(self, level=LogLevel.Info):
    self.level = level

  def SetLogLevel(self, level: LogLevel):
    self.level = level

  def Trace(self, msg: str):
    if self.level.value <= LogLevel.Trace.value:
      t_stamp = self.__TimeStamp()
      print(f"{Color.Bold.value}[{t_stamp}] [{Color.Trace.value}Trace{Color.White.value}] {Color.Reset.value}{msg}")

  def Debug(self, msg: str):
    if self.level.value <= LogLevel.Debug.value:
      t_stamp = self.__TimeStamp()
      print(f"{Color.Bold.value}[{t_stamp}] [{Color.Debug.value}Debug{Color.White.value}] {Color.Reset.value}{msg}")

  def Info(self, msg: str):
    if self.level.value <= LogLevel.Info.value:
      t_stamp = self.__TimeStamp()
      print(f"{Color.Bold.value}[{t_stamp}] [{Color.Info.value}Info{Color.White.value} ] {Color.Reset.value}{msg}")

  def Warn(self, msg: str):
    if self.level.value <= LogLevel.Warn.value:
      t_stamp = self.__TimeStamp()
      print(f"{Color.Bold.value}[{t_stamp}] [{Color.Warn.value}Warn{Color.White.value} ] {Color.Reset.value}{msg}")

  def Error(self, msg: str):
    if self.level.value <= LogLevel.Error.value:
      t_stamp = self.__TimeStamp()
      print(f"{Color.Bold.value}[{t_stamp}] [{Color.Error.value}Error{Color.White.value}] {Color.Reset.value}{msg}")

  def __TimeStamp(self):
    return datetime.datetime.now().strftime('%F %T.%f')[:-3]


default_logger = Logger()
