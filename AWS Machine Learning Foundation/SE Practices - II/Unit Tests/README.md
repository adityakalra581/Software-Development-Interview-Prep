## [pytest: helps you write better programs](https://docs.pytest.org/en/latest/)

The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.

Before you begin, make sure to run this command in your terminal to install pytest:
```
pip install -U pytest
```
Then, to run pytest, just enter:
```
pytest
```

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
