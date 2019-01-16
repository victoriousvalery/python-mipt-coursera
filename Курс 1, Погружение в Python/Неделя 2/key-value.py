import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--value")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'w+') as f:
    if args.key and not args.value:  # чтение. передан только ключ без значения
        pass
    elif args.key and args.value:  # запись. переданы и ключ, и значение
        f.write(json.dumps({args.key: args.value}))
    print(f.read())