from functools import reduce

class Instruction():
    def __init__(self, name, argv = []):
        self.name = name
        self.argv = argv

    def eval(self):
        if self.name == "mul":
            return reduce(lambda a,b: a*b, [int(x) for x in self.argv])
        else:
            return "invalid_instruction"
        
    def __str__(self):
        return self.name + "(" + ",".join(self.argv) + ")"

def parse(input_string):
    # could be done simply through regex
    # or we could create a dfa for this dsl! let's do that.

    matches = []
    tokenized_instructions = []

    # recursively parse
    def parse_loop(start_index):        
        VALID_SYMBOLS = [
            "mul",
            "do",
            "don't"
        ]

        stack = []
        parser_state = "READING"
        arg_state = ""
        arg_buffer = []
        instruction_buffer = []
        token_buffer = []

        i = start_index

        while i < len(input_string):
            char = input_string[i]
            if (char in ["m", "u", "l", "d", "o", "n", "t", "'"]) and parser_state == "READING":
                token_buffer += [char]
                print("Reading Token: " + char + " (token_buffer = " + "".join(token_buffer) + ")")

            elif parser_state == "READING" and char == "(" and "".join(token_buffer) in VALID_SYMBOLS:
                symbol = "".join(token_buffer)
                stack.append(symbol)
                if symbol == "mul":
                    parser_state = "ARGLIST"
                token_buffer = []
                arg_buffer = []
                print("Entering Func Call: " + symbol + " (stack = " + ",".join(stack) + ")")
            
            elif parser_state == "ARGLIST" and char.isdigit():
                token_buffer += [char]
                print("Reading Symbol in Arglist: " + char + " (token_buffer = " + "".join(token_buffer) + ")")

            elif parser_state == "ARGLIST" and char == ",":
                symbol = "".join(token_buffer)
                print("Read Full Symbol in Arglist: " + symbol + " (argbufffer = " + ",".join(arg_buffer) + ")")
                if len(symbol) > 3 or len(arg_buffer) > 1:
                    print("Failed - " + symbol + " / " + arg_buffer)
                    return -1, []
                token_buffer = []
                arg_buffer += [symbol]

            elif char == ")":
                if parser_state == "ARGLIST":
                    symbol = "".join(token_buffer)
                    print("Read Full Symbol in Arglist: " + symbol + " (argbufffer = " + ",".join(arg_buffer) + ")")
                    if len(symbol) > 3 or len(arg_buffer) > 1:
                        print("Failed - " + symbol + " / " + arg_buffer)
                        return -1, []
                    token_buffer = []
                    arg_buffer += [symbol]

                print("Finished Func Call: stack = " + ",".join(stack) + "), parser_state = " + parser_state + ", argbuffer = " + ",".join(arg_buffer))

                if parser_state == "ARGLIST" and len(stack) > 0 and stack[-1] == "mul" and len(arg_buffer) == 2:
                    return i, Instruction("mul", arg_buffer)
                elif parser_state == "READING" and len(stack) > 0 and stack[-1] == "do":
                    return i, Instruction("do")
                elif parser_state == "READING" and len(stack) > 0 and stack[-1] == "don't":
                    return i, Instruction("don't")
                else:
                    return -1, None
                
            else:
                # Invalid transition
                #print("Invalid Transition: " + parser_state + " / " + arg_state + " TO " + char)
                print("Invalid, exiting")
                return -1, []
            #print("Continuing Transition: " + parser_state + " / " + arg_state + " TO " + char)

            i += 1

        # Didn't match
        print("Didn't Match " + char)
        return -1, None

    i = 0
    while i < len(input_string):
        match_end, instruction = parse_loop(i)
        if match_end != -1:
            matches += [input_string[i:match_end + 1]]
            tokenized_instructions += [instruction]
            i = match_end
        else:
            i += 1

    return tokenized_instructions

def part2():
    f = open("input1.txt", "r")
    instructions: list[Instruction] = parse("".join(f.readlines()))
    # now we have to evaluate them
    on = True
    valid_sums = []
    for i in instructions:
        if i.name == "mul" and on:
            valid_sums += [i.eval()]
        elif i.name == "do":
            on = True
        elif i.name == "don't":
            on = False
    print(valid_sums)
    return reduce(lambda x,y: x+y, valid_sums)
        
print(part2())