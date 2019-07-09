# coding=utf8

missions = {
    '1号_[中期实验]_SAR1T': {
        'aerocraft_num': 1,
        'application': '中期实验',
        'aerocraft': '翱翔号（白色）',
        'cameras': 'minisar',
        'ground_resolution_m': 0.1,
        'fly_direction': 'longest_edge',
        'forward_overlap': 0.,
        'sideway_overlap': 0.3,
    },
    '5号_[中期实验]_双5T': {
        'aerocraft_num': 1,
        'application': '中期实验',
        'aerocraft': '猛牛-轻小型固定翼无人机（橙色）',
        'cameras': '轻型双波段相机(可见光)',
        'ground_resolution_m': 0.1,
        'fly_direction': 'longest_edge',
        'forward_overlap': 0.,
        'sideway_overlap': 0.3,
    },
    '3号_[中期实验]_RGB3': {
        'aerocraft_num': 1,
        'application': '中期实验',
        'aerocraft': '猛牛-轻小型固定翼无人机（黄色300）',
        'cameras': '光学相机（照片）',
        'ground_resolution_m': 0.1,
        'fly_direction': 'longest_edge',
        'forward_overlap': 0.6,
        'sideway_overlap': 0.5,
    },
    '4号_[中期实验]_RGB4': {
        'aerocraft_num': 1,
        'application': '中期实验',
        'aerocraft': '猛牛-轻小型固定翼无人机（浅绿）',
        'cameras': '光学相机（照片）',
        'ground_resolution_m': 0.1,
        'fly_direction': 'longest_edge',
        'forward_overlap': 0.6,
        'sideway_overlap': 0.5,
    },
    '2号_[中期实验]_RGB2': {
        'aerocraft_num': 1,
        'application': '中期实验',
        'aerocraft': '猛牛-轻小型固定翼无人机（深绿）',
        'cameras': '光学相机（照片）',
        'ground_resolution_m': 0.1,
        'fly_direction': 'longest_edge',
        'forward_overlap': 0.6,
        'sideway_overlap': 0.5,
    },
    '6号_[中期实验]_RGB6': {
        'aerocraft_num': 1,
        'application': '中期实验',
        'aerocraft': '海豚-轻小型固定翼无人机（浅蓝）',
        'cameras': '光学相机（照片）',
        'ground_resolution_m': 0.1,
        'fly_direction': 'longest_edge',
        'forward_overlap': 0.8,
        'sideway_overlap': 0.5,
    },
    '7号_[中期实验]_RGB7': {
        'aerocraft_num': 1,
        'application': '中期实验',
        'aerocraft': '海豚-轻小型固定翼无人机（深蓝）',
        'cameras': '光学相机（照片）',
        'ground_resolution_m': 0.1,
        'fly_direction': 'longest_edge',
        'forward_overlap': 0.7,
        'sideway_overlap': 0.5,
    },
    '8号_[中期实验]_RGB8': {
        'aerocraft_num': 1,
        'application': '中期实验',
        'aerocraft': '滑翔机-轻小型固定翼无人机（紫色180）',
        'cameras': '光学相机（照片）',
        'ground_resolution_m': 0.1,
        'fly_direction': 'longest_edge',
        'forward_overlap': 0.75,
        'sideway_overlap': 0.5,
    },
    '9号_[中期实验]_RGB9': {
        'aerocraft_num': 1,
        'application': '中期实验',
        'aerocraft': '滑翔机-轻小型固定翼无人机（棕色）',
        'cameras': '光学相机（照片）',
        'ground_resolution_m': 0.1,
        'fly_direction': 'longest_edge',
        'forward_overlap': 0.75,
        'sideway_overlap': 0.5,
    },
    '3号_[中期实验]_RGB3(协同)': {
        'aerocraft_num': 1,
        'application': '中期实验',
        'aerocraft': '猛牛-轻小型固定翼无人机（黄色280）',
        'cameras': '光学相机（照片）',
        'ground_resolution_m': 0.1,
        'fly_direction': 'longest_edge',
        'forward_overlap': 0.75,
        'sideway_overlap': 0.5,
    },
    '8号_[中期实验]_RGB8(协同)': {
        'aerocraft_num': 1,
        'application': '中期实验',
        'aerocraft': '滑翔机-轻小型固定翼无人机（紫色200）',
        'cameras': '光学相机（照片）',
        'ground_resolution_m': 0.1,
        'fly_direction': 'longest_edge',
        'forward_overlap': 0.75,
        'sideway_overlap': 0.5,
    },
   '[中期实验]_minisar': {
        'aerocraft_num': 0,
        'application': '洪涝',
        'aerocraft': '轻小型固定翼无人机',
        'cameras': 'minisar',
        'ground_resolution_m': 0.1,
        'fly_direction': 0,
        'forward_overlap': 0.,
        'sideway_overlap': 0.3,
    },
    '[中期实验]_大视场立体测绘相机': {
        'aerocraft_num': 0,
        'application': '洪涝',
        'aerocraft': '轻小型固定翼无人机',
        'cameras': '大视场立体测绘相机',
        'ground_resolution_m': 0.1,
        'fly_direction': 0,
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3,
    },
    '[中期实验]_轻型双波段(可见光)': {
        'aerocraft_num': 0,
        'application': '洪涝',
        'aerocraft': '轻小型固定翼无人机',
        'cameras': '轻型双波段相机',
        'ground_resolution_m': 0.1,
        'fly_direction': 0,
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3,
    },
    '[中期实验]_轻型双波段(红外)': {
        'aerocraft_num': 0,
        'application': '洪涝',
        'aerocraft': '轻小型固定翼无人机',
        'cameras': '轻型双波段相机',
        'ground_resolution_m': 0.49,
        'fly_direction': 0,
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3,
    },
    '中尺度_区域1_0.1m_minisar': {
        'aerocraft_num': 0,
        'application': '洪涝',
        'aerocraft': '轻小型固定翼无人机',
        'cameras': 'minisar',
        'ground_resolution_m': 0.1,
        'fly_direction': 0,
        'forward_overlap': 0.,
        'sideway_overlap': 0.3,
    },
    '中尺度_区域1_0.1m_大视场立体测绘相机': {
        'aerocraft_num': 0,
        'application': '洪涝',
        'aerocraft': '轻小型固定翼无人机',
        'cameras': '大视场立体测绘相机',
        'ground_resolution_m': 0.1,
        'fly_direction': 0,
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3,
    },
    '中尺度_区域1_0.1m_可见光': {
        'aerocraft_num': 0,
        'application': '洪涝',
        'aerocraft': '轻小型固定翼无人机',
        'cameras': '轻型双波段相机',
        'ground_resolution_m': 0.1,
        'fly_direction': 0,
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3,
    },
    '中尺度_区域1_0.1m_红外': {
        'aerocraft_num': 0,
        'application': '洪涝',
        'aerocraft': '轻小型固定翼无人机',
        'cameras': '轻型双波段相机',
        'ground_resolution_m': 0.49,
        'fly_direction': 0,
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3,
    },
    '中尺度_区域1_0.1m_广域SAR': {
        'application': '洪涝',
        'aerocraft': '长航时固定翼无人机',
        'aerocraft_num': 0,
        'cameras': '广域SAR',
        'ground_resolution_m': 0.1,
        'fly_direction': 0,
        'forward_overlap': 0.,
        'sideway_overlap': 0.3,
    },
    '大尺度_区域1_10m_高光谱':{
        'aerocraft_num': 1,
        'application': '生态',
        'aerocraft': '轻小型无人机(1)',
        'cameras': '高光谱相机(1)',
        'ground_resolution_m':0.5,
        'fly_direction': 0,
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3, 
    },
    '大尺度_区域1_1m_视频吊舱':{
        'aerocraft_num': 1,
        'application': '生态',
        'aerocraft': '轻小型无人机(1)',
        'cameras': '视频吊舱(1)',
        'ground_resolution_m':1,
        'fly_direction': 0,
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3, 
    },
     '大尺度_区域1_1m_可见光':{
        'aerocraft_num': 1,
        'application': '生态',
        'aerocraft': '轻小型无人机(78)',
        'cameras': '可见光相机(78)',
        'ground_resolution_m':1,
        'fly_direction': 0,
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3, 
    },
      '大尺度_区域1_1m_MiniSAR':{
        'aerocraft_num': 1,
        'application': '生态',
        'aerocraft': '轻小型无人机(1)',
        'cameras': 'MiniSAR(1)',
        'ground_resolution_m':0.1,
        'fly_direction': 0,
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3, 
    },
     '大尺度_区域1_10m_高光谱':{
        'aerocraft_num': 1,
        'application': '生态',
        'aerocraft': '轻小型固定翼无人机(1)',
        'cameras': '高光谱相机(1)',
        'ground_resolution_m':0.5,
        'fly_direction': 0,
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3, 
    },
     '大尺度_区域1_3.5m_偏振相机':{
        'aerocraft_num': 1,
        'application': '生态',
        'aerocraft': '轻小型固定翼无人机(3)',
        'cameras': '偏振光学相机(3)',
        'ground_resolution_m':3.5,
        'fly_direction': 0,
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3, 
    },
    '大尺度_区域1_2.5m_多光谱相机':{
        'aerocraft_num': 1,
        'application': '生态',
        'aerocraft': '轻小型固定翼(2)',
        'cameras': 'MiniSAR(1)+视频吊舱(1)',
        'ground_resolution_m':0.1,
        'fly_direction': 0,
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3, 
    },
    '大尺度_区域1_1m_可见光':{
        'aerocraft_num': 1,
        'application': '生态',
        'aerocraft': '轻小型多旋翼无人机(19)',
        'cameras': '可见光相机(19)',
        'ground_resolution_m':1,
        'fly_direction': 0,
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3, 
    },
    '大尺度_区域1_0.8m_全色':{
        'aerocraft_num': 1,
        'application': '生态',
        'aerocraft': '轻小型多旋翼无人机(4)',
        'cameras': '全色相机(4)',
        'ground_resolution_m':0.8,
        'fly_direction': 0,
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3, 
    },
    '大尺度_区域1_0.8m_全色':{
        'aerocraft_num': 1,
        'application': '生态',
        'aerocraft': '轻小型多旋翼无人机(3)',
        'cameras': '多光谱相机(3)',
        'ground_resolution_m':0.8,
        'fly_direction': 0,
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3, 
    },

    #'小尺度_round3':{
    #    'aerocraft_num': 5,
    #    'application': '国土安全',
    #    'aerocraft': '旋翼无人机',
    #    'cameras': '双波段视频相机',
    #    'ground_resolution_m':0.8,
    #    'fly_direction': 0,
    #    'forward_overlap': 0.6,
    #    'sideway_overlap': 0.3, 
    #},
    #'小尺度_round4':{
    #    'aerocraft_num': 10,
    #    'application': '国土安全',
    #    'aerocraft': '固定翼无人机',
    #    'cameras': '普通视频相机',
    #    'ground_resolution_m':0.8,
    #    'fly_direction': 0,
    #    'forward_overlap': 0.6,
    #    'sideway_overlap': 0.3, 
    #},
    #'小尺度_round6':{
    #    'aerocraft_num': 1,
    #    'application': '国土安全',
    #    'aerocraft': '飞艇',
    #    'cameras': 'Lidar',
    #    'ground_resolution_m':0.8,
    #    'fly_direction': 0,
    #    'forward_overlap': 0.6,
    #    'sideway_overlap': 0.3, 
    #},
}
