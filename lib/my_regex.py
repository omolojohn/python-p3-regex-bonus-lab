import re

class MyRegex:
    @staticmethod
    def fullmatch(string):
        patterns = [
            r"It's such a lovely day today\.",
            r"Some weather we're having today, huh\?",
            r"Maybe today's just not my day\."
        ]
        return any(re.fullmatch(pattern, string) for pattern in patterns)
    
    @staticmethod
    def findall(string):
        patterns = [
            r"It's such a lovely day today\.",
            r"Some weather we're having today, huh\?",
            r"Maybe today's just not my day\."
        ]
        results = []
        for pattern in patterns:
            results.extend(re.findall(pattern, string))
        return results
