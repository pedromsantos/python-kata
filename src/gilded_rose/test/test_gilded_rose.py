from gilded_rose.kata import GildedRose, Item

def test_foo():
    items = [Item(name="foo", sell_in=0, quality=0)]
    app = GildedRose(items)
    app.update_quality()
    assert items[0].name == "foo"
