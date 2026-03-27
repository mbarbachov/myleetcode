from math import ceil

class Solution:
    def __init__(self) -> None:
        # Array initiation
        self._nums_to_20 = ['', ' One', ' Two', ' Three', ' Four', ' Five', ' Six', ' Seven', ' Eight', ' Nine', ' Ten', ' Eleven',
                            ' Twelve', ' Thirteen', ' Fourteen', ' Fifteen', ' Sixteen', ' Seventeen', ' Eighteen', ' Nineteen']
        self._nums_to_100 = ['', ' Ten', ' Twenty', ' Thirty', ' Forty', ' Fifty', ' Sixty', ' Seventy', ' Eighty', ' Ninety']
        self._nums_everything_else = ['', ' Thousand', ' Million', ' Billion']

    def numberToWords(self, num: int) -> str:
        # Initiate return variable
        return_str = ''

        # Account for edge case
        if num == 0:
            return 'Zero'

        # Split number in sections of 3. (i.e. 1234567 -> ['1', '234', '567'])
        num = str(num)
        num_sections = ['000'] * (4 - ceil(len(num) / 3)) + list(
            reversed([''.join(reversed(''.join(reversed(num))[i:i + 3])) for i in range(0, len(num), 3)]))

        # Convert the numbers to words
        cnt = 4 - len(num_sections)
        for sec in num_sections:
            return_str += self.convert_100(sec) + (self._nums_everything_else[3 - cnt] if self.convert_100(sec) != '' else '')
            cnt += 1

        return return_str.strip()

    def convert_100(self, num: str) -> str:
        return_str = ''
        num = ''.join(['0'] * (3 - len(num)) + [_ for _ in num])
        if num[0] != '0':
            return_str += self._nums_to_20[int(num[0])] + ' Hundred'

        return_str += self._nums_to_100[int(num[1])] + self._nums_to_20[int(num[2])] if int(num[1:]) >= 20 else ''
        return_str += self._nums_to_20[int(num[1:])] if int(num[1:]) < 20 else ''
        
        return return_str

