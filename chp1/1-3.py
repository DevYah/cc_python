def rem_dups(word):
  i = len(word)-1
  while i >= 0:
    if word[i] in word[0:i]:
      del word[i]
    i -=1
      
def rem_dups3(word):
  tail, i = 0, 0
  while i < len(word)-1:
    if word[i] in word[i+1:]:
      word[tail] = word[i]
      tail +=1
    i +=1
  
  del word[tail+1:]

def rem_dups2(word):
  hit = [0]*256
  tail = 0
  for c in word:
    if not hit[ord(c)]:
      hit[ord(c)] = 1
      word[tail] = c
      tail +=1

  del word[tail:]

word = list('yahya')
rem_dups(word)
print "".join(word)
word = list('yahya')
rem_dups2(word)
print "".join(word)
word = list('yahya')
rem_dups3(word)
print "".join(word)
