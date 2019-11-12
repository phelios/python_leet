class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i = numRows - 1
        zigzag = ""
        s_len = len(s)

        for row in range(numRows):
            index = 0
            next_key = row

            while next_key < s_len:
                zigzag += s[next_key]

                adj = self.get_gap_adj(numRows, row, index) * 2
                next_key = next_key + adj
                index += 1

        return zigzag

    def get_gap_adj(self, n, row, i):
        n_adj = n - 1

        zig_adj = n_adj - (row % n_adj)

        zag_adj = n_adj - zig_adj

        if zig_adj == n_adj:
            zag_adj = zig_adj

        zag = i % 2

        return zag_adj if zag else zig_adj
