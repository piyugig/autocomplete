from redisearch import TextField, NumericField, Query, AutoCompleter, Suggestion

ac = AutoCompleter('ac', 'localhost')

ac.add_suggestions(
  Suggestion('google', 5.0),
  Suggestion('goo', 1.0)
)

#res = ac.get_suggestions('goo')

#res = ac.get_suggestions('goo', fuzzy = True)

