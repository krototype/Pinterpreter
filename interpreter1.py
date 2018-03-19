
class Token:
    def __init__(self,type,value):
        self.type=type#we would pass these 2 things to the object->Token(Integer,3)
        self.value=value
        print("type :" + str(self.type))
    def __str__(self):
        #after writing this you can access directly by writing obj.type or object.value
        return "Token({type},{value})".format(type=self.type,value=self.value)#just what it would print when asked to
    def __repr__(self):
        return self.__str__()

class Interpreter:
    def __init__(self,text):
        self.text=text
        self.pos=0
        self.current_token=None
        self.current_char=None

    def error(self):
        #generates the error message
        raise Exception("Error parsing input")


    def escape_space(self):
        #helps in escaping spaces
        text=self.text
        if self.pos > len(text) - 1:
            return None
        current_char=text[self.pos]
        if current_char==" ":
            self.pos += 1
            self.escape_space()

        #if we don't get any spaces then we just return he result
        return None

    def total_integer(self):
        result=""
        text=self.text
        if self.pos > len(text) - 1:
            return result
        current_char=text[self.pos]
        if current_char.isdigit():
            result+=current_char
            self.pos+=1
            #we did call the recursion after increasing the position by 1, so that it takes the new character
            result+=self.total_integer()
        return result

    def get_next_token(self):
        text=self.text
        self.escape_space()
        if self.pos>len(text)-1:
            return Token("EOF",None)

        current_char=text[self.pos]

        if current_char>="0" and current_char<="9":
            token=Token("Integer",int(self.total_integer()))
            #self.pos+=1
            return token

        if current_char=="+":
            token=Token("Plus",current_char)
            self.pos+=1
            return token

        if current_char=="-":
            token=Token("Minus",current_char)
            self.pos+=1
            return token

        return self.error()

    def match(self,token_type):
        if self.current_token.type==token_type:
            self.current_token=self.get_next_token()
        else:
            self.error()

    def check(self):
        #taking the first character
        self.current_token=self.get_next_token()
        left=self.current_token
        self.match("Integer")#this takes the next character

        #now every time match is calling the get next token
        op=self.current_token

        if op.value=="+":
            self.match("Plus")
        elif op.value=="-":
            self.match("Minus")
        else:
            self.error()

        #match is calling the get next token
        right=self.current_token
        self.match("Integer")

        print("left->"+str(left))
        print("right->" + str(right))
        if op.value=="+":
            result=left.value+right.value
        elif op.value=="-":
            result = left.value - right.value
        return result


def main():
    while 1:
        try:
            inp=input("enter->")
        except EOFError:
            print("error occured")
            break
        if inp.lower()=="end":
            print("Thankyou for using Pinterpreter")
            break
        if not inp:
            continue
        objinter=Interpreter(inp)
        result=objinter.check()
        print(result)
        print("If you want to end type\"end\" in the input without quotes")

if __name__=="__main__":
    main()

