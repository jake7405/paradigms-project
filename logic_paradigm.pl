% This program demonstrates the logical programming paradigm
% Jacob Blackstone
% CSE 240 - Honors Contract
% Fall 2019

% Facts
cyclist(cole).
fast_cyclist(jean).
walking(adin).
running(corryn).
motorcycle(ahmed).
fast_motorcycle(sara).
car(jim).
fast_car(pam).
veryfast_car(chad).

% Rules
pedestrian(X) :- walking(X) ; cyclist(X) ; running(X) ; fast_cyclist(X).
stopped(X) :- car(X).
not_speeding(X) :- pedestrian(X) ; stopped(X).
ran_red(X) :- fast_cyclist(X) ; veryfast_car(X).
speeding(X) :- fast_motorcycle(X) ; fast_car(X) ; veryfast_car(X). 
criminal_speeding(X) :- (ran_red(X), speeding(X)) ; veryfast_car(X).
pulled_over(X) :- ran_red(X) ; speeding(X).
citation(X) :- pulled_over(X).
arrested(X) :- criminal_speeding(X).

% Goals
?- pedestrian(_X).
?- stopped(jim).
?- not_speeding(jean).
?- not_speeding(_X).
?- ran_red(_X).
?- speeding(_X).
?- criminal_speeding(_X).
?- pulled_over(_X).
?- arrested(_X).
?- arrested(chad).
?- citation(_X).


