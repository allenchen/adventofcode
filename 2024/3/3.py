from functools import reduce

def parse(input_string):
    # could be done simply through regex
    # or we could create a dfa for this dsl! let's do that.

    # DFA looks like
    # m -> u -> l -> ( -> \d -> , -> \d -> ) -> ACCEPT
    #                      |    ^     |    ^ 
    #                      V    |     V    |
    #                     \d -> |    \d -> |
    #                      |    |     |    |
    #                      V    |     V    |
    #                     \d -> |    \d -> |
    matches = []
    tokenized_instructions = []

    # recursively parse
    def parse_loop(start_index):
        """
        PARSER_STATES = [
            "START", 
            "M", 
            "U", 
            "L", 
            "OPEN_PAREN",
            "ARG_1", #ARG_1/ARG_2 should really be an arglist but w/e
            "ARG_2",
            "COMMA", 
            "CLOSE_PAREN"
        ]
        ARG_STATES = [
            "NONE",
            "FIRST_DIGIT",
            "SECOND_DIGIT",
            "THIRD_DIGIT"
        ]
        """
        
        parser_state = "START"
        arg_state = ""
        arg_buffer = []
        instruction_buffer = []

        i = start_index

        while i < len(input_string):
            char = input_string[i]
            if char == "m":
                parser_state = "M"

            elif parser_state == "M" and char == "u":
                parser_state = "U"

            elif parser_state == "U" and char == "l":
                parser_state = "L"

            elif parser_state == "L" and char == "(":
                parser_state = "OPEN_PAREN"
                arg_state = "NONE"
                arg_buffer = []

            elif parser_state == "OPEN_PAREN" and char.isdigit():
                parser_state = "ARG_1"
                arg_state = "FIRST_DIGIT"
                arg_buffer += [char]

            elif parser_state == "ARG_1" and arg_state == "FIRST_DIGIT" and char.isdigit():
                arg_state = "SECOND_DIGIT"
                arg_buffer += [char]

            elif parser_state == "ARG_1" and arg_state == "SECOND_DIGIT" and char.isdigit():
                arg_state = "THIRD_DIGIT"
                arg_buffer += [char]

            # if arg_state == THIRD_DIGIT and lookahead token isdigit, we're rejecting
            
            elif parser_state == "ARG_1" and char == ",":
                parser_state = "COMMA"
                instruction_buffer += [int("".join(arg_buffer))]
                arg_state = "NONE"
                arg_buffer = []

            elif parser_state == "COMMA" and char.isdigit():
                parser_state = "ARG_2"
                arg_state = "FIRST_DIGIT"
                arg_buffer += [char]

            elif parser_state == "ARG_2" and arg_state == "FIRST_DIGIT" and char.isdigit():
                arg_state = "SECOND_DIGIT"
                arg_buffer += [char]

            elif parser_state == "ARG_2" and arg_state == "SECOND_DIGIT" and char.isdigit():
                arg_state = "THIRD_DIGIT"
                arg_buffer += [char]

            # if arg_state == THIRD_DIGIT and lookahead token isdigit, we're rejecting

            elif parser_state == "ARG_2" and char == ")":
                parser_state = "CLOSE_PAREN"
                instruction_buffer += [int("".join(arg_buffer))]
                arg_state = "NONE"
                return i, instruction_buffer
            else:
                # Invalid transition
                #print("Invalid Transition: " + parser_state + " / " + arg_state + " TO " + char)
                return -1, []
            #print("Continuing Transition: " + parser_state + " / " + arg_state + " TO " + char)

            i += 1

        # Didn't match
        return -1, []

    i = 0
    while i < len(input_string):
        match_end, instruction = parse_loop(i)
        if match_end != -1:
            matches += [input_string[i:match_end + 1]]
            tokenized_instructions += [instruction]
        i += 1

    return tokenized_instructions

def part1():
    f = open("input1.txt", "r")
    instructions = parse("".join(f.readlines()))
    return reduce(lambda x,y:x+y, [reduce(lambda x,y:x*y, instruction) for instruction in instructions])

print(part1())