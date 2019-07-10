import argparse


def less_than_zero(data):
    data = eval(data)
    data_sum = 0
    for f in data:
        data_sum += f * f
    print(f'less than zero result: {data_sum}')


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, required=True, help='data')
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    less_than_zero(args.data)


if __name__ == '__main__':
    main()
