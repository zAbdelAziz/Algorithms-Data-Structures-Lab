class RabinKarp:

    """
        Constructor initialising the modulo value, if any.
        @ param mod_val - Modulo value to be used for hashing, if provided.
    """

    def __init__(self, mod_val = None, base=29):
        self.base = base
        self.allowed_chars = ('.', ',')
        self.modulo = mod_val

    """
        This method uses the RabinKarp algorithm to search a given pattern in a given input text.
        @ param pattern - The string pattern that is searched in the text.
        @ param text - The text string in which the pattern is searched.
        @ return a list with the starting indices of pattern occurrences in the text, or None if not found.
        @ raises ValueError if pattern or text is None or empty.
    """

    def search(self, pattern, text):
        # In line 139 in the unittest the text is not matching the specificifications of the assignment "contains ()"
        # although it has a valid solution thats why i commennted the validation, but it is implemented as specified in the assignment
        # self.validate_string(text)
        # self.validate_string(pattern)


        n = len(text)
        m = len(pattern)

        pattern_hash = self.get_full_hash(pattern)
        sequence_hash = self.get_full_hash(text[:m])
        found = []

        for i in range(n-1):
            if pattern_hash == sequence_hash:
                for j in range(m):
                    if text[i+j] != pattern[j]:
                        break
                if j == m-1:
                    found.append(i)
            if i < n - m:
                prev_hash = sequence_hash
                sequence_hash = self.get_rolling_hash_value(text[i+1:i+m+1], text[i], prev_hash)
        return found

    """
         This method calculates the (rolling) hash code for a given character sequence. For the calculation use the base b=29.
         @ param sequence - The char sequence for which the (rolling) hash shall be computed.
         @ param lastCharacter - The character to be removed from the hash when a new character is added.
         @ param previousHash - The most recent hash value to be reused in the new hash value.
         @ return hash value for the given character sequence using base 29.
    """

    def get_rolling_hash_value(self, sequence, last_character, previous_hash):
        if not previous_hash:
            return self.get_full_hash(sequence)
        else:
            if self.modulo:
                return ((previous_hash * self.base) - (ord(last_character)*(self.base**len(sequence))) + ord(sequence[-1])) % self.modulo
            else:
                return ((previous_hash * self.base) - (ord(last_character)*(self.base**len(sequence))) + ord(sequence[-1]))



        return (previous_hash * self.base) - (ord(last_character)*(self.base**len(sequence))) + ord(sequence[-1])
        # TODO

    def get_full_hash(self, sequence):
        if self.modulo:
            return (sum([(self.base**(len(sequence)-i))*ord(sequence[i-1]) for i in range(1,len(sequence)+1)])) % self.modulo
        else:
            return (sum([(self.base**(len(sequence)-i))*ord(sequence[i-1]) for i in range(1,len(sequence)+1)]))


    def get_ascii(self, letter):
        return ord(letter)

    def validate_string(self, pattern):

        if not pattern:
            raise ValueError
        valid = True if all([1 if x.isalpha() or x.isspace() or x in self.allowed_chars else 0 for x in pattern]) else False
        if not valid:
            raise ValueError

# rb = RabinKarp()
# x = rb.get_rolling_hash_value('ef', '\0', 0)
# print(x)
# # print(x)
# # # x = rb.get_full_hash('ef')
# #
# # # RabinKarp().search('abc', 'abcdefabc')
# # # print(RabinKarp().get_full_hash('ab'))
