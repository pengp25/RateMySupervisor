import json
import requests
from multiprocessing import Pool
import time
from numpy import average
import pickle

url_comment = r'https://www.urfire.com/tutor/api/comments'
url_teacher = r'https://www.urfire.com/tutor/api/teacher'

def get_teacher_data(teacher_id):
    comment_req_data = {
        'teacher_id': teacher_id,
        'state': 1
    }
    teacher_req_data = {
        'id':teacher_id
    }
    try:
        res_comment = requests.get(url=url_comment, params=comment_req_data)
        res_teacher = requests.get(url=url_teacher, params=teacher_req_data)
    except:
        print(f'{teacher_id} skipped')
        return None
    print(f'{teacher_id}')
    comment = res_comment.json()
    teacher = res_teacher.json()
    teacher.update({'comments': comment})
    return teacher

def convert_format():
    with open('data/urfire.json', 'r',encoding='utf8') as f:
        data_list = json.load(f)
    record = {
        'school_cate': '其他',
        'university': '',
        'department': '',
        'supervisor': '',
        'rate': 0,
        'description': '',
        'date': '',
        'counts': 0
    }
    data = []
    for teacher in data_list:
        if teacher:
            if teacher['comments']['count'] != 0:
                
                if teacher['985']==1:
                    record['school_cate'] = '985'
                elif teacher['211']==1:
                    record['school_cate'] = '211'
                elif teacher['research_institute'] == 1:
                    record['school_cate'] = '研究机构'
                elif teacher['country'] != None:
                    record['school_cate']=teacher['country']
                else:
                    record['school_cate'] = '其他'
                record['university'] = teacher['school_name']
                record['department'] = '无' if not teacher['college_name'] else teacher['college_name']
                record['supervisor'] = teacher['name']
                for comment in teacher['comments']['data']:
                    desc = comment['other_desc']
                    record['description'] = desc
                    record['counts'] = len(desc) if desc else 0
                    record['date'] = comment['other_desc_date']
                    scores = ["academic_score", "project_money_score", "relation_score", "future_score"]
                    record['rate'] = average([comment[item] for item in scores])
                    data.append(record.copy())
    return data

if __name__ == '__main__':
    # with Pool(processes=8) as pool:
    #     teacher_list = pool.map(get_teacher_data, range(1, 60800))
    #     with open('../data/urfire_teacher_list.pickle', 'wb') as f:
    #         pickle.dump(teacher_list, f, pickle.HIGHEST_PROTOCOL)
    # with open('../data/urfire.json', 'w',encoding='utf8') as f:
    #     json.dump(teacher_list, f,ensure_ascii=False)
    data = convert_format()
    with open('data/comments_data.json', 'w',encoding='utf8') as f:
        json.dump(data, f,ensure_ascii=False)
    
        