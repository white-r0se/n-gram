import generate
import train

class Model():
    def __init__(self):
        self.input_dir = None
        self.model = None
        self.prefix = None
        self.length = None
    
    def fit(self, input_dir, model=None):
        self.input_dir = input_dir
        self.model = model
        train.main_train(self)

    def generate(self, prefix=None, length=10):
        self.prefix = prefix
        self.length = length
        generate.main_generate(self)
        
if __name__ == "__main__":
    model = Model()
    model.fit("test.txt", "model.pickle")
    model.generate(["saw", "her"], 10)
