# Makefile for Python Kata

.PHONY: test

test:  # Make test the default task
	$(MAKE) fizz
	$(MAKE) fib
	$(MAKE) leap
	$(MAKE) prime
	$(MAKE) roman
	$(MAKE) stack
	$(MAKE) tic
	$(MAKE) yahtzee

fizz:
	pytest src/fizz_buzz/tests

fib:
	pytest src/fibonacci/tests

leap:
	pytest src/leap_year/tests

prime:
	pytest src/prime_factors/tests

roman:
	pytest src/roman_numerals/tests

stack:
	pytest src/stack_kata/tests

tic:
	pytest src/tic_tac_toe/tests

yahtzee:
	pytest src/yahtzee/tests