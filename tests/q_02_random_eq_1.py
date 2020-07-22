test = {
  'name': 'Question 02_random_eq_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'h'
          >>> 'h' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # h should be an array with 4 elements.
          >>> len(h)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Values in h should all be either False or True
          >>> set(h).issubset([True, False])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Values in h should be True only where g has 1
          >>> np.all(h == (g == 1))
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
