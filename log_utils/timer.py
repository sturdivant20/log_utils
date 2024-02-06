#======================================== simple_timer.py =========================================#
#                                                                                                  #
#   Property of Daniel Sturdivant. Unauthorized copying of this file via any medium is would be    #
#   super sad and unfortunate for me. Proprietary and confidential.                                #
#                                                                                                  #
# ------------------------------------------------------------------------------------------------ #
#                                                                                                  #
#   @file                                                                                          #
#   @brief    simple utility for tracking runtime of any process                                   #
#   @author   Daniel Sturdivant <sturdivant20@gmail.com> <dfs0012@auburn.edu>                      #
#   @date     November 2023                                                                        #
#                                                                                                  #
#==================================================================================================#

from log_utils.logger import default_logger
import time

time_scales = {
  'ns': 1e9,
  'µs': 1e6,
  'ms': 1e3,
  's': 1.0,
  'min': 1.0/60.0,
  'hr': 1.0/3.6e3,
  'dy': 1.0/86.5e3}
auto_scale_thresholds = [
  (1100e-9, 'ns'),
  (1100e-6, 'µs'),
  (1100e-3, 'ms'),
  (120.0, 's'), # 2 min
  (7.2e3, 'min'), # 2 hr
  (345.6e3, 'hr'), # 4 dy
  (float('inf'), 'dy')]

def tic(message=None):
  # Show a message and start a timer.
  # Get the current precise time, and optionally show a message on stdout. By
  # default, the message is printed without a trailing newline character.
  #
  # Inputs:
  #   message     string to be printed verbatim (default: None)
  #   timestamp   include a timestamp with the message (default: True)
  # Outputs:
  #   output of time.perf_counter()
  #
  if message:
    default_logger.Info(message)
  return time.perf_counter()

def toc(t0, message='done.', unit='auto', precision=1):
  # Stop the timer and display the result.
  # Calculate the elapsed time relative to `t0`, format the result to an
  # appropriate time unit, and display the result.
  #
  # Inputs:
  #   t0          start time as reported by time.perf_counter()
  #   message     string to be printed immediately preceeding the time (default: 'done.')
  #   unit        reporting unit for the elapsed time; can be 'dy', 'hr', 'min',
  #                 's', 'ms', 'µs', 'ns', or 'auto' (default: 'auto')
  #   precision   number of decimal places to report (default: 1)
  #   timestamp   include a timestamp with the message (default: False)
  # Returns:
  #   elapsed time scaled to the specified units
  # 
  t1 = time.perf_counter()
  dt_s = t1-t0
  unit_l = unit.lower()
  try:
    scale = time_scales[unit_l]
  except KeyError:
    if unit_l != 'auto':
      print(f"Invalid unit spec: '{unit}'. Defaulting to 'auto'.")
    for threshold, scale_spec in auto_scale_thresholds:
      if dt_s < threshold:
        unit = scale_spec
        scale = time_scales[scale_spec]
        break
    else:
      print("Auto time scaling failed. Defaulting to 's'.")
      scale = 1.0
  dt = scale*dt_s
  default_logger.Info(f"{message} {dt:.{precision}f} {unit}")
  return dt, unit
