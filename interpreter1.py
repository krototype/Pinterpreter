
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

    def advance(self):
        self.pos+=1
        if self.pos>len(self.text)-1:
            self.current_char=None
        else:
            self.current_char=self.text[self.pos]


    def escape_space(self):
        #helps in escaping spaces
        if self.current_char==" ":
            print("space escaped")
            self.advance()
            self.escape_space()
        #self.advance()
        #if we don't get any spaces then we just return he result
        return None

    def total_integer(self):
        result=""
        if self.current_char==None:
            return result
        if self.current_char.isdigit():
            result+=self.current_char
            self.advance()
            #we did call the recursion after increasing the position by 1, so that it takes the new character
            result+=self.total_integer()
        return result

    def get_next_token(self):
        self.escape_space()

        if self.current_char==None:
            return Token("EOF",None)

        if self.current_char>="0" and self.current_char<="9":
            token=Token("Integer",int(self.total_integer()))
            #self.advance()
            return token

        if self.current_char=="+":
            token=Token("Plus",self.current_char)
            self.advance()
            #self.pos+=1
            return token

        if self.current_char=="-":
            token=Token("Minus",self.current_char)
            self.advance()
            #self.pos+=1
            return token

        return self.error()

    def match(self,token_type):
        if self.current_token.type==token_type:
            self.current_token=self.get_next_token()
        else:
            self.error()

    def check(self):
        #taking the first character
        self.current_char=self.text[self.pos]
        self.current_token=self.get_next_token()
        left=self.current_token
        self.match("Integer")#this takes the next character

        result=left.value
        #now every time match is calling the get next token
        while self.current_token.type in ("Plus","Minus"):
            op=self.current_token

            if op.value=="+":
                self.match("Plus")
                right = self.current_token
                self.match("Integer")
                result += right.value
            elif op.value=="-":
                self.match("Minus")
                right = self.current_token
                self.match("Integer")
                result -= right.value
            else:
                self.error()

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

