class NonStandardInputFileError(Exception):
    def __init__(self, message="Input file is not standard"):
        self.message = message
        super().__init__(self.message)