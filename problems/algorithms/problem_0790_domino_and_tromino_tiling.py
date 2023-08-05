class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10 ** 9 + 7

        hasEvenCache = [False] * (n + 1)
        evenCache = [None] * (n + 1)

        def even(N):
            if N == 0:
                return 1

            if hasEvenCache[N]:
                return evenCache[N]

            count = 0
            count += even(N - 1)

            if N - 2 >= 0:
                count += even(N - 2)
                count += 2 * odd(N - 2)

            hasEvenCache[N] = True
            evenCache[N] = count % mod
            return evenCache[N]

        hasOddCache = [False] * (n + 1)
        OddCache = [None] * (n + 1)

        def odd(N):
            if N == 0:
                return 0
            if hasOddCache[N]:
                return OddCache[N]

            count = 0
            count += even(N - 1)
            count += odd(N - 1)

            hasOddCache[N] = True
            OddCache[N] = count % mod
            return OddCache[N]

        return even(n) % mod
