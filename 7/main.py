from __future__ import annotations

import typing


class FileSystemObjectHolder:
    def __init__(self) -> None:
        self.content: list[Directory | File] = []
        self.size: int = 0

    def add_content(self, content: FileSystemObjectHolder | File) -> None:
        for obj in self.content:
            if obj.name == content.name:
                raise Exception(f"File or folder with name {content.name} already exists.")
        content.parent = self
        self.content.append(content)
        if hasattr(content, "size"):
            self.change_size(content.size)

    def change_size(self, change: int) -> None:
        self.size += change
        if hasattr(self, "parent"):
            self.parent.change_size(change)


class FileSystemRoot(FileSystemObjectHolder):
    def __init__(self) -> None:
        super().__init__()
        self.name = "/"


class FileSystemObject:
    def __init__(self, name: str, parent: FileSystemObjectHolder) -> None:
        self.name: str = name
        self.parent: FileSystemObjectHolder = parent


class Directory(FileSystemObject, FileSystemObjectHolder):
    def __init__(self, name: str, parent: FileSystemObjectHolder) -> None:
        FileSystemObject.__init__(self, name, parent)
        FileSystemObjectHolder.__init__(self)


class File(FileSystemObject):
    def __init__(self, name: str, parent: FileSystemObjectHolder, size: int) -> None:
        super().__init__(name, parent)
        if size is not None:
            self.size = size


class FileSystem:
    def __init__(self, size: int = 0) -> None:
        self._root: FileSystemRoot = FileSystemRoot()
        self._cwd: FileSystemObjectHolder = self._root
        self.total: int = size

    def cd(self, d: str) -> None:
        if d == "/":
            self._cwd = self._root
        elif d == "..":
            self._cwd = self._cwd.parent
        else:
            for obj in self._cwd.content:
                if obj.name == d:
                    self._cwd = obj

    def cwd(self) -> FileSystemObjectHolder:
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

    def free(self) -> int:
        return self.total - self._root.size


def process_ls(file_system: FileSystem, f: typing.TextIO) -> None:
    while True:
        pos: int = f.tell()
        line: str = f.readline()
        if line and line[0] != "$":
            words: list = line.split()
            cwd: FileSystemObjectHolder = file_system.cwd()
            if words[0] == "dir":
                cwd.add_content(Directory(words[1], cwd))
            else:
                size: int = int(words[0])
                filename: str = words[1]
                cwd.add_content(File(filename, cwd, size))
        else:
            f.seek(pos)
            break


def main(file_name: str) -> tuple[int, int]:
    file_system: FileSystem = FileSystem(size=70000000)
    with open(file_name) as f:
        while True:
            line: str = f.readline()
            if not line:
                break
            line = line.strip()
            if line[0] == "$":
                args: list = line[2:].split(" ", 1)
                cmd: str = args.pop(0)
                if cmd == "cd":
                    file_system.cd(args[0])
                elif cmd == "ls":
                    process_ls(file_system, f)
    part1: int = 0
    file_system.cd("/")
    free_space: int = file_system.free()
    part2: int = file_system.total
    for d in file_system.find(d=None, dirs_only=True):
        if d.size < 100000:
            part1 += d.size
        if d.size < part2 and free_space + d.size > 30000000:
            part2 = d.size

    return part1, part2


if __name__ == '__main__':
    print(main('input.txt'))
