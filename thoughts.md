---
# Thoughts on problem i'm still working on 
---
- ### p169
- some sorta binary combinatorics problem, each '1' in the number's binary representation has a 'collapsing range'
- 1000 -> 200 -> 120 -> 112 (in bad binary notation)
- 8 -> 4+4 -> 4+2+2 -> 4+2+1+1
- but if a '1' collapses into another, smaller '1', we can no longer multiply the number of ways. instead we multiply by the number of ways minus one.
- example:
- 10 is 1010 in binary, the second 1 can 'collapse' once, becoming a 2.
- so we have 
---