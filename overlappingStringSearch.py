s = 'gkobobbobbbobobtyk'

searchTerm = 'bob'
results = 0
sub_len = len(searchTerm)
for i in range(len(s)):
    if s[i:i+sub_len] == searchTerm:
        results += 1
print results
