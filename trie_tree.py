class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_leaf = False
        self.word = None


class TrieTree:

    def __init__(self, word_list=None): 
        
        self.root = TrieNode()
        if word_list:
            for word in word_list:
                self.insert(word)
    
    def insert(self, word: str) -> None:
        node = self.root
        
        for c in word.lower(): 
            if c not in node.children:
                node.children[c] = TrieNode()
            
            node = node.children[c]
        
        node.is_leaf = True
        node.word = word
    
    def search(self, word: str) -> bool:
        node = self.root
        
        for c in word.lower():
            if c not in node.children:
                return False
            
            node = node.children[c]

        return node.is_leaf
    
    def starts_with(self, prefix:str) -> list[str]:
        node = self.root
        
        for c in prefix.lower():
            if c not in node.children:
                return []
            
            node = node.children[c]
        
        words = []
        self._collect_words(node, words)
        return words
    
    def _collect_words(self, node: TrieNode, words: list[str]) -> None:
        if node.is_leaf:
            words.append(node.word)
        
        for child_node in node.children.values():
            self._collect_words(child_node, words)
    
    def find_similar(self, word: str, max_distance: int = 2) -> list[str]:

        words = []

        # collect all words in the trie
        self._collect_words(self.root, words)
        
        similar_words = []
        for candidate in words:
            if self._minDistance(word.lower(), candidate.lower()) <= max_distance:
                similar_words.append(candidate)
        
        return similar_words
    
    def _minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (m+1) for i in range(n+1)]
        dp[0] = [i for i in range(m+1)]
        for i in range(n+1):
            dp[i][0] = i

        for i in range(1, n+1):
            for j in range(1, m+1):
                if word2[i-1] == word1[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]
   

