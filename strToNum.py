def alphabet_position(text):
    ans = ""
    for letter in text:
        if(ord(letter.lower()) in range(97,123)):
            ans += str((ord(letter.lower()) - 96))
            ans += " "
    return ans.rstrip()

ans = alphabet_position("I am groot")
print(ans)