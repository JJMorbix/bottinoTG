class StringReader:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(StringReader, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):  # Avoid reinitializing if already done
            self.initialized = True
            self._file_cache = {}  # Cache to store previously read files

    def read(self, file_path):
        # Return cached content if file has already been read
        if file_path in self._file_cache:
            return self._file_cache[file_path]
        try:
            with open("data/strings/" + file_path + ".txt", 'r') as file:
                content = file.read()
            # Cache the content for future reads
            self._file_cache[file_path] = content
            return content
        except FileNotFoundError:
            return f"Error: The file at {file_path} was not found."
        except IOError as e:
            return f"Error reading the file: {e}"

    def parse(self, string, tag, value):
        return string.replace("{{" + tag + "}}", value)