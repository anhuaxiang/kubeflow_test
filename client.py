import kfp
from kubernetes import client as k8s_client
from kfp import gcp, dsl, notebook, compiler

client = kfp.Client()
EXPERIMENT_NAME = 'usr1'
exp = client.create_experiment(name=EXPERIMENT_NAME)


class validateOp(dsl.ContainerOp):
    """对文件中的数据进行验证"""

    def __init__(self, output_dir, inputFilename):
        super(validateOp, self).__init__(
            name='validate_number',
            image='anhuaxiang/validate:0.5',
            arguments=[
                '--inputFilename', inputFilename,
                '--output_dir', output_dir,
            ],
            file_outputs={
                'more': '/moreFilePath.txt',
                'less': '/lessFilePath.txt',
            })


class MoreThanZeroOp(dsl.ContainerOp):
    """handle the number more than zero"""

    def __init__(self, output_dir, data):
        super(MoreThanZeroOp, self).__init__(
            name='MoreThanZero',
            image='anhuaxiang/more:0.5',
            arguments=[
                '--output_dir', output_dir,
                '--data', data,
            ])


class LessThanZeroOp(dsl.ContainerOp):
    """handle the number less than zero"""

    def __init__(self, output_dir, data):
        super(LessThanZeroOp, self).__init__(
            name='LessThanZero',
            image='anhuaxiang/less:0.5',
            arguments=[
                '--output_dir', output_dir,
                '--data', data,
            ])


@dsl.pipeline(
    name='Testpipelines',
    description='shows how to define dsl.Condition.'
)
def validate_test():
    output_dir = '/home/yan/nfs'
    inputFilename = '/home/yan/nfs/a.txt'
    validate = validateOp(output_dir, inputFilename).add_volume(k8s_client.V1Volume(name='usr-pv',
                                                                                    nfs=k8s_client.V1NFSVolumeSource(
                                                                                        path='/home/yan/nfs',
                                                                                        server='192.168.59.128'))).add_volume_mount(
        k8s_client.V1VolumeMount(mount_path='/home/yan/nfs', name='usr-pv'))
    moreThanZero = MoreThanZeroOp(output_dir, validate.outputs['more']).add_volume(k8s_client.V1Volume(name='usr-pv',
                                                                                                       nfs=k8s_client.V1NFSVolumeSource(
                                                                                                           path='/home/yan/nfs',
                                                                                                           server='192.168.59.128'))).add_volume_mount(
        k8s_client.V1VolumeMount(mount_path='/home/yan/nfs', name='usr-pv'))

    lessThanZero = LessThanZeroOp(output_dir, validate.outputs['less']).add_volume(k8s_client.V1Volume(name='usr-pv',
                                                                                                       nfs=k8s_client.V1NFSVolumeSource(
                                                                                                           path='/home/yan/nfs',
                                                                                                           server='192.168.59.128'))).add_volume_mount(
        k8s_client.V1VolumeMount(mount_path='/home/yan/nfs', name='usr-pv'))


compiler.Compiler().compile(validate_test, 'test.tar.gz')
run = client.run_pipeline(exp.id, 'usr', 'test.tar.gz')
