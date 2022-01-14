def fine(authorized_speed, actual_speed):
    delta = actual_speed-authorized_speed
    if delta > 0 and delta <= 2:
        return 12.5
    elif 1 < delta <= 10:
        return delta*5
    elif delta > 10:
        return delta*2*5
    else:
        return 0
