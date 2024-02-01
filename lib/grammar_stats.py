class GrammarStats:
    def __init__(self):
        self.good = 0
        self.total = 0

    def check(self, text):

        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        punctuation = "?!."
        if text[0].isupper() and text[-1] in punctuation:
            self.good += 1
            self.total += 1
            return True
        self.total += 1
        return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        return round((self.good / self.total) * 100)