class Datasaver:
    def __init__(self, path):
        self.path = path
        self.dict = []

        # open the file at the path
        with open(self.path, 'r') as file:
            # index each variable so we can access it later
            lines = file.readlines()
            for line in lines:
                self.dict.append(line.split("|")[0])

    def has_data(self):
        return len(self.dict) != 0

    def has_variable(self, name):
        return name in self.dict

    def change_variable(self, name, value):
        if self.has_variable(name):
            file_data_arr = []
            to_write = ""
            with open(self.path, 'r') as file:
                file_data_arr = file.read().split("\n")

            for line in file_data_arr:
                if line.split("|")[0] == name:
                    to_write += name + "|" + str(value) + "\n"
                else:
                    to_write += line + "\n"

            with open(self.path, 'w') as file:
                file.write(to_write)

    # creates a variable in the saved data file
    def create_variable(self, name, value, type):
        if not self.has_variable(name):
            with open(self.path, 'a') as file:
                if type == "string" or type == "int" or type == "boolean":
                    file.write("\n" + name + "|" + str(value))
                elif type == "array":
                    to_write = ""
                    for element in value:
                        to_write += str(element)
                        if element != value[len(value) - 1]:
                            to_write += ","
                    file.write("\n" + name + "|" + to_write)
                self.dict.append(name)

    def delete_variable(self, name):
        if self.has_variable(name):
            file_data_arr = []
            to_write = ""
            with open(self.path, 'r') as file:
                file_data_arr = file.read().split("\n")

            for line in file_data_arr:
                if line.split("|")[0] != name:
                    to_write += "\n" + line

            with open(self.path, 'w') as file:
                file.write(to_write)

    def get_variable(self, name, type):
        if self.has_variable(name):
            var_as_string = ""
            with open(self.path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if line.split("|")[0] == name:
                        var_as_string = line.split("|")[1].replace("\n", "")

            if type == "int":
                return int(var_as_string)
            elif type == "string":
                return var_as_string
            elif type == "boolean":
                return bool(var_as_string)
