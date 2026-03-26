class Solution:
    def intToRoman(self, num: int) -> str:
        rom={1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',
        50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',
        1000:'M'}

        romno=""

        for key in reversed(rom):
            while num >= key:
                romno+= rom[key]
                num-=key

        

        return romno
