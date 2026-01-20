# Version 0.6.0
**2026-01-20**

Add support for Python 3.14, keep dependencies up-to-date.

## What's Changed
### Dependency Changes
* Bump packaging from 24.1 to 25.0 by @teutoburg in https://github.com/AstarVienna/Pyckles/pull/39
* Bump pytest-cov from 6.2.1 to 7.0.0 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/40
* Bump pytest from 8.4.1 to 8.4.2 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/41
* Bump matplotlib from 3.10.1 to 3.10.6 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/43
* Bump numpydoc from 1.6.0 to 1.9.0 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/42
* Bump actions/upload-artifact from 4 to 5 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/44
* Bump actions/download-artifact from 5 to 6 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/45
* Bump matplotlib from 3.10.6 to 3.10.7 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/46
* Bump sphinx-book-theme from 1.1.0 to 1.1.4 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/47
* Bump synphot from 1.5.0 to 1.6.0 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/48
* Bump actions/checkout from 5 to 6 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/49
* Bump fonttools from 4.53.1 to 4.61.0 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/50
* Bump urllib3 from 2.5.0 to 2.6.0 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/51
* Bump actions/upload-artifact from 5 to 6 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/53
* Bump actions/download-artifact from 6 to 7 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/52
* Bump synphot from 1.6.0 to 1.6.1 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/54
* Bump numpydoc from 1.9.0 to 1.10.0 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/55
* Bump matplotlib from 3.10.7 to 3.10.8 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/56
* Bump pytest from 8.4.2 to 9.0.2 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/57
* Bump urllib3 from 2.6.0 to 2.6.3 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/58
* Allow Python 3.14, sync and update dependencies by @teutoburg in https://github.com/AstarVienna/Pyckles/pull/59

**Full Changelog**: https://github.com/AstarVienna/Pyckles/compare/v0.5.0...v0.6.0


# Version 0.5.0
**2025-09-12**

Add support for Python 3.13, Numpy 2 and Astropy 7.

## What's Changed
### Dependency Changes
* Allow numpy 2.x, keep 1.26.4 in the lock file by @teutoburg in https://github.com/AstarVienna/Pyckles/pull/27
* Bump requests from 2.32.3 to 2.32.4 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/23
* Bump urllib3 from 2.2.2 to 2.5.0 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/24
* Bump sphinxcontrib-apidoc from 0.4.0 to 0.6.0 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/31
* Bump pytest-cov from 6.0.0 to 6.2.1 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/33
* Bump pytest from 8.3.5 to 8.4.1 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/30
* Bump actions/setup-python from 5 to 6 by @dependabot[bot] in https://github.com/AstarVienna/Pyckles/pull/36
* Allow Python 3.13 and Astropy 7.x by @teutoburg in https://github.com/AstarVienna/Pyckles/pull/38
### Documentation Improvements
* Fix toml classifiers for PyPI by @teutoburg in https://github.com/AstarVienna/Pyckles/pull/37
### Other Changes
* Update workflows etc. by @teutoburg in https://github.com/AstarVienna/Pyckles/pull/28

**Full Changelog**: https://github.com/AstarVienna/Pyckles/compare/v0.4.1...v0.5.0


# Version 0.4.1
**2025-05-23**

## What's Changed
### Dependency Changes
* Bump jinja2 from 3.1.4 to 3.1.5 by @dependabot in https://github.com/AstarVienna/Pyckles/pull/17
* Bump pytest and pytest-cov to match ScopeSim by @teutoburg in https://github.com/AstarVienna/Pyckles/pull/19
* Bump jinja2 from 3.1.5 to 3.1.6 by @dependabot in https://github.com/AstarVienna/Pyckles/pull/20
### Other Changes
* Fail gracefully if Pyckles is not properly installed. by @hugobuddel in https://github.com/AstarVienna/Pyckles/pull/21

## New Contributors
* @dependabot made their first contribution in https://github.com/AstarVienna/Pyckles/pull/17

**Full Changelog**: https://github.com/AstarVienna/Pyckles/compare/v0.4.0...v0.4.1


# Version 0.4.0
**2024-10-23**

Python 3.10+ release to sync dependency versions with other @AstarVienna packages.

> [!IMPORTANT]
> The minimum required Python version for this package is now **3.10** (see Dependency Changes).

## What's Changed
### Other Changes
* Update workflow files by @teutoburg in https://github.com/AstarVienna/Pyckles/pull/14
* Drop support for Python 3.9, update dependencies by @teutoburg in https://github.com/AstarVienna/Pyckles/pull/15


**Full Changelog**: https://github.com/AstarVienna/Pyckles/compare/v0.3.0...v0.4.0


# Version 0.3.0
**2024-08-27**

Modernize package, general overhaul and refactoring.

## What's Changed
### New Features or Improvements
* General package overhaul by @teutoburg in https://github.com/AstarVienna/Pyckles/pull/7
* Use pooch for downloading and caching by @teutoburg in https://github.com/AstarVienna/Pyckles/pull/9

### Other Changes
* Switch to pyproject.toml by @hugobuddel in https://github.com/AstarVienna/Pyckles/pull/3
* Use DevOps repo by @hugobuddel in https://github.com/AstarVienna/Pyckles/pull/4
* Update dependencies by @hugobuddel in https://github.com/AstarVienna/Pyckles/pull/6
* Fix whitespace stripping in spectrum name by @teutoburg in https://github.com/AstarVienna/Pyckles/pull/8

## New Contributors
* @hugobuddel made their first contribution in https://github.com/AstarVienna/Pyckles/pull/3
* @teutoburg made their first contribution in https://github.com/AstarVienna/Pyckles/pull/7

**Full Changelog**: https://github.com/AstarVienna/Pyckles/compare/v0.2.0...v0.3.0

# Version 0.2.0
**2022-07-12**

Updated DLC server URL to new scopesim.univie.ac.at space

# Version 0.1.3
**2019-11-07**

First public version.
