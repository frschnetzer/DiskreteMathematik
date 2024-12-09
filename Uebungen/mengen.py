A = {1,2,3,3,3,3,4}
B = {3,4, 5}
A == B
emptySet = set()
 
durchschnitt = A & B # Durschnitt -> logisches und
print(durchschnitt)
 
vereinigung = A | B # Vereinigung -> logisches oder
print(vereinigung)
 
differenz = A - B
print(differenz)
 
print(3 in A, 42 in A)