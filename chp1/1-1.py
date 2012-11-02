def is_unique(w):
  chars = []
  for s in w:
    if chars[s]:
      return False
    else:
      chars[s] = True
  return True

word = "yahia"
#print sorted(word)
print is_unique(word)

