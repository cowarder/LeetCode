"""
问题描述：

96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""

"""
解题思路：
问题是求解二叉搜索树的所有可能的排列组合
本质上是动态规划问题，需要推倒：
假设Node(n)表示n个节点的排列组合数目
G(i, n)表示i作为根结点，n个节点的排列数目
G(i, n)来讲，左子树节点数目为i-1，右子树节点数目n-i
G(i, n)=Node(i-1)*Node(n-i)
而Node(N) = G(1, n)+G(2, n) + G(3, n) +......+G(n, n)
综合上述两个公式；
Node(n) = Node(1-1)*Node(n-1)+Node(2-1)*Node(n-2)...+Node(n-1)*Node(n-n)
特殊情况是Node(0)，因为空节点的情况只有一种，所以也是1
"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = [0] * (n + 1)
        num[1] = 1
        num[0] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                num[i] += num[j - 1] * num[i - j]
        return num[n]
