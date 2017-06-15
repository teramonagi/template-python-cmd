import sys
import template_python_cmd.hoge as hoge
import template_python_cmd.moge.noge as noge


def main():
    print("Main function is called")
    hoge.hello()
    print(noge.f())
    print("Main function is finished")

if __name__ == '__main__':
    main()
