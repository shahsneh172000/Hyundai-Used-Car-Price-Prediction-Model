from flask import Flask , request , render_template
import hyundai_model 

app = Flask(__name__)

@app.route("/")
def home():
    var = hyundai_model.l
    return render_template('hyundai_index.html',xyz=var)

@app.route("/hyundai_price",methods=['POST'])
def hyundai_price():
    in_data = [x for x in request.form.values()]

    model = in_data[0]
    year = in_data[1]
    mileage = in_data[2]
    total_run = in_data[3]
    tax = in_data[4]
    engine_size = in_data[5]
    trans = in_data[6]
    fule = in_data[7]

    #return render_template('hyundai_index.html',abc = in_data)
    predict_price = hyundai_model.car_price(year,total_run,tax,engine_size,mileage,model,trans,fule)
    return render_template('predict.html',pred_text = "Predicted Car Price = {} $".format(predict_price),data = in_data)

app.run(debug=True)