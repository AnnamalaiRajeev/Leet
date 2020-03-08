class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        targets = [x for _, x in sorted(zip(indexes,targets), key= lambda x: x[0])]
        sources = [x for _, x in sorted(zip(indexes, sources), key=lambda x: x[0])]
        indexes.sort()
        print(indexes, sources, targets)
        count = 0
        for index, index_value in enumerate(indexes):
            index_value += count
            print(index_value)
            in_front = S[:index_value]
            current = S[index_value: (index_value+len(sources[index]))]
            ahead = S[index_value+len(sources[index]):]
            print(in_front,current,ahead)
            if current == sources[index]:
                current = targets[index]
                S = in_front+current+ahead
                if len(sources[index]) >= len(targets[index]):
                    count -= len(sources[index]) - len(targets[index])
                elif len(sources[index]) < len(targets[index]):
                    count += len(targets[index]) - len(sources[index])

        return S

    def findReplaceString_1(self, S, indexes, sources, targets):
        s = list(S)
        for tuple in sorted(zip(indexes,sources,targets), key=lambda x: x[0], reverse=True):
            if s[tuple[0]:len(tuple[1])]




x = Solution()
y = x.findReplaceString("vmokgggqzp",[3,5,1],["kg","ggq","mo"],["s","so","bfr"])
y = x.findReplaceString("abcd",[0, 2],["a", "cd"],["eee", "ffff"])
print(y)

test = "vbfrssozp"