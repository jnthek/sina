import time
import sys

# Spinning cursor
def spinning_cursor():
  while True:
    for cursor in '\\|/-':
      time.sleep(0.1)
      # Use '\r' to move cursor back to line beginning
      # Or use '\b' to erase the last character
      sys.stdout.write('\r{}'.format(cursor))
      # Force Python to write data into terminal.
      sys.stdout.flush()
      
# Progress bar
def progress_bar():
  for i in range(100):
    time.sleep(0.1)
    sys.stdout.write('\r{:02d}: {}'.format(i, '#' * (i / 2)))
    sys.stdout.flush()

progress_bar()
