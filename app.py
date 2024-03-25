from flask import Flask, render_template, request, jsonify
from neo_db.query_graph import query,queryf2
import json
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index(name=None):
    return render_template('index.html', name = name)

@app.route('/a', methods=['GET', 'POST'])
def a(name=None):
    return render_template('a.html', name = name)

@app.route('/echart', methods=['GET', 'POST'])
def echart(name=None):
    return render_template('echart.html', name = name)

@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')

@app.route('/getIndustryInfoList', methods=['GET'])
def getIndustryInfoList():
    companyName = request.args.get("companyName")
    with open("scripts/info.json", encoding='utf-8') as f:
        data = json.load(f)
    print(data)
    print(type(data))
    print(data.get(companyName))
    return data.get(companyName, [])
    


@app.route('/KGQA', methods=['GET', 'POST'])
def KGQA():
    return render_template('KGQA.html')


@app.route('/get_profile',methods=['GET','POST'])
# def get_profile():
#     name = request.args.get('character_name')
#     json_data = get_answer_profile(name)
#     return jsonify(json_data)

@app.route('/KGQA_answer', methods=['GET', 'POST'])

@app.route('/search_name', methods=['GET', 'POST'])
def search_name():
    # # 显示只有一阶邻居：
    # name = request.args.get('name')
    # json_data=query(str(name))
    # return jsonify(json_data)

    # # 显示包含二阶邻居：
    name = request.args.get('name')
    json_data = queryf2(str(name))
    return jsonify(json_data)

@app.route('/get_all_relation', methods=['GET', 'POST'])
def get_all_relation():
    return render_template('all_relation.html')

if __name__ == '__main__':
    app.debug=True
    app.run()
