import pytest
from gilded_rose.kata import GildedRose, Item

def test_foo():
	Items = [Item(name="foo", sell_in=0, quality=0)]
	app = GildedRose(Items)
	app.update_quality()
	assert Items[0].name == "foo"
