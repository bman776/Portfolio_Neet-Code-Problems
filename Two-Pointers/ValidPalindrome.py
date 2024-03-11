
class Solution:
    def isPalindrome(self, string:str) -> bool:
        i:int = 0
        j:int = len(string) - 1
        while (i<j):

            #DEBGUGGING:
            #print(ord(string[i]))
            #print(ord(string[j]))

            while not ((48 <= ord(string[i]) and ord(string[i]) <= 57) or 
                        (65 <= ord(string[i]) and ord(string[i]) <= 90) or 
                        (97 <= ord(string[i]) and ord(string[i]) <= 122)):
                i += 1
            while not ((48 <= ord(string[j]) and ord(string[j]) <= 57) or 
                        (65 <= ord(string[j]) and ord(string[j]) <= 90) or 
                        (97 <= ord(string[j]) and ord(string[j]) <= 122)):
                j -= 1
            
            if (string[i].lower() != string[j].lower()):
                return False
            
            i+=1
            j-=1
        
        return True