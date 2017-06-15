import sys
from template_python_cmd import hoge
from template_python_cmd.moge import noge

def main():
    print("Main function is called")
    hoge.hello()
    print(noge.f())

if __name__ == '__main__':
    main()
