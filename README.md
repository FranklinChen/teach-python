# Exercises for helping to teach Python

Fork this repository, clone it to your local computer, then work on answers on your own branch, e.g.,

```console
$ git checkout -b my-answers
```

- Each exercise in the `problems/` directory has some sample doctests.
    - Remember to run your doctests in a file with

      ```console
      $ python -m doctest file.py
      ```

      or, if you want verbose output,

      ```console
      $ python -m doctest file.py -v
      ```
- You should write your own doctests also:
    - Think about and test the simplest possible cases (the "base cases").
    - Write more complicated cases, and think about how they reduce
      to the base cases.
- In many situations, you will want to write helper functions to call from the
  main one you are implementing.
- Use Python Tutor when having trouble visualizing what your code is doing.
