import argparse


def more_than_zero(data):
    data = eval(data)
    data_sum = 0
    for f in data:
        data_sum += f
    print(f'more than zero result: {data_sum}')


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, required=True, help='data')
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    more_than_zero(args.data)


if __name__ == '__main__':
    main()
