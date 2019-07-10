import argparse


def validate(data):
    data = eval(data)
    print(f'validate origin data: {data}')
    less_data = []
    more_data = []
    for i in data:
        if i > 0:
            more_data.append(i)
        elif i < 0:
            less_data.append(i)
    with open('/less_data.txt', 'w+') as f:
        f.write(str(less_data))
    with open('/more_data.txt', 'w+') as f:
        f.write(str(more_data))
    print(f'more than zero data: {more_data}')
    print(f'less than zero data: {less_data}')


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, required=True, help='input data, ex: [1, -1, 2, 4, -3]')
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    validate(args.data)


if __name__ == '__main__':
    main()
