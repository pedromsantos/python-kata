# Makefile for Python Kata

.PHONY: test fizz fib leap prime roman stack tic yahtzee tennis gilded raid smelly copier esa social london deps format lint lint-fix types

deps:
	uv sync

format:
	uv run ruff format

lint:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

types:
	uv run pyright

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
	pytest src/fizz_buzz/test

fib:
	pytest src/fibonacci/test

leap:
	pytest src/leap_year/test

prime:
	pytest src/prime_factors/test

roman:
	pytest src/roman_numerals/test

stack:
	pytest src/stack_kata/test

tic:
	pytest src/tic_tac_toe/test

yahtzee:
	pytest src/yahtzee/test

tennis:
	pytest src/tennis/test

gilded:
	pytest src/gilded_rose/test

raid:
	pytest src/raid/test

smelly:
	pytest src/smelly_tic_tac_toe/test

copier:
	pytest src/character_copier/test

esa:
	pytest src/esa_mars_rover/test

social:
	pytest src/social_network/test

london:
	pytest src/london_tic_tac_toe/test
