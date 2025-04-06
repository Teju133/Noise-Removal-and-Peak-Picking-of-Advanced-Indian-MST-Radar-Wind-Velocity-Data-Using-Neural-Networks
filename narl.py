import numpy as np
def read_mst_radar_data(file_path):
    with open(file_path, 'rb') as fid:
        header = np.fromfile(fid, dtype=np.int16, count=64)
        if header.size < 64:
            print("File is too small to contain a valid header.")
            return
        nrgb = header[2] 
        nfft = header[3]  
        d_size = np.int32(nrgb) * np.int32(nfft)  
        fid.seek(0, 0)
        frame_count = 0
        while True:
            x= np.fromfile(fid, dtype=np.int16, count=64)
            x= np.fromfile(fid, dtype=np.int32, count=2 * d_size)
            frame_count += 1
            if x.size < 128:
                break 
            iq_matrix = x.reshape((nrgb, nfft, 2))  
            i_data = iq_matrix[:, :, 0]  
            q_data = iq_matrix[:, :, 1]  
            print(f"Frame {frame_count}:")
            print(f"I Component : {i_data.flatten()[::1]}")
            print(f"Q Component : {q_data.flatten()[::1]}")
            print("-" * 40)
file_path = "C:\\Users\\Hp\\Desktop\\nar\\6JU2024SHT1.r1"
read_mst_radar_data(file_path)