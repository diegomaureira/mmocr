paddleann_textdet_data_root = 'data/paddleann'

paddleann_textdet_train = dict(
    type='OCRDataset',
    data_root=paddleann_textdet_data_root,
    ann_file='textdet_test.json',
    filter_cfg=dict(filter_empty_gt=True, min_size=32),
    pipeline=None)

paddleann_textdet_test = dict(
    type='OCRDataset',
    data_root=paddleann_textdet_data_root,
    ann_file='textdet_test.json',
    test_mode=True,
    pipeline=None)
