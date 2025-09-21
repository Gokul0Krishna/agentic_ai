from langchain.memory import ConversationBufferMemory

class CustomMemory(ConversationBufferMemory):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_path = None   # extra variable

    def save_file_path(self, path: str):
        self.file_path = path

    def load_memory_variables(self, inputs):
        """Include both conversation + file_path in memory"""
        base_memory = super().load_memory_variables(inputs)
        base_memory["file_path"] = self.file_path
        return base_memory
