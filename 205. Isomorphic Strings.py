class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_t={}
        t_s={}
        
        for i in range(len(s)):
            e1, e2=s[i], t[i]

            if((e1 in s_t and s_t[e1]!=e2) or (e2 in t_s and t_s[e2]!=e1)):
                return False

            s_t[e1]=e2
            t_s[e2]=e1
        return True
