def order(sentence):
    
    sentence_dict = {}
    
    for word in sentence.split():
        for letter in word:
        
            if letter.isdigit():
                sentence_dict[letter] = word
    
    sentence = ""
    i = 1
    
    for key in sorted(sentence_dict):
    
        sentence += sentence_dict[key]  
        
        if i < len(sentence_dict):
            sentence += " "     
        i += 1
        
    return sentence

Test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
Test.assert_equals(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
Test.assert_equals(order(""), "")