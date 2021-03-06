# coding:utf-8
import mission_planning, json, sys

testdata = {
    'area_points_list': [(30, 30), (30, 30.01), (30.01, 30.01), (30.01, 30)],
    'mission_name': 'mission1',
    'aerocraft': '猛牛-轻小型固定翼无人机',
    'camera': '大视场立体测绘相机',
    'ground_resolution_m': 0.05,
    'forward_overlap': 0.4,
    'sideway_overlap': 0.6,
    'fly_direction_degree': 0,
    'application': 'flood',
    'aerocraft_num': 3,
    'board_region':None,
    'board_region_max_fly_height_m':1000,
}

def plan(input_):
    succ, res = mission_planning.mission_planning(
        area_points_list=input_['area_points_list'],
        mission_name=input_['mission_name'],
        aerocraft=input_['aerocraft'],
        camera=input_['camera'],
        ground_resolution_m=input_['ground_resolution_m'],
        forward_overlap=input_['forward_overlap'],
        sideway_overlap=input_['sideway_overlap'],
        fly_direction_degree=input_['fly_direction_degree'],
        aerocraft_num=input_['aerocraft_num'],
        application=input_['application'],
        board_region=input_['board_region'],
        board_region_max_fly_height_m=input_['board_region_max_fly_height_m'],
    )
    if succ:
        print (json.dumps(res).replace(' ', ''))
    else:
        print ('failed')
        print(res)

def print_test_data():
    print (json.dumps(testdata).replace(' ', ''))

def test():
    plan(testdata)

def main(input_):
    input_ = json.loads(input_)
    plan(input_)

if __name__ == '__main__':
    input_ = sys.argv[1]
    if input_ == 'test':
        test()
    elif input_ == 'print_test_data':
        print_test_data()
    else:
        main(input_)