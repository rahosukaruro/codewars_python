def duplicate_count(text):

    duplicate = 0
    checklist = ''.join(set(text.lower()))
    
    for letter in checklist:
        if text.lower().count(letter) > 1:
            duplicate += 1
    
    return duplicate