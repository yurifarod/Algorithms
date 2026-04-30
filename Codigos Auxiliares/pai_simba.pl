:- initialization(imprime_pai(simba)).
imprime_pai(X):- leao(Y), pai(Y,X), write('o pai de '), write(X), write(' e '), write(Y),!.

%Fatos
leao(simba).
leao(mufasa).


%Predicados
pai(mufasa, simba).