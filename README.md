### Software Development Interview Prep

This Repository contains all the python Codes and Tutorials,past interview experience,expected questions based on skills and lot more curated over number of years on my experience as interviewee.

References:
(Starting Approach)[https://youtu.be/nw0m3-N9G5Y?si=I4K6gFiOpAuHEL14]

## Python

I have linked the important libraries in this readme anyways for reference as well.
 
 
### [Pylint](https://www.pylint.org/) 
- Pylint is a tool that checks for errors in Python code, tries to enforce a coding standard and looks for code smells. It can also look for certain type errors, it can recommend suggestions about how particular blocks can be refactored and can offer you details about the code's complexity.

### [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

PEP Stands for **Python Enhancement Proposal**. This document gives coding conventions for the Python code comprising the standard library in the main Python distribution. Please see the companion informational PEP describing style guidelines for the C code in the C implementation of Python.
This document and PEP 257 (Docstring Conventions) were adapted from Guido's original Python Style Guide essay, with some additions from Barry's style guide .
This style guide evolves over time as additional conventions are identified and past conventions are rendered obsolete by changes in the language itself.

### [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)

- Abstract

This PEP documents the semantics and conventions associated with Python docstrings.

- Rationale

The aim of this PEP is to standardize the high-level structure of docstrings: what they should contain, and how to say it (without touching on any markup syntax within docstrings). The PEP contains conventions, not laws or syntax.

### [pytest: helps you write better programs](https://docs.pytest.org/en/latest/)

The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.

An example of a simple test:
```

# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5
```

To execute it:
```
$ pytest
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-5.x.y, py-1.x.y, pluggy-0.x.y
cachedir: $PYTHON_PREFIX/.pytest_cache
rootdir: $REGENDOC_TMPDIR
collected 1 item

test_sample.py F                                                     [100%]

================================= FAILURES =================================
_______________________________ test_answer ________________________________

    def test_answer():
>       assert inc(3) == 5
E       assert 4 == 5
E        +  where 4 = inc(3)

test_sample.py:6: AssertionError
========================= short test summary info ==========================
FAILED test_sample.py::test_answer - assert 4 == 5
============================ 1 failed in 0.12s =============================
```
