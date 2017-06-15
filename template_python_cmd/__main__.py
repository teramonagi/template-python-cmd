import sys
from template_python_cmd import hoge
from template_python_cmd.moge.noge import noge


def main():
    print("Main function is called")
    hoge.hello()
    print(noge.f())
    print("Main function is finished")

if __name__ == '__main__':
    main()
