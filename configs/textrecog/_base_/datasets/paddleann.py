paddleann_textrecog_data_root = 'data/paddleann'

paddleann_textrecog_train = dict(
    type='OCRDataset',
    data_root=paddleann_textrecog_data_root,
    ann_file='textrecog_test.json',
    pipeline=None)

paddleann_textrecog_test = dict(
    type='OCRDataset',
    data_root=paddleann_textrecog_data_root,
    ann_file='textrecog_test.json',
    test_mode=True,
    pipeline=None)
