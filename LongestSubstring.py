def lengthOfLongestSubstring(s):
        tmp_string=""
        max_string=0
        for i in range(len(s)):
            tmp_string=s[i]
            for j in range(i+1,len(s)):
                if s[j] not in tmp_string:
                    tmp_string+=s[j]
                else:
                    break
            max_string=max(max_string,len(tmp_string))
                
        return max_string
      
input_string = input("Enter the String: ")
lengthOfLongestSubstring(input_string)
