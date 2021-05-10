import random 

class Hand(object):
    def __init__(self, n):
        '''
        Initialize a Hand.

        n: integer, the size of the hand.
        '''
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.dealNewHand()

    def dealNewHand(self):
        '''
        Deals a new hand, and sets the hand attribute to the new hand.
        '''
        # Set self.hand to a new, empty dictionary
        self.hand = {}

        # Build the hand
        numVowels = self.HAND_SIZE // 3
    
        for i in range(numVowels):
            x = self.VOWELS[random.randrange(0,len(self.VOWELS))]
            self.hand[x] = self.hand.get(x, 0) + 1
        
        for i in range(numVowels, self.HAND_SIZE):    
            x = self.CONSONANTS[random.randrange(0,len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1
            
    def setDummyHand(self, handString):
        '''
        Allows you to set a dummy hand. Useful for testing your implementation.

        handString: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.

        This method converts sets the hand attribute to a dictionary
        containing the letters of handString.
        '''
        assert len(handString) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(len(handString), self.HAND_SIZE)
        self.hand = {}
        for char in handString:
            self.hand[char] = self.hand.get(char, 0) + 1


    def calculateLen(self):
        '''
        Calculate the length of the hand.
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans
    
    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = sorted(self.hand.keys())
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output

    def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.

        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.

        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.
        
        word: string
        returns: Boolean (if the word was or was not made)
        """
        # Make copy of hand dictionary
        hand2 = self.hand.copy()
        # If any letter in word not in hand dictionary, return False
        for letter in word:
            if letter not in self.hand:
                return False
        # Compare hand letters and their counts to letters and counts
        # within word (use a set because only need to go through each
        # unique character of word)
        for i in set(word):
            # If letter in hand dictionary is in the word, check to see
            # if the letter count in hand is greater than or equal to what
            # is in word
            if i in self.hand:
                # If not enough letters in hand to make word, return False
                if self.hand[i] < word.count(i):
                    # Return dictionary to what it originally was
                    # before update was run
                    self.hand = hand2
                    return False
                # If enough letters in hand to make word, update self.hand.
                # If it comes across the same letter again, it will skip over
                # this because it was updated previouly and the count of letters in
                # hand won't be greater than or equal to the count of the
                # same letters in the word
                if self.hand[i] >= word.count(i):
                    self.hand[i] = self.hand[i] - word.count(i)  
        # Enough letters are in hand dictionary to make word, so
        # return True
        return True
         
myHand = Hand(7)
#print(myHand)
#print(myHand.calculateLen())

myHand.setDummyHand('aazzmsp')
print(myHand)
print(myHand.calculateLen())

myHand.update('za')
#print(myHand.update('za'))
print(myHand)

print("-----------------------")

myHand2 = Hand(3)
print(myHand2)
print(myHand2.calculateLen())

myHand2.setDummyHand('abc')
print(myHand2)
print(myHand2.calculateLen())

myHand2.update('abcd')
print(myHand.update('z'))
print(myHand2)

print("-----------------------")
# Creates a new randomly generated hand
myHand.dealNewHand()
print(myHand)
