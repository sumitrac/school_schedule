class Student:
    def __init__(self, name, grade, classlist):
        self.name = name
        self.grade = grade
        self.classlist = classlist 

    def add_class(self, new_class):
        self.classlist.append(new_class)
        return self.classlist 
    
    def get_num_class(self):
        return len(self.classlist)



#happy case -> #
#sad case
#Bad input in any of the parameters, name, grade, classlist(if its emppty, dictionary, set, tuple, if any of the items in the data structure or not strings, (so if they're int or float)

#what would be the test of def get_num_class
