keypad = {0:".",1:"abc",2:"def",3:"ghi",4:"jkl",5:"mno",6:"pqrs",7:"tu",8:"vwx",9:"yz"}
class Solution:
    def helper(self,keys,i,n,ans):
        global keypad
        if i == n:
            print(ans)
            return
        for j in keypad[int(keys[i])]:
            self.helper(keys,i+1,n,ans+j)

    def keyPadCombis(self,keys):
        self.helper(keys,0,len(keys),"")
    
A = Solution()
A.keyPadCombis("12")