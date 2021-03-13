# -*- coding: utf-8 -*-

import hashlib
import sys
import os


def find_file(file_name, folder):
    for element in os.scandir(folder):
        if element.name == file_name:
            return True


def hash_sum_file(file_path, algorithm):
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as check_file:
        while True:
            data = check_file.read(60000)
            if not data:
                break
            md5.update(data)
            sha1.update(data)
            sha256.update(data)
    if algorithm == 'md5':
        return md5.hexdigest()
    elif algorithm == 'sha1':
        return sha1.hexdigest()
    elif algorithm == 'sha256':
        return sha256.hexdigest()
    else:
        return


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Must to use 3 arguments: run_file, path_input_file, path_to_check_files")
        sys.exit()
    else:
        path_input_file = sys.argv[1]
        path_to_check_files = sys.argv[2]
        if path_to_check_files[-1] != '/':
            path_to_check_files += '/'

        with open(path_input_file, 'r', encoding='utf-8') as filename:
            for line in filename.readlines():
                if len(line.split()) == 3:
                    j = line.split(' ')
                    filename, algorithm, hash = j[0], j[1], j[2][:-1]
                    if find_file(filename, path_to_check_files):
                        hash_sum = hash_sum_file(path_to_check_files + filename, algorithm)
                        if hash_sum:
                            if hash == hash_sum:
                                print(filename, "OK")
                            else:
                                print(filename, "FAIL")
                        else:
                            print(f'{filename} {algorithm} NOT SUPPORT. MUST BE USE MD5, SHA1 OR SHA256')
                    else:
                        print(filename, 'NOT FOUND')
                else:
                    print('WRONG INPUT DATA')
