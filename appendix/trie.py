class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def print_trie(self):
        def dfs(node, prefix="", depth=0):
            for ch, child in sorted(node.children.items()):
                marker = "✓" if child.is_word else ""
                print("  " * depth + f"└─ {ch} {marker}")
                dfs(child, prefix + ch, depth + 1)

        print("(root)")
        dfs(self.root)

trie = Trie()
words = ["cat", "car", "care", "card", "dog"]
for w in words:
    trie.insert(w)
trie.print_trie()
print(f"ca? { trie.starts_with('ca') }")


