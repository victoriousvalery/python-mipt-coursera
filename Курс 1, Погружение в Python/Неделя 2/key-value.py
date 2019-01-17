import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--value")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if not os.path.isfile(storage_path):
    f = open(storage_path, 'w')
    f.close()

if args.key and not args.value:  # чтение. передан только ключ без значения
    data_read = None
    with open(storage_path, 'r') as f:
        try:
            data_read = json.loads(f.read())
        except:
            print(None)
        else:
            if args.key in data_read.keys() and data_read:
                data_read = data_read[args.key]
                data_read = set(data_read)
                output_string = ", ".join(data_read)
                print(output_string)
            else:
                print(None)

elif args.key and args.value:  # запись. переданы и ключ, и значение
    data = None
    data_write = None
    args_write = None
    with open(storage_path, 'r') as f:  # надо прочитать предварительно, потому что иначе перезапишется файл
        if not f.read() == "":
            f.seek(0)
            data = json.loads(f.read())
    with open(storage_path, 'w') as f:
        if data:
            if args.key in data.keys() and args.value not in data.values():
                data[args.key].append(args.value)
                f.write(json.dumps(data))
            elif args.key not in data.keys() and args.value not in data.values():
                args_write = {args.key: [args.value]}
                data_write = dict(list(data.items())+list(args_write.items()))
                f.write(json.dumps(data_write))
        else:
            f.write(json.dumps({args.key: [args.value]}))