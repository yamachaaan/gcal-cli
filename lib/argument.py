class Argument():
    def get_argument(self):
        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument('function', help='function call: day,week,2week,month')
        args = parser.parse_args()
        return args
