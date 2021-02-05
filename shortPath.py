class Solution:
    def simplifyPath(path):
        path = path.split('/')
        while '' in path:
            path.remove('')
        while '.' in path:
            path.remove('.')
        ans = []
        for i in path:
            if i == "..":
                if len(ans) > 0:
                    ans.pop()
            else:
                ans.append(i)

        finalPath = '/'
        for i in range(len(ans)):
            if i == len(ans) - 1:
                finalPath += ans[i]
                break
            else:
                finalPath += ans[i]
                finalPath += '/'

        return(finalPath)

Solution.simplifyPath("/a/./b/../../c/")