def reverse_even_string(sentence):
    
    words = sentence.split()

    for i in range(len(words)):
        if i % 2 == 1:  
            words[i] = words[i][::-1] 
 
    reversed_sentence = ' '.join(words)

    return reversed_sentence

sentence = "the sky is blue"
result = reverse_even_string(sentence)
print(result)
