import random

#Some helper for source lists generation.

class SourceGenerationHelper:
    max_number: int
    min_number: int

    def __init__(self, min_number, max_number):
        """

        :param min_number: minimum possible number to generate
        :param max_number: maximum possible number to generate
        """
        assert isinstance(min_number, int) and isinstance(max_number, int), \
            'Min and max possible numbers should have int type.'
        self.min_number = min_number
        self.max_number = max_number

    def __generate_number_for_source(self):
        type = random.randint(0, 1)
        if type == 0:
            return random.randint(self.min_number, self.max_number)
        else:
            return random.uniform(self.min_number, self.max_number)


    def generate_good_source(self, elements_number: int):
        """

        :param elements_number: total number of elements in generated list
        :return: a list of random int or float numbers
        """
        result = []
        for i in range(elements_number):
            result.append(self.__generate_number_for_source())
        return result


# Probably not really rational method, but it doesn't really matter since it is only a helper.
    def generate_any_source(self, elements_number):
        """

        :param elements_number: total number of elements in generated list
        :return: not a list (like a sample of incorrect value), a list of random elements, which could be correct
        (int/float numbers) or incorrect (str)
        """
        result = []
        result_type = random.randint(0, 2)
        if result_type == 0:
            result = self.generate_good_source(elements_number)
        elif result_type == 1:
            for i in range(elements_number):
                is_bad = random.randint(0, 1)
                if (is_bad):
                    result.append('badstring')
                else:
                    result.append(self.__generate_number_for_source())
        else:
            result = 'badstring'

        return result



