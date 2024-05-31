import pytest
from my_regex import MyRegex

FINDALL_STRING = """
    It's such a lovely day today.
    Where'd all the time go?
    Some weather we're having today, huh?
    Tomorrow never knows!
    Maybe today's just not my day.
    It's clobbering time!
"""

class TestRegEx:
    '''MyRegex in my_regex.py'''

    def test_matches_its_such_a_lovely_day(self):
        '''matches the string "It's such a lovely day today."'''
        my_regex = MyRegex()
        assert my_regex.fullmatch("It's such a lovely day today.")

    def test_matches_some_weather_were_having(self):
        '''matches the string "Some weather we're having today, huh?"'''
        my_regex = MyRegex()
        assert my_regex.fullmatch("Some weather we're having today, huh?")

    def test_matches_maybe_todays_not_my_day(self):
        '''matches the string "Maybe today's just not my day."'''
        my_regex = MyRegex()
        assert my_regex.fullmatch("Maybe today's just not my day.")

    def test_finds_all_matches(self):
        '''can be used to find these three strings and ONLY these three strings.'''
        my_regex = MyRegex()
        assert my_regex.findall(FINDALL_STRING) == [
            "It's such a lovely day today.",
            "Some weather we're having today, huh?",
            "Maybe today's just not my day.",
        ]
