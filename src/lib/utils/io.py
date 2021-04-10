class Input:
    @staticmethod
    def multichoice(question, choices):
        """
        Returns index of chosen option from list choices
        """

        outstring = question + '\n'
        outstring += '\n'.join([" {}) {}".format(i + 1, choice) for i, choice in enumerate(choices)])

        outstring += "\n\n: "

        choice = None

        while choice is None:
            try:
                choice = int(input(outstring)) - 1
                assert(choice in range(len(choices)))

            except (ValueError, AssertionError):
                print("Please choose a correct option\n\n")
                choice = None

        return choice

    @staticmethod
    def ask(question, default='', oftype=str):
        outstring = "{}\n\n: ".format(question)

        result = None
        while result is None:
            try:
                result = oftype(input(outstring))

            except (TypeError, ValueError):
                result = None
                print("Choice must be of type '{}'\n\n".format(oftype))

        return result if str(result).strip() != '' else default
