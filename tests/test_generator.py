from buzz import generator

def test_sample_single_word():
    lijst = ('foo', 'bar', 'foobar')
    word = generator.sample(lijst)
    assert word in lijst

def test_sample_multiple_words():
    lijst = ('foo', 'bar', 'foobar')
    words = generator.sample(lijst, 2)
    assert len(words) == 2
    assert words[0] in lijst
    assert words[1] in lijst
    assert words[0] is not words[1]

def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5
