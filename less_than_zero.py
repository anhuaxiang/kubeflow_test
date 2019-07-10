import argparse
import os


def LessThanZero(output_dir, filename):
    f = open(filename, 'rb+')
    output_path = os.path.join(output_dir, 'square.txt')
    f1 = open(output_path, 'w')
    lines = f.readlines()
    for line in lines:
        sum = int(line) * int(line)
        f1.write(str(sum) + "\n")
    f.close()
    f1.close()


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_dir', type=str, required=True, help='local file to be input')
    parser.add_argument('--data', type=str, required=True, help='local file to be input')
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    LessThanZero(args.output_dir, args.data)


if __name__ == '__main__':
    main()
