class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_mapping={}
        t_mapping={}
        
        for i in range(len(s)):
            e1,e2=s_mapping[i],t_mapping[i]
            if(e1 in s_mapping and s_mapping[e1]!=e2) or (e2 in t_mapping and t_mapping[e2]!=e1):
                return False
            s_mapping[e1]=e2
            t_mapping[e2]=e1
