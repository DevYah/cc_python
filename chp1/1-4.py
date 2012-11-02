def is_anag(str1, str2):
  return sorted(str1) == sorted(str2)


str1 = 'ate'
str2 = 'eat'
print is_anag(str1, str2)

