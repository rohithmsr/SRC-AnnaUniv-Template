from setup import config, folders
from utils import wavelet_transform, verify_transform

if __name__ == '__main__':
    folders.create_folders()

    wavelet_transform.load_dwt(
        config.TRAIN_SET_PATH, 
        config.VINN_FILES_TRAIN, 
        dwt_columns=['vdd', 'xpd', 'pd', 'vinp', 'vinn'],
        usecols=['process', 'temperature', 'vinn', 'vdd', 'xpd', 'pd', 'vinp']
    )

    wavelet_transform.load_dwt(
        config.TEST_SET_PATH, 
        config.VINN_FILES_TEST, 
        dwt_columns=['vdd', 'xpd', 'pd', 'vinp', 'vinn'],
        usecols=['process', 'temperature', 'vinn', 'vdd', 'xpd', 'pd', 'vinp']
    )

    verify_transform.plot_verify('vdd', 'fastnfastp_3.3V_45.csv')