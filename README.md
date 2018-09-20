# sebak-transaction-compatibility-test

## Requirement

* Python 3.6 or higher
* go 1.0 or higher
* Godep 5.0 or higher

## Test

```
$ cd in_golang
$ dep ensure -v
```

Run test
```
$ python -m unittest discover -v -s ./
```
