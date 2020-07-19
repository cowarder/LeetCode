"""
问题描述：

207. Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


"""

"""
解题思路：
这个问题的本质上是判断有向图中是否存在环的问题
首先计算所有节点的入度，找到一个入度为0的节点，将节点所有的子节点入度减1，如果子节点的入度为0，将其添加到待判断的数组中
不断重复上述过程，直到所有的节点入度为0，如果存在一个节点的入度不为0，则说明存在环
"""


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        child = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for i, j in prerequisites:
            child[j].append(i)
            indegree[i] += 1
        res = [i for i in range(numCourses) if indegree[i] == 0]
        for i in res:
            for j in child[i]:
                indegree[j] -= 1
                if indegree[j]==0:
                    res.append(j)
        return len(res) == numCourses