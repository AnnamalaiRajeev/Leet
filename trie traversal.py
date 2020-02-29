import time


class RootNode:
    def __init__(self, data=None):
        self.root = {}
        self.word_list = []

    def add_trie(self,word_list):
        root = self.root
        for word in word_list:
            current = root
            for char in word:
                current.setdefault(char,{})
                current = current[char]
            current['*'] = True

    def search_trie(self, word):
        current = self.root
        string = ''
        for char in word:
            if char in current:
                string += char
                current = current[char]
        if string == word and current.get('*'):
            return string
        else:
            return False

    def print_trie(self):
        print(self.root)

    def auto_complete(self, substring):

        current = self.root
        string = ''
        for char in substring:
            if char in current:
                string += char
                current = current[char]
        print(string)
        if current.get('*'):
            self.word_list.append(string)
        elif string == substring:
            self.recursive_complete(current, string)

        return_list = self.word_list
        self.word_list = []
        return return_list

    def recursive_complete(self, node, word):
        if node.get('*'):
            self.word_list.append(word)
        else:
            for char in node:
                print(word+char)
                time.sleep(1)
                if node[char] != True:
                    self.recursive_complete(node[char], word+char)


if __name__ == '__main__':
    trie_1 = RootNode()
    trie_1.add_trie(['dot', 'bot', 'hatter', 'fatter', 'hat', 'hallo', 'hallo kelly'])
    trie_1.print_trie()
    print(trie_1.search_trie('fatter'))
    print(trie_1.auto_complete('ha'))
