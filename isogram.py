def is_isogram(string):
      
    unique = ''.join(set(string.lower()))

    return True if len(unique) == len(string) else False

