                    self.gen_code(i, self.valiables)
                    f = open('test.txt','r')
                    string = f.read()
                    print(string)
                    if string in previous:
                        print("succeed")
                    else:
                        previous.append(string)
                    print("previous = {}".format(previous))
                    f.close()
                    self.mode = 0