import PyQt5, time, logging
import geo_polygons
import mission_simulate

def parse_kml(kml_str):
    points_str = kml_str.strip().split(' ')
    points = []
    for point_str in points_str:
        lon, lat, height = point_str.strip().split(',')
        lon, lat = float(lon), float(lat)
        points.append((lon, lat))
    return points


def create_mid_term_experiment(rc):
    rc.gis_canvas.zoom_to_polygon(geo_polygons.Polygons.aoxiang_fly_round['vertex'], geo_polygons.Polygons.aoxiang_fly_round['geo_ref'])
    mm = rc.mission_manager
    #mm.add_area('生态监测区（区域1）', [(117.4063, 39.5660), (117.4139, 39.5565), (117.4022, 39.5526), (117.3976, 39.5624)])
    #mm.add_area('生态监测区（区域1）', parse_kml(
      #'117.3491379572283,39.48294753602178,0 117.4682815990997,39.4768342897785,0 117.4073868950992,39.57253199053769,0 117.3921564836651,39.56987558402626,0 117.401568354145,39.54819851183547,0 117.3340229206388,39.53991091692195,0 117.3491379572283,39.48294753602178,0'
    #))
    #mm.add_area('宝坻区域1', parse_kml(
      #'117.3491379572283,39.48294753602178,0 117.4682815990997,39.4768342897785,0 117.4073868950992,39.57253199053769,0 117.3921564836651,39.56987558402626,0 117.401568354145,39.54819851183547,0 117.3340229206388,39.53991091692195,0 117.3491379572283,39.48294753602178,0'
     #))
    #mm.add_area('水域观测区（区域1）', [(117.3997, 39.5627), (117.4087, 39.5670), (117.4152, 39.5586), (117.4061, 39.5542)])
    #mm.add_area('水域观测区（区域2）', [(117.4006, 39.5637), (117.4006, 39.5562), (117.4201, 39.5562), (117.4201, 39.5637)])#原来的观测区域
    mm.add_area('联调空域', [(117.39780278,39.576355556), (117.4441638889, 39.55281388889), (117.4218805556,39.530930556), (117.3799472222, 39.552422222)])
    #mm.add_area('验证场全场', [(117.377495586,39.55726334894), (117.391738266954, 39.56096469166), (117.3998998,39.5441836896954), (117.386137212664, 39.540481451649)])
    #mm.add_area('验证场（潮白河）', [(117.4052608123,39.56614623955785), (117.41070183647965, 39.567873336), (117.418863372731,39.553191643925), (117.413582378686, 39.551587573279534)])
    #mm.add_area('验证场（基地）', [(117.3903780109,39.56133481506568), (117.41070183647965, 39.56688642908), (117.4142224991763,39.56096469166255), (117.39325855311883, 39.55553598815341)])
    #mm.add_area('双波段（单双机）', [(117.40016538984737,39.56081454296114), (117.40330469488843, 39.562208002839625), (117.4072526088,39.5566339953), (117.4041133037, 39.5552404234)])
    #mm.add_area('双波段（单双机）', [(117.40016538984737,39.56081454296114), (117.40330469488843, 39.562208002839625), (117.4072526088,39.5566339953), (117.4041133037, 39.5552404234)])
    #mm.add_area('双波段（单双机）', [(117.40016538984737,39.56081454296114), (117.40330469488843, 39.562208002839625), (117.4072526088,39.5566339953), (117.4041133037, 39.5552404234)])
    #mm.add_area('光学相机（单双，四机）', [(117.40030808553104,39.559861106912784), (117.40473165172526, 39.56180463575405), (117.40853686995683,39.55659732275688), (117.40392304285102, 39.55465364799791)])
    mm.add_area('1号协同', [(117.399629,39.565379), (117.405638, 39.567696), (117.410062,39.561315), (117.403836, 39.559096)])
    mm.add_area('3号协同', [(117.399629,39.565379), (117.405638, 39.567696), (117.410062,39.561315), (117.403836, 39.559096)])
    mm.add_area('6号协同', [(117.399629,39.565379), (117.405638, 39.567696), (117.410062,39.561315), (117.403836, 39.559096)])
    mm.add_area('5号协同', [(117.40114,39.56608455674), (117.405540865, 39.567688292), (117.4150626573,39.554055359), (117.410741844, 39.5523279)])
    mm.add_area('9号协同', [(117.399629,39.565379), (117.405638, 39.567696), (117.410062,39.561315), (117.403836, 39.559096)])
    mm.add_area('2号协同', [(117.405554,39.556351), (117.412209, 39.558207), (117.415775,39.551760), (117.409075, 39.549869)])
    mm.add_area('4号协同', [(117.405554,39.556351), (117.412209, 39.558207), (117.415775,39.551760), (117.409075, 39.549869)])
    mm.add_area('7号协同', [(117.405554,39.556351), (117.412209, 39.558207), (117.415775,39.551760), (117.409075, 39.549869)])
    mm.add_area('8号协同', [(117.405554,39.556351), (117.412209, 39.558207), (117.415775,39.551760), (117.409075, 39.549869)])
    mm.add_area('10号协同', [(117.405554,39.556351), (117.412209, 39.558207), (117.415775,39.551760), (117.409075, 39.549869)])
    mm.add_fly_mission_to_area({
        'area_name': '生态监测区（区域1）',
        'mission_name': '植被覆盖提取生态观测任务_可见光',
        'aerocraft': '猛牛-轻小型固定翼无人机（绿色）',
        'cameras': '光学相机（照片）',
        'ground_resolution_m': 0.1,
        'forward_overlap': 0.5,
        'sideway_overlap': 0.3,
        'fly_direction': 'longest_edge',
        'application': '大尺度生态应用(中期实验)',
        'aerocraft_num': 1,
        'board_region_name': '无限制',
    })
    mm.add_fly_mission_to_area({
        'area_name': '水域观测区（区域1）',
        'mission_name': '水域提取_Sar',
        'aerocraft': '猛牛-轻小型固定翼无人机(搭载sar)',
        'cameras': 'minisar',
        'ground_resolution_m': 0.1,
        'forward_overlap': None,
        'sideway_overlap': 0.2,
        'fly_direction': 'longest_edge',
        'application': '中尺度洪涝应用(中期实验)',
        'aerocraft_num': 1,
        'board_region_name': '翱翔5km圆',
    })


g_last_execute_time = None
def generate_files(rc):
    global g_last_execute_time
    if g_last_execute_time and time.time() - g_last_execute_time < 1.:
        return

    generate_dir = PyQt5.QtWidgets.QFileDialog.getExistingDirectory(rc.main_window, '选取文件夹', './')
    version = 'v2'

    for area in rc.mission_manager.areas.values():
        for mission in area.missions.values():
            text = mission.to_text()
            filename = '%s/%s_%s.json' % (generate_dir, version, mission.name)
            f = open(filename, 'w')
            f.write(text)
            f.close()
            print('write to %s' % filename)

    g_last_execute_time = time.time()

def show_wpt_routes(rc):
    global g_last_execute_time
    if g_last_execute_time and time.time() - g_last_execute_time < 1.:
        return

    filenames, _ = PyQt5.QtWidgets.QFileDialog.getOpenFileNames(rc.main_window, '请选择航迹文件', './', "WPT Files (*.wpt);;All Files (*)")
    routes = []
    for wptfile in filenames:
        try:
            f = open(wptfile, 'r')
            point_num = int(f.readline().strip().split(',')[0])
            coors = []
            for i_point in range(point_num):
                line = f.readline().strip().split(',')
                lon, lat = float(line[1]), float(line[2])
                coors.append((lon, lat))
            routes.append(coors)
            rc.mission_manager.create_route_simulations(wptfile, coors)
        except Exception as e:
            logging.exception(e)
    
    for route in routes:
        mission_simulate.Polyline_Simulation(rc, route, need_judge_if_mission_exist=False).begin()

    g_last_execute_time = time.time()