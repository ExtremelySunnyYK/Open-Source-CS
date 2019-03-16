
    
# python3


class QueryProcessor:
    """A simple hash table using the chaining scheme.
    Samples:
    >>> bucket_count, n = 5, 12
    >>> qp = QueryProcessor(bucket_count)
    >>> queries = [
    ... "add world",
    ... "add HellO",
    ... "check 4",
    ... "find World",
    ... "find world",
    ... "del world",
    ... "check 4",
    ... "del HellO",
    ... "add luck",
    ... "add GooD",
    ... "check 2",
    ... "del good"
    ... ]
    >>> process_queries(queries)
    HellO world
    no
    yes
    HellO
    GooD luck
    >>> # Explanation:
    >>> # The ASCII code of ’w’ is 119, for ’o’ it is 111, for ’r’ it is 114,
    >>> # for ’l’ it is 108, and for ’d’ it is 100. Thus, h("world") = 4.
    >>> # It turns out that the hash value of “HellO“ is also 4.
    >>> # We always insert in the beginning of the chain, so after adding
    >>> # “world” and then “HellO” in the same chain index 4, first goes
    >>> # “HellO” and then goes “world”. Of course, “World” is not found,
    >>> # and “world” is found, because the strings are case-sensitive,
    >>> # and the codes of ’W’ and ’w’ are different. After deleting “world”,
    >>> # only “HellO” is found in the chain 4.
    >>> # Similarly to “world” and “HellO”, after adding “luck” and
    >>> # “GooD” to the same chain 2, first goes “GooD” and then “luck”.
    """
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.buckets = [[] for _ in range(bucket_count)]

    def _hash_func(self, s):
        """Hash function."""
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def add(self, string):
        """Insert string into the table.
        If there is already such string in the hash table,
        then the query is ignored.
        """
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        if string not in bucket:
            self.buckets[hashed] = [string] + bucket

    def delete(self, string):
        """Removes string from the table.
        If there is no such string in the hash table,
        then the query is ignored.
        """
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i] == string:
                bucket.pop(i)
                break

    def find(self, string):
        """Looks up for the string in the table.
        Returns “yes” or “no” (without quotes) depending on whether
        the table contains string or not.
        """
        hashed = self._hash_func(string)
        if string in self.buckets[hashed]:
            return "yes"
        return "no"

    def check(self, i):
        """Returns the content of the i-th list in the table."""
        return self.buckets[i]


def process_queries(queries):
    """Helper function which reads queries from standard input,
    runs query processor and sends the results to standard output.
    """
    for query in queries:
        command, arg = query.split()
        if command == "add":
            qp.add(arg)
        elif command == "del":
            qp.delete(arg)
        elif command == "find":
            print(qp.find(arg))
        elif command == "check":
            arg = int(arg)
            print(" ".join(qp.check(arg)))


if __name__ == "__main__":
    bucket_count = int(input())
    n = int(input())

    qp = QueryProcessor(bucket_count)
    queries = [input() for i in range(n)]
    process_queries(queries)

