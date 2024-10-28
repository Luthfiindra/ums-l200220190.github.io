from metaflow import FlowSpec, step

class HelloWorldFlow(FlowSpec):
    @step
    def start(self):
        print("This is the start step!")
        self.next(self.hello)

    @step
    def hello(self):
        print("Hello, World!")
        self.next(self.end)

    @step
    def end(self):
        print("This is the end step!")

if __name__ == '__main__':
    HelloWorldFlow()