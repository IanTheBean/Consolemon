from util.datasaver import Datasaver

datasaver = Datasaver('data/savedata.txt')
datasaver.change_variable("coins", 120)
datasaver.delete_variable("virus")