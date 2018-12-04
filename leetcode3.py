def lengthOfLongestSubstring(s):
    dict1={}
    start=0
    maxlen=0
    len1=0
    if s is None or len(s)==0:
        return 0
    for i in range(len(s)):
        
        
        if s[i] not in dict1:
            dict1[s[i]]=i
            
        elif s[i] in dict1 and dict1[s[i]]>=start:
            start=dict1[s[i]]+1
            
            
            dict1[s[i]]=i
        else:
            dict1[s[i]]=i
        len1=i-start+1 
        
        maxlen=max(maxlen,len1)
    
            
            
    
    print (maxlen)


            
s="aabaab!bb"
lengthOfLongestSubstring(s)
        
