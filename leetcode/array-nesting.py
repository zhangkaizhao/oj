from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        longest_s_length = 0
        ss = []
        for k in nums:
            s = set()
            _k = k
            s_length = 0
            while True:
                n = nums[_k]

                calculated = False
                for _s in ss:
                    if n in _s:
                        calculated = True
                        break
                if calculated:
                    if s_length > longest_s_length:
                        longest_s_length = s_length
                    break

                if n in s:
                    if s_length > longest_s_length:
                        longest_s_length = s_length
                    ss.append(s)
                    break
                else:
                    s.add(n)
                    _k = n
                    s_length += 1
        return longest_s_length


if __name__ == '__main__':
    s = Solution()

    l1 = [5, 4, 0, 3, 1, 6, 2]
    r1 = s.arrayNesting(l1)
    print(r1)
    assert(r1 == 4)

    l2 = [0, 1, 2]
    r2 = s.arrayNesting(l2)
    print(r2)
    assert(r2 == 1)

    l3 = [0, 2, 1]
    r3 = s.arrayNesting(l3)
    print(r3)
    assert(r3 == 2)

    # for performance test
    from array_nesting_l4 import l4
    r4 = s.arrayNesting(l4)
    print(r4)
