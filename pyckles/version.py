from importlib import metadata
version = metadata.version(__package__)
date = 'xxxx-xx-xx 17:00:00 GMT'
yaml_descriptions = """
- version : 0.3
  date : xxxx-xx-xx
  comment: Modernize package
  - Move to pyproject.toml [#3]
  - Test on windows [#3]

- version : 0.2
  date : 2022-07-12
  comment : Updated DLC server URL to new scopesim.univie.ac.at space
"""