
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

class Lexer:
    def __init__(self,text):
        self.text=text
        self.pos=0
        self.current_char = self.text[self.pos]

    def error(self):
        #generates the error message
        raise Exception("Invalid character")

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
            return token

        if self.current_char=="+":
            token=Token("Plus",self.current_char)
            self.advance()
            return token

        if self.current_char=="-":
            token=Token("Minus",self.current_char)
            self.advance()
            return token

        if self.current_char=="*":
            token=Token("Multiply",self.current_char)
            self.advance()
            return token

        if self.current_char=="/":
            token=Token("Divide",self.current_char)
            self.advance()
            return token

        return self.error()


class Interpreter:
    def __init__(self,lexer):
        self.lexer=lexer
        self.current_token=self.lexer.get_next_token()

    def error(self):
        #generates the error message
        raise Exception("Invalid syntax")


    def match(self,token_type):
        if self.current_token.type==token_type:
            self.current_token=self.lexer.get_next_token()
        else:
            self.error()

    def divfactor(self):
        token = self.current_token
        self.match("Integer")
        return token.value

    def factor(self):
        result = self.divfactor()

        while self.current_token.type == "Divide":
            self.match("Divide")
            result /= self.divfactor()

        return result

    def term(self):
        result=self.factor()

        while self.current_token.type=="Multiply":
            self.match("Multiply")
            result *= self.factor()

        return result

    def expression(self):
        #taking the first character

        result=self.term()
        #now every time match is calling the get next token
        while self.current_token.type in ("Plus","Minus"):
            op=self.current_token

            if op.value=="+":
                self.match("Plus")
                result += self.term()
            elif op.value=="-":
                self.match("Minus")
                result -= self.term()
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

        lexer=Lexer(inp)
        objinter=Interpreter(lexer)
        result=objinter.expression()
        print(result)
        print("If you want to end type\"end\" in the input without quotes")

if __name__=="__main__":
    main()

