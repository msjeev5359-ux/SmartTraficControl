def get_signal_timing(count):
    if count >= 10:
        return 60
    elif count >= 5:
        return 30
    else:
        return 15