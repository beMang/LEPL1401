import search


def test_readfile():
    assert search.readfile("text_example_1.txt") == ['While the Congress of the Republic endlessly debates',
                                                     'this alarming chain of events, the Supreme Chancellor has', 'secretly dispatched two Jedi Knights.']
    assert search.readfile("text_example_2.txt") == [
        'Turmoil has engulfed the Galactic Republic. The taxation of trade routes to outlying star systems is in dispute.']


def test_get_words():
    assert search.get_words("Turmoil has engulfed the Galactic Republic.") == [
        "turmoil", "has", "engulfed", "the", "galactic", "republic"]
    assert search.get_words(search.readfile("text_example_1.txt")[0]) == [
        "while", "the", "congress", "of", "the", "republic", "endlessly", "debates"]
    assert search.get_words(search.readfile("text_example_1.txt")[1]) == [
        'this', 'alarming', 'chain', 'of', 'events', 'the', 'supreme', 'chancellor', 'has']
    assert search.get_words(search.readfile("text_example_2.txt")[0]) == [
        'turmoil', 'has', 'engulfed', 'the', 'galactic', 'republic', 'the', 'taxation', 'of', 'trade', 'routes', 'to', 'outlying', 'star', 'systems', 'is', 'in', 'dispute']


def test_create_index():
    search.create_index("text_example_1.txt") == {'while': [1], 'the': [1, 1], 'congress': [1], 'of': [1], 'republic': [1], 'endlessly': [1], 'debates': [1], 'this': [
        2], 'alarming': [2], 'chain': [2], 'events': [2], 'supreme': [2], 'chancellor': [2], 'has': [2], 'secretly': [3], 'dispatched': [3], 'two': [3], 'jedi': [3], 'knights': [3]}
    search.create_index("text_example_2.txt") == {'turmoil': [1], 'has': [1], 'engulfed': [1], 'the': [1, 1], 'galactic': [1], 'republic': [1], 'taxation': [
        1], 'of': [1], 'trade': [1], 'routes': [1], 'to': [1], 'outlying': [1], 'star': [1], 'systems': [1], 'is': [1], 'in': [1], 'dispute': [1]}


def test_get_lines():
    assert search.get_lines(['while', 'the'], {'while': [2, 37], 'the': [
                            1, 37, 56], 'congress': [1, 43]}) == [37]
    assert search.get_lines(['of'], search.create_index(
        "text_example_1.txt")) == [0, 1]
    assert search.get_lines(['the', 'of'], search.create_index(
        "text_example_1.txt")) == [0, 1]
    assert search.get_lines(['events', 'chain'],
                            search.create_index("text_example_1.txt")) == [1]


test_get_words()
test_readfile()
test_create_index()
test_get_lines()
