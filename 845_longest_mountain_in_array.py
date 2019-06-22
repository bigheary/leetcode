class Solution(object):
    # AC
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        largest_cnt = 0
        cnt = 0
        up = 0
        down = 0
        if len(A) < 3:
            return 0
        for i in range(len(A) - 1):
            if up == 0 and down == 0:
                if A[i] < A[i+1]:
                    up = 1
                    cnt += 1
            elif up == 1 and down == 0:
                if A[i] < A[i+1]:
                    cnt += 1
                elif A[i] > A[i+1]:
                    cnt += 1
                    down = 1
                else:
                    cnt = 0
                    up = 0
            elif up == 1 and down == 1:
                if A[i] < A[i+1]:
                    down = 0
                    cnt += 1
                    if largest_cnt < cnt:
                        largest_cnt = cnt
                    # 新一轮重新计数
                    cnt = 1
                elif A[i] > A[i+1]:
                    cnt += 1
                else:
                    up = 0
                    down = 0
                    cnt += 1
                    if largest_cnt < cnt:
                        largest_cnt = cnt
                    cnt = 0
        if A[-2] > A[-1]:
            if up == 1:
                cnt += 1
                if largest_cnt < cnt:
                    largest_cnt = cnt
        return largest_cnt


if __name__=='__main__':
    sol = Solution()
    A = [875,884,239,731,723,685]
    print(sol.longestMountain(A))

