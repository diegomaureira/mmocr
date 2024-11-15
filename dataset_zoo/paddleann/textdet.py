data_root = 'data/paddleann'

test_preparer = dict(
    gatherer=dict(
        type='PairGatherer',
        img_suffixes=['.jpg', '.JPG'],
        rule=[r'img(\d+)\.([jJ][pP][gG])', r'img\1.txt']),
    parser=dict(type='TotaltextTextDetAnnParser'),
    packer=dict(type='TextDetPacker'),
    dumper=dict(type='JsonDumper'),
)
#delete = ['totaltext', 'txt_format', 'annotations']
config_generator = dict(type='TextDetConfigGenerator')
