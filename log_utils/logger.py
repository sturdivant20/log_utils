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

from datetime import datetime
# from enum import Enum
from dataclasses import dataclass, fields

# class LogLevel(Enum):
@dataclass
class LogLevel:
  Trace: int = 0
  Debug: int = 1
  Info: int = 2
  Warn: int = 3
  Error: int = 4

# class Color(Enum):
@dataclass
class Color:
  Trace: str = "\u001b[35m"  # magenta
  Debug: str = "\u001b[36m"  # cyan
  Info: str = "\u001b[32m"   # green
  Warn: str = "\u001b[33m"   # yellow
  Error: str = "\u001b[31m"  # red
  Bold: str = "\u001b[1m"
  Reset: str = "\u001b[0m"
  White: str = "\u001b[37m"
  
# class Level(Enum):
@dataclass
class Level:
  Trace: str = "Trace"
  Debug: str = "Debug"
  Info: str  = "Info "
  Warn: str  = "Warn "
  Error: str = "Error"

class Logger:
  def __init__(self, level=LogLevel.Info):
    self.level = level

  def SetLogLevel(self, level: LogLevel):
    self.level = level

  def Trace(self, msg: str):
    if self.level <= LogLevel.Trace:
      print(self.GenerateSring(msg, Level.Trace, Color.Trace))

  def Debug(self, msg: str):
    if self.level <= LogLevel.Debug:
      print(self.GenerateSring(msg, Level.Debug, Color.Debug))

  def Info(self, msg: str):
    if self.level <= LogLevel.Info:
      print(self.GenerateSring(msg, Level.Info, Color.Info))

  def Warn(self, msg: str):
    if self.level <= LogLevel.Warn:
      print(self.GenerateSring(msg, Level.Warn, Color.Warn))

  def Error(self, msg: str):
    if self.level <= LogLevel.Error:
      print(self.GenerateSring(msg, Level.Error, Color.Error))
      
  def GenerateSring(self, msg: str, level: Level, color: Color):
    t_stamp = self.__TimeStamp()
    return f"{Color.Bold}[{t_stamp}] [{color}{level}{Color.White}] {Color.Reset}{msg}"
    

  def __TimeStamp(self):
    return datetime.now().strftime('%F %T.%f')[:-3]


default_logger = Logger()
