class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # Split the version strings into lists of revisions
        v1 = [int(x) for x in version1.split(".")]
        v2 = [int(x) for x in version2.split(".")]
        
        # Compare revisions one by one
        for i in range(max(len(v1), len(v2))):
            rev1 = v1[i] if i < len(v1) else 0
            rev2 = v2[i] if i < len(v2) else 0
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
        
        # All revisions are equal
        return 0