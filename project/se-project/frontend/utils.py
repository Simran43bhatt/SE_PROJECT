# frontend/utils.py
def validate_positive_integer(value):
    try:
        return int(value) > 0
    except ValueError:
        return False
