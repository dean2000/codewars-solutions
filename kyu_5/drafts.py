class PokerHand(object):

	RESULT = ["Loss", "Tie", "Win"]
	CARDS = ['1','2','3','4','5','6','7','8','9','10','J','Q','K','A']
	RANKS = {'A': 14,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'T': 10,'J': 11,'Q': 12,'K': 13}

	def __init__(self, hand):
		self.hand = list(hand.replace(' ',''))
		
	def compare_with(self, other):
		other = list(other.replace(' ',''))

		def check_for_pairs(self):
			fixed_hand = list(i for index,i in enumerate(self.hand) if index % 2 == 0)
			fixed_other = list(i for index,i in enumerate(other) if index % 2 == 0)
			count_hand_pairs = list(set(["{}:{}".format(fixed_hand.count(i),i) for i in fixed_hand if fixed_hand.count(i) > 1]))
			count_other_pairs = list(set(["{}:{}".format(fixed_other.count(i),i) for i in fixed_other if fixed_other.count(i) > 1]))
			# if len(count_hand_pairs) == len(count_other_pairs):
				if max(count_hand_pairs)[0] == max(count_other_pairs)[0]:
					if (self.CARDS).index(max(count_hand_pairs)[2]) == (self.CARDS).index(max(count_other_pairs)[2]):
						return self.RESULT[1]
					elif (self.CARDS).index(max(count_hand_pairs)[2]) > (self.CARDS).index(max(count_other_pairs)[2]):
						return self.RESULT[2]
					else:
						return self.RESULT[0]
				elif max(count_hand_pairs)[0] > max(count_other_pairs)[0]:
					return self.RESULT[2]
				else:
					return self.RESULT[0]
			# return count_hand_pairs,count_other_pairs
		return check_for_pairs(self)

i = PokerHand("5S 5D 5H AS JS")
print(i.compare_with("AH AC 5H 5H 5S"))


import re

def increment_string(strng):
    try:
        strng_nums = strng[strng.find(re.search('[1-9]',strng)[0]):]
        before_len = len(strng_nums)
        strng = strng.replace(strng_nums,"")
        strng_nums = str(int(strng_nums) + 1)
        after_len = len(strng_nums)
        if after_len - before_len == 1 and strng[-1] == "0":
            strng = strng[:-1]
        return strng + strng_nums
    except:
        if len(strng) >= 1:
            if strng[-1] == "0":
                return strng[:-1] + '1'
            return strng + '1'
        return '1'

print (increment_string("foo125"))