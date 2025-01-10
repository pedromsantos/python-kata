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
	$(MAKE) tennis
	$(MAKE) gilded
	$(MAKE) raid
	$(MAKE) smelly
	$(MAKE) copier
	$(MAKE) esa
	$(MAKE) london

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

tennis:
	pytest src/tennis/tests

gilded:
	pytest src/gilded_rose/tests

raid:
	pytest src/raid/tests

smelly:
	pytest src/smelly_tic_tac_toe/tests

copier:
	pytest src/character_copier/tests

esa:
	pytest src/ESA_mars_rover/tests

social:
	pytest src/social_network/tests

london:
	pytest src/london_tic_tac_toe/tests
