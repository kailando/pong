try:
  import curses
except:
  import os
  os.system("pip install -r requirements.txt")
  del(os)
import time
class impossible:
  def pong(stdscr):
      curses.curs_set(0)
      stdscr.nodelay(1)
      stdscr.timeout(100)
  
      # Initialize paddles and ball positions
      paddle_height, paddle_width = 5, 1
      left_paddle_pos, right_paddle_pos = 0, 0
      ball_pos = [curses.COLS // 2, curses.LINES // 2]
      ball_speed = [1, 1]
  
      while True:
          stdscr.clear()
  
          # Move the ball
          ball_pos[0] += ball_speed[0]
          ball_pos[1] += ball_speed[1]
  
          # Ball collisions with walls
          if ball_pos[1] <= 0 or ball_pos[1] >= curses.LINES - 1:
              ball_speed[1] = -ball_speed[1]
  
          # Ball collisions with paddles
          if (
              ball_pos[0] == 1
              and left_paddle_pos <= ball_pos[1] <= left_paddle_pos + paddle_height
          ) or (
              ball_pos[0] == curses.COLS - 2
              and right_paddle_pos <= ball_pos[1] <= right_paddle_pos + paddle_height
          ):
              ball_speed[0] = -ball_speed[0]
  
          # Set the CPU paddle position to the ball's Y position
          right_paddle_pos = int(ball_pos[1]) - paddle_height // 2
  
          # Draw paddles and ball
          for i in range(paddle_height):
              stdscr.addch(left_paddle_pos + i, 0, '|')
              stdscr.addch(right_paddle_pos + i, curses.COLS - 1, '|')
          stdscr.addch(int(ball_pos[1]), int(ball_pos[0]), '*')
  
          stdscr.refresh()
          time.sleep(0.1)
  def __init__(self):
      curses.wrapper(self.pong)
