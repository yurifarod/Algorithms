:- initialization(main).
main :- (leao(tom) -> write('E leao'), nl;
write('Nao e leao'), nl),
halt.

%Fatos
leao(simba).
gato(tom).