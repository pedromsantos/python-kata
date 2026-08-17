.PHONY: test tests fizz stats anagrams fib leap prime roman stack tic yahtzee tennis gilded raid smelly copier esa social london golf smellyrover smellycart smellyyahtzee cart katacombs deps format lint lint-fix types

test:
	uv run pytest --cov=src

deps:
	uv sync --locked --all-extras --dev

format:
	uv run ruff format

lint:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

types:
	uv run pyright

tests:
	$(MAKE) fizz
	$(MAKE) stats
	$(MAKE) anagrams
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
	$(MAKE) golf
	$(MAKE) smellyrover
	$(MAKE) smellycart
	$(MAKE) smellyyahtzee

fizz:
	pytest src/fizz_buzz/test

stats:
	pytest src/stats_calculator/test

anagrams:
	pytest src/anagrams/test

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

golf:
	pytest src/refactoring_golf

smellyrover:
	pytest src/smelly_mars_rover/test

smellycart:
	pytest src/smelly_shopping_cart/test

smellyyahtzee:
	pytest src/smelly_yahtzee/test

cart:
	pytest src/shopping_cart

katacombs:
	pytest src/katacombs
