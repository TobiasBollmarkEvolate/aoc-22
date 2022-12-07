from __future__ import annotations

import typing


class FileSystemObjectHolder:
    def __init__(self):
        self.content: list[Directory | File] = []
        self.size: int = 0

    def add_content(self, content: FileSystemObjectHolder | File):
        for obj in self.content:
            if obj.name == content.name:
                raise Exception(f"File or folder with name {content.name} already exists.")
        content.parent = self
        self.content.append(content)
        if hasattr(content, "size"):
            self.change_size(content.size)

    def change_size(self, change: int):
        self.size += change
        if hasattr(self, "parent"):
            self.parent.change_size(change)


class FileSystemRoot(FileSystemObjectHolder):
    def __init__(self):
        super().__init__()
        self.name = "/"


class FileSystemObject:
    def __init__(self, name: str, parent: FileSystemObjectHolder):
        self.name: str = name
        self.parent: FileSystemObjectHolder = parent


class Directory(FileSystemObject, FileSystemObjectHolder):
    def __init__(self, name: str, parent: FileSystemObjectHolder):
        FileSystemObject.__init__(self, name, parent)
        FileSystemObjectHolder.__init__(self)


class File(FileSystemObject):
    def __init__(self, name: str, parent: FileSystemObjectHolder, size: int):
        super().__init__(name, parent)
        if size is not None:
            self.size = size


class FileSystem:
    def __init__(self):
        self._root = FileSystemRoot()
        self._cwd: [FileSystemRoot | Directory] = self._root

    def cd(self, d: str):
        if d == "/":
            self._cwd = self._root
        elif d == "..":
            self._cwd = self._cwd.parent
        else:
            for obj in self._cwd.content:
                if obj.name == d:
                    self._cwd = obj

    def cwd(self):
        return self._cwd

    def find(self, d: typing.Optional[FileSystemObjectHolder], dirs_only: bool = True) -> list[Directory | File]:
        if not d:
            d = self._cwd
        ret: list[Directory | File] = []
        for obj in d.content:
            if obj.__class__.__name__ == "Directory":
                ret.extend(self.find(obj, dirs_only))
                ret.append(obj)
            else:
                if not dirs_only:
                    ret.append(obj)
        return ret


def process_ls(file_system: FileSystem, f: typing.TextIO):
    while True:
        pos: int = f.tell()
        line: str = f.readline()
        if line and line[0] != "$":
            words: list = line.split()
            cwd = file_system.cwd()
            if words[0] == "dir":
                cwd.add_content(Directory(words[1], cwd))
            else:
                size: int = int(words[0])
                filename = words[1]
                cwd.add_content(File(filename, cwd, size))
        else:
            f.seek(pos)
            break


def main(file_name: str) -> tuple[int, int]:
    file_system = FileSystem()
    with open(file_name) as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            if line[0] == "$":
                args = line[2:].split(" ", 1)
                cmd = args.pop(0)
                if cmd == "cd":
                    file_system.cd(args[0])
                elif cmd == "ls":
                    process_ls(file_system, f)
    part1: int = 0
    file_system.cd("/")
    for d in file_system.find(d=None, dirs_only=True):
        if d.size < 100000:
            part1 += d.size

    return part1, 0


if __name__ == '__main__':
    print(main('input.txt'))
