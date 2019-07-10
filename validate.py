import argparse
import os


def validate(output_dir, filename):
    f = open(filename, 'rb+')
    lessOutput_path = os.path.join(output_dir, 'lessThanZero.txt')
    f1 = open(lessOutput_path, 'w')

    moreOutput_path = os.path.join(output_dir, 'moreThanZero.txt')
    f2 = open(moreOutput_path, 'w')
    lines = f.readlines()
    for line in lines:
        num = int(line)
        if num > 0:
            f1.write(str(num) + "\n")
        elif num < 0:
            f2.write(str(num) + "\n")
    f.close()
    f1.close()
    f2.close()
    with open('/lessFilePath.txt', 'w+') as f:
        f.write(lessOutput_path)
    with open('/moreFilePath.txt', 'w+') as f:
        f.write(moreOutput_path)


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputFilename', type=str, required=True, help='local file to be input')
    parser.add_argument('--output_dir', type=str, required=True, help='local file to be input')
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    validate(args.output_dir, args.inputFilename)


if __name__ == '__main__':
    main()