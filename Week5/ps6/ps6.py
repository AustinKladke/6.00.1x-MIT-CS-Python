import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # Code should return (example, letters are shifted by one):
        # {"A" : "B", "B" : "C", "C" : "A", "a" : "b", "b" : "c", "c" : "a"}, etc.
        lower_dict = {}
        
        count_lower = 1
        for i in string.ascii_lowercase:
            lower_dict[i] = count_lower
            lower_dict[i] = ord(i)
            count_lower += 1
            
        for i in lower_dict:
            if lower_dict[i] + shift > 122:
                x = (122 - lower_dict[i])
                x2 = abs(shift - x)
                lower_dict[i] = chr(97 + x2 - 1)
            else:
                lower_dict[i] += shift
                lower_dict[i] = chr(lower_dict[i])

        upper_dict = {}
        
        count_upper = 1
        for i in string.ascii_uppercase:
            upper_dict[i] = count_upper
            upper_dict[i] = ord(i)
            count_upper += 1
        
        for i in upper_dict:
            if upper_dict[i] + shift > 90:
                x = (90 - upper_dict[i])
                x2 = abs(shift - x)
                upper_dict[i] = chr(65 + x2 - 1)
            else:
                upper_dict[i] += shift
                upper_dict[i] = chr(upper_dict[i])
                
        final_combined_dict = {}
        final_combined_dict.update(lower_dict)
        final_combined_dict.update(upper_dict)
        return final_combined_dict
        
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        new_dict = self.build_shift_dict(shift)
        new_word = ""
        for i in self.message_text:
            try:
                new_word += new_dict[i]
            except:
                new_word += i
        return new_word
            
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # Example of if 1 is the best shift value and the original coded
        # message is "abc"
        # Example return value: (1, "bcd")
        
        # Dictionary - Shift value = key, tuple of number of real words 
        # and decrypted message
        shift_dict = {}
        
        # Loop through and apply shift value (0 - 25) to the encrypted 
        # message to decrypt it. Keep track of how many real words are 
        # present in each decrypted message and add the information to 
        # the dictionary
        for i in range(0, 26):
            # Decrypt message with current shift
            decrypted_message = Message.apply_shift(self, i)
            # Find out how many real words are in the decrypted message
            real_words_count = 0
            word_lst = decrypted_message.split()
            for word in word_lst:
                if is_word(self.valid_words, word) == True:
                    real_words_count += 1
            # Add key and value to shift_dict dictionary
            shift_dict[i] = (real_words_count, decrypted_message)
        
        # Go through the dictionary and see which tuple has the greatest
        # number of real words. Choose the first one that you come across
        # and return a tuple with this structure:
        # (shift value, decrypted message)
        max_value = 0
        shift_value_max = 0
        for key, value in shift_dict.items():
            if value[0] > max_value:
                max_value = value[0]
                shift_value_max = key
        return (shift_value_max, shift_dict[shift_value_max][1])

# Message test
messagetext = Message("hello")
print(messagetext.get_message_text())
print(messagetext.build_shift_dict(2))
print(messagetext.apply_shift(2))

# Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())
print(plaintext.get_encrypting_dict())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())

# Decrypt a story
def decrypt_story():
    ciphertext_story = CiphertextMessage(get_story_string())
    return ciphertext_story.decrypt_message()
    
print(decrypt_story())