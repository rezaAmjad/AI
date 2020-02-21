import Node

class TrigramModel:
    word_list = []
    h_map = []
    sentence = []
    first_word_index = []
    second_word_index = []
    third_word_index = []


    def text_editor(self):
        # read_files = glob.glob("*.txt")
        # with open("result.txt", "wb") as outfile:
        #     for f in read_files:
        #         with open(f, "rb") as infile:
        #             outfile.write(infile.read())
        # with open("result.txt", 'r') as f:
        #     for line in f:
        #         for word in line.split():
        #             self.word_list.append(word.lower())

        with open("doyle-27.txt", 'r') as f:
            for line in f:
                for word in line.split():
                    self.word_list.append(word.lower())

    def print_list(self):
        for word in self.word_list:
            print(word)

    def build_model(self):

        for i in range(2, len(self.word_list)):
            print("value of i:", i)
            if self.does_not_contain(self.h_map, self.word_list[i - 2]) or len(self.h_map) == 0:
                self.add_new_item(self.h_map, self.word_list[i - 2])
                index = self.get_index(self.h_map, self.word_list[i - 2])
                self.add_new_item(self.h_map[index].list, self.word_list[i - 1])
                index2 = self.get_index(self.h_map[index].list, self.word_list[i - 1])
                self.add_new_item(self.h_map[index].list[index2].list, self.word_list[i])
            else:
                self.update(self.h_map, self.word_list[i - 2])
                index = self.get_index(self.h_map, self.word_list[i - 2])
                if self.does_not_contain(self.h_map[index].list, self.word_list[i - 1]):
                    self.add_new_item(self.h_map[index].list, self.word_list[i - 1])
                else:
                    self.update(self.h_map[index].list, self.word_list[i - 1])
                index2 = self.get_index(self.h_map[index].list, self.word_list[i - 1])
                if self.does_not_contain(self.h_map[index].list[index2].list, self.word_list[i]):
                    self.add_new_item(self.h_map[index].list[index2].list, self.word_list[i])
                else:
                    self.update(self.h_map[index].list[index2].list, self.word_list[i])

    def add_new_item(self, lst, word):
        w = Node.node(word)
        w.count += 1
        lst.append(w)

    def update(self, lst, word):
        index = self.get_index(lst, word)
        lst[index].count += 1

    def get_index(self, lst, w):
        index = None
        for word in lst:
            if word.word == w:
                index = lst.index(word)
        return index

    def cal_prob(self, lst):
        total = 0
        if len(lst) == 0:
            print("this list is empty")
        highest_value_word = lst[0]
        for word in lst:
            total += word.count
        for word in lst:
            word.probability = word.count/total
        for word in lst:
            if word.probability > highest_value_word.probability:
                highest_value_word = word
        return highest_value_word

    def best_combination(self):
        if len(self.h_map) == 0:
            print("hash map is empty")
        first_word = self.cal_prob(self.h_map)
        second_word = self.cal_prob(first_word.list)
        third_word = self.cal_prob(second_word.list)
        combination = first_word.word + ' ' + second_word.word + ' ' + third_word.word
        index = self.get_index(self.h_map, first_word)
        self.h_map.remove(first_word)
        return combination

    def create_story(self):
        story_list = []
        self.text_editor()
        self.build_model()
        for i in range(0, 334):
            result = self.best_combination()
            story_list.append(result)
        print(len(story_list))
        with open("story2.txt", "w") as f:
            for string in story_list:
                f.write(string)
                f.write(" ")
            f.close()

    def does_not_contain(self, lst, word):
        result = True
        for w in lst:
            if w.word == word:
                result = False
        return result

g = TrigramModel()
# g.text_editor()
# print(len(g.word_list))
# g.build_model()
# string = g.best_combination()
# print(string)
g.create_story()



