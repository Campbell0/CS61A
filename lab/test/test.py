def commentary(n):
    def say():
        print(n)
        print(say)
    return say
    
