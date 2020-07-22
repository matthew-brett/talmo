test = {
  'name': 'Question 01_four_random',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'g'
          >>> 'g' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # g should be an array with 4 elements.
          >>> len(g)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # numbers in g should all be either 0 or 1
          >>> np.all(g >= 0)
          True
          >>> np.all(g <= 1)
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
