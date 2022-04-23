
def print_import():
    print('임포트되어 사용되었습니다. ')
    
def print_main():
    print('직접 실행되었습니다. ')
    
if __name__ == '__main__':
    print_main()
else:
    print_import()
    