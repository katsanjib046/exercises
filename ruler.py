def draw_line(tick_length, tick_label = ' '):
    """ Draw one line with given tick length followed by a label (optional)"""
    line = '-' * tick_length # drawing a single tick line of a given lenght
    if tick_label:
        line += ' ' + tick_label # if there is any label, it is attached
    print(line)

def draw_interval(center_length):
    """draw tick interval based upon a centra tick length"""
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)

def draw_ruler(num_inches, major_length):
    """Draw English ruler given number of inches, major tick length"""
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length,str(j))


if __name__ == "__main__":
    draw_ruler(5, 4)