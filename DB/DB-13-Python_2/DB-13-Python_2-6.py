import re


# patterns = ['term1', 'term2']
# text = "To jest string z term1, a nie z innym!"

# for _ in patterns:
#     print("Wyszkuje za:" + _)
#
# if re.search(_, text):
#     print("JEST")
# else:
#     print("NIE MA:(")


# split_term = '@'
# email = 'user@gmail.com'
# print(re.split(split_term,email))
#
# match = re.search('term1', text)
# print(match.start())
# print(type(match.start()))


# print(re.findall("match","test phrase match in match middle"))

def multi_re_find(patterns, phrase):
    for _ in patterns:
        print("Searching for pattern {}".format(_))
        print(re.findall(_, phrase))
        print("\n")


# test_phrase = "sdsd..sssddd..sdddsddd....dsds...dssssss...sddddd"
# test_pattern=["sd*"]
# test_pattern=["sd+"]
# test_pattern = ["sd{1,3}"]
# test_pattern=["s[sd]+"]

test_phrase = "This is a string! But is has punctuation. How can we remove it?"
# test_pattern=["[^!.?]+"]
test_pattern=["[^A-Z]+"] #[negacja+zakres od A-Z

test_phrase = "This is a string with number 1232123 and symbol #hashtag"
test_pattern=[r"\d+"]
test_pattern=[r"\D+"]
test_pattern=[r"\s+"]
test_pattern=[r"\S+"]
test_pattern=[r"\w+"]
test_pattern=[r"\W+"]

multi_re_find(test_pattern, test_phrase)