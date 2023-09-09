from random import randint, choice


class FileOperations:
    def write_content_to_file(self, content, filename):
        """Write given content to a file."""
        with open(filename, 'wb') as f:
            f.write(bytes((int(i, 16) for i in content)))

    def __init__(self):
        self.hex_digits = '0123456789abcdef'
        self.header_size = 1000

    def randomize_content(self, content, random_chance):
        for i in range(self.header_size, len(content)):
            if randint(0, random_chance) == 1:
                content[i] = choice(self.hex_digits)
        return content
