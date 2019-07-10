import kfp
from kubernetes import client as k8s_client
from kfp import gcp, dsl, notebook, compiler


EXPERIMENT_NAME = 'usr1'
# client = kfp.Client()
# exp = client.create_experiment(name=EXPERIMENT_NAME)


class ValidateOp(dsl.ContainerOp):

    def __init__(self, data):
        super(ValidateOp, self).__init__(
            name='validate_number',
            image='anhuaxiang/validate:0.1',
            arguments=[
                '--data', data,
            ],
            file_outputs={
                'more': '/more_data.txt',
                'less': '/less_data.txt',
            })


class MoreThanZeroOp(dsl.ContainerOp):

    def __init__(self, data):
        super(MoreThanZeroOp, self).__init__(
            name='MoreThanZero',
            image='anhuaxiang/more:0.1',
            arguments=[
                '--data', data,
            ])


class LessThanZeroOp(dsl.ContainerOp):
    def __init__(self, data):
        super(LessThanZeroOp, self).__init__(
            name='LessThanZero',
            image='anhuaxiang/less:0.1',
            arguments=[
                '--data', data,
            ])


@dsl.pipeline(
    name='test_pipelines',
    description='shows how to define dsl.Condition.'
)
def validate_test():
    data = '[1, -1, 2, -4, 4, 8, -1]'
    validate = ValidateOp(data)
    moreThanZero = MoreThanZeroOp(validate.outputs['more'])
    lessThanZero = LessThanZeroOp(validate.outputs['less'])


compiler.Compiler().compile(validate_test, 'test.tar.gz')
# run = client.run_pipeline(exp.id, 'usr', 'test.tar.gz')
