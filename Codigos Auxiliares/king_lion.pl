:- initialization(main).

main :- bicho(pumba).

% =========================
% FATOS BÁSICOS
% =========================

leao(simba).
leao(mufasa).
leao(scar).
leao(sarabi).
leao(nala).
javali(pumba).
suricato(timao).


% =========================
% Relações
% =========================
pai(mufasa, simba).
mae(sarabi, simba).
pai(simba, kiara).
mae(nala, kiara).
irmao(scar, mufasa).
amigo(simba, pumba).
amigo(pumba, timao).
casado(sarabi, mufasa).
casado(simba, nala).

% =========================
% PAPÉIS NO REINO
% =========================

rei(mufasa).
rainha(sarabi).
regente(scar).


% Herdeiro do trono
herdeiro(X) :- leao(X), rei(X), pai(X, Y), write(Y); write(X).
herdeiro(X) :- leao(X), rei(X); regente(Y), write(Y); write(X).
bicho(X) :- leao(X), write('Leao');javali(X), write('Javali');write('Suricato').
amigo(X, Y) :- amigo(Y, X).
irmao(X, Y) :- irmao(Y, X).
casado(X, Y) :- casado(Y, X).