def main():   
    def generate_table():
        a = []
        for p in [True, False]:
            for q in [True, False]:
                for r in [True, False]:
                    a.append([p,q,r])
        return a

    def equivalence_check(equivalenc1, equivalenc2):   
        for x in generate_table():  
            p, q, r = x[0], x[1], x[2]   
            if eval(equivalenc1) != eval(equivalenc2): # ersetzt strings durch local oder global variablen
                return False            
            return True 
        
    print(f"{equivalence_check("(p and (q or r))", "((p and q) or (p and r))")}")
    print(f"{equivalence_check("(not (p and q))", "((not p) or (not q))")}")   
   
    def equivalence_check_02(p,q,r):
        if (p and (q or r)) ==((p and q) or (p and r)):
            return True
        return False  
    
    def equivalence_check_03(p,q,r):
        if (not (p and q)) == ((not p) or (not q)):
            return True
        return False 
    
    for x in generate_table():  
        p, q, r = x[0], x[1], x[2]   
        print(equivalence_check_02(p,q,r))
        print(equivalence_check_03(p,q,r))
            
main()
    