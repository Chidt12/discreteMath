class Bottle:
    def __init__(self, waterin, waterlimit):
        self.previous = waterin
        self.waterin = waterin
        self.waterlimit = waterlimit

    def pourwater(self, anotherbottle):
        if self.waterin != 0:
            self.previous = self.waterin
            anotherbottle.previous = anotherbottle.waterin
            if self.waterin + anotherbottle.waterin <= anotherbottle.waterlimit:
                anotherbottle.waterin += self.waterin
                self.waterin = 0
            else:
                self.waterin = (self.waterin + anotherbottle.waterin - anotherbottle.waterlimit)
                anotherbottle.waterin = anotherbottle.waterlimit

    def backprevious(self, anotherbottle):
        self.waterin = self.previous
        anotherbottle.waterin = anotherbottle.previous


array_situations = []

def swapPourWater(array_bottle, a, b):
    situation = []
    for i in range(len(array_bottle)):
        situation.append(array_bottle[i].waterin)
    if situation not in array_situations:
        array_situations.append(situation)
    else:
        print("previous___",array_bottle[a].previous," ",array_bottle[b].previous)
        return array_bottle[a].backprevious(array_bottle[b])
    if situation[1] == 2 or situation[2] == 2: 
        # TRạng thái mà bình 2 hoặc bình 3 chứa 2 lít nước, có thể thay 2 lít nước bằng số khác
        return True
    for i in range(len(array_bottle)):
        for j in range(len(array_bottle)):
            if i != j:
                array_bottle[i].pourwater(array_bottle[j])
                print(i,j,"_waterin__",array_bottle[0].waterin, array_bottle[1].waterin, array_bottle[2].waterin)
                status = swapPourWater(array_bottle, i, j)
                if status == True:
                    return status
    return status

swapPourWater([Bottle(0,10), Bottle(7,7), Bottle(4,4)], 0, 4) 
# input dau vao a b bat ki, Bottle có 2 thông số, 
# số đầu là lượng nước có, số sau là giới hạn đựng, chỉ áp dụng cho 3 bình
print(array_situations)
# Array_situation chính là kêt quả lượng nước lần lượt ở 3 chai cho đến khi đạt được trạng thái yêu cầu