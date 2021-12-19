from util.datasaver import Datasaver

datasaver = Datasaver('data/savedata.txt')
datasaver.create_variable("item_ids", [10, 12, 42, 12, 55], "array")