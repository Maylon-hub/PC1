from cards import Card

def tests_field_access():
	c = Card("do something", "800199", "todo", 123)
	assert c.summary == "do something"
	assert c.owner == "800199"
	assert c.state == "todo"
	assert c.id == 123

def test_defaults():
	c = Card()
	assert c.summary is None
	assert c.owner is None
	assert c.state == "todo"
	assert c.id is None

def test_equality():
	c1 = Card("do something", "800199", "todo", 123)
	c2 = Card("do something", "800199", "todo", 123)
	assert c1 == c2

def test_equality_with_different_ids():
	c1 = Card("do something", "800199", "todo", 123)
	c2 = Card("do something", "800199", "todo", 4567)
	assert c1 == c2

def test_inequality():
	c1 = Card("do something", "800199", "todo", 123)
	c2 = Card("do something else", "800199", "todo", 123)
	assert c1 != c2

def test_inequality_with_different_owners():
	c1 = Card("do something", "800199", "todo", 123)
	c2 = Card("do something", "Maylon", "todo", 123)
	assert c1 != c2

def test_from_dict():
	c1 = Card("do something", "800199", "todo", 123)
	c2_dict = {
		"summary": "do something",
		"owner": "800199",
		"state": "todo",
		"id": 123
	}
	c2 = Card.from_dict(c2_dict)
	assert c1 == c2

def test_to_dict():
	c1 = Card("do something", "800199", "todo", 123)
	c2 = c1.to_dict()
	c2_expected = {
		"summary": "do something",
		"owner": "800199",
		"state": "todo",
		"id": 123
	}
	assert c2 == c2_expected