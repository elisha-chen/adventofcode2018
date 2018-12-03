# adventday3.py
# Elisha Chen
# 12/3/18

import useful

"""Create a matrix and find overlaps of claims."""

def create_matrix():
    table = []
    for x in range(1000):
        table.append([])
        for y in range(1000):
            table[x].append(0)
        
    claims = useful.read_file("advent3data.txt")
    
    for claim in claims:
        left = int(claim[(claim.find("@") + 2): claim.find(",")])
        top = int(claim[(claim.find(",") + 1): claim.find(":")])
        for width in range (int(claim[(claim.find(":") + 2): claim.find("x")])):
            for height in range (int(claim[(claim.find("x") + 1):])):
                table[height + top][width + left] += 1
                
    claim_ids = []
    for x in range(len(claims)):
        claim_ids.append(x)
    for claim in claims:
        if (overlap_exists(table, claim)):
            print (claims.index(claim))
            claim_ids.remove(claims.index(claim))
            
    
    overlap = 0
    for x in range(1000):
        for y in range(1000):
            if (table[x][y] > 1):
                overlap += 1
                
    return claim_ids

def overlap_exists(table, claim):
    left = int(claim[(claim.find("@") + 2): claim.find(",")])
    top = int(claim[(claim.find(",") + 1): claim.find(":")])
    for width in range (int(claim[(claim.find(":") + 2): claim.find("x")])):
            for height in range (int(claim[(claim.find("x") + 1):])):
                if (table[height + top][width + left] > 1):
                    return True
                
    return False

print(create_matrix())