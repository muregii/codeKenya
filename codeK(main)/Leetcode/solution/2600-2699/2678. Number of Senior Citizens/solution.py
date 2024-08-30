class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        senior_count = 0
        
        for detail in details:
            age = int(detail[11:13])
            if age > 60:
                senior_count += 1
        
        return senior_count