# template-python-cmd
Template package for Python cmd tool.

## Install
From github
```
$ pip install git+https://github.com/teramonagi/template-python-cmd
```

Local
```
$ cd <path to template-python-cmd>
$ pip .
```

## Use as python script

Run main script(__main__.py) automatically
```
$ python -m template_python_cmd
```

## Use as library
```
$ import template_python_cmd    .hoge
$ template_python_cmd.hoge.hello()
$ import template_python_cmd.moge.noge
$ template_python_cmd.moge.noge.f()
$ from template_python_cmd.moge import noge
$ noge.f()
```

