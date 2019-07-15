import json
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
    static_html_path = '/aaa.html'
    with open(static_html_path, 'w') as f:
        f.write("""
            <!DOCTYPE html>
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>Pipeline</title>
                </head>
                <body>
                    <h1>pipeline output</h1>
                    <p>pipeline output web</p>
                </body>
            </html>
        
        """)

    metadata = {
        'outputs': [{
            'type': 'web-app',
            'storage': 'gcs',
            'source': static_html_path,
        }]
    }
    with open('/mlpipeline-ui-metadata.json', 'w') as f:
        json.dump(metadata, f)


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
