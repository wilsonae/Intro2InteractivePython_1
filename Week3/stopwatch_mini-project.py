'''
An Introduction to Interactive Programming in Python (Part 1)
This mini-project assessment for week 3 will combine text drawing in 
the canvas with timers to build a simple digital stopwatch that keeps 
track of the time in tenths of a second.  The stopwatch contains 
"Start", "Stop" and "Reset" buttons.
'''
# http://www.codeskulptor.org/#user40_G4oFkLlUF7ZLBNA.py

# import required modules
import simplegui


# define global variables with initial values
counter = 0
n_stopped = 0
n_stopped_on_second = 0
timer_is_running = False


# define helper functions
def format(t):
    ''' This function converts the number of deciseconds, t, into
        the formatted string A:BC.D '''
    
    # get whole number of seconds and remaining decisecs
    secs = t / 10
    decisecs = t - 10*secs
    
    # get whole number of minutes and remaining seconds
    mins = secs / 60
    secs = secs - 60*mins
    
    # if number of seconds less than 10 need a leading zero
    if secs < 10:
        ten_string = "0"
    else:
        ten_string = ""
        
    # create and return the formatted string
    return str(mins) + ":" \
            + ten_string + str(secs) + "." \
            + str(decisecs)


# define event handlers for buttons; "Start", "Stop" and "Reset"
def start_timer():
    ''' This function with start the timer and set the 
        is_running flag to True '''
    
    global timer_is_running
    
    # Start the timer and set the flag 
    timer.start()
    timer_is_running = True
    
    return


def stop_timer():
    ''' This function with stop the timer and set the is_running flag to
        False.  It will also increment the stop counter and, if stopped 
        on the second, increment the stopped on second counter.  '''
    
    global n_stopped, n_stopped_on_second, timer_is_running
    
    # First stop the timer
    timer.stop()
    
    # If, and only if, the timer was running ...
    if timer_is_running:
        # ... increment stop counter
        n_stopped += 1          
        # ... set the running flag to False
        timer_is_running = False
        # ... and, if stopped on a round number of seconds
        if (counter % 10) == 0: 
            # increment 'stopped on second' counter
            n_stopped_on_second += 1
        
    return


def reset_timer():
    ''' This function will stop the timer and set the is_running flag to 
        False.  It will also set all the counters to zero. '''
    
    global counter, n_stopped, n_stopped_on_second, timer_is_running
    
    # First stop the timer
    timer.stop()
    
    # reset all the counters and running flag
    counter = 0
    n_stopped = 0 
    n_stopped_on_second = 0
    timer_is_running = False
    
    return


# define event handler for timer with 0.1 sec interval
def timer_handler():
    ''' This handler increments the tenth of a second counter '''
    global counter
    counter += 1
    return


# define draw handler
def draw_handler(canvas):
    ''' This handler draws both the formatted time and
        'correctness' ratio '''
    
    global n_stopped, n_stopped_on_second
    
    # Draw the formatted count of tenths of a second
    canvas.draw_text(format(counter), (80, 100), 24, 'White')
    
    # Create the ratio string and draw it
    ratio = str(n_stopped_on_second) + "/" + str(n_stopped)
    canvas.draw_text(ratio, (240, 40), 24, 'Green')
    
    return

    
# create frame
frame = simplegui.create_frame("Stopwatch",300,200)

# register event handlers
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)

# register button control elements
frame.add_button("Start Timer",start_timer,150)
frame.add_button("Stop Timer",stop_timer,150)
frame.add_button("Reset Timer",reset_timer,150)

# start frame
frame.start()
