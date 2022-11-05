from flask import Flask, render_template, request
import SQL_Control_Functions as SCF
mydb = SCF.connect_server("localhost", "Shambhu Kaka", "shree_123", "Test")

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")



@app.route("/BankOptions", methods=["post", "get"])
def BankOptions():
    output = request.form.to_dict()
    name = output["name"]
    DOB = SCF.GetDate(mydb, name)
    global name0
    name0 = name
    global DOB0
    DOB0=DOB
    print(name0)

    return render_template("BankOptions.html", name = name)

@app.route("/Deposit", methods=["post", "get"])
def Deposit():
    print(name0)
    return render_template("Deposit.html")
     
    

@app.route("/SuccessfulTransaction", methods=["post", "get"])
def SuccessfulTransaction():
    output = request.form.to_dict()
    bmount = int(output["amount"])
    print(name0)
    command = str(f"update Account set balance = {bmount} where name = '{name0}';")
    SCF.HTMLTrialDeposit(mydb, command)
    render_template("successful_transaction.html", amount = bmount)
    return render_template("BankOptions.html", name = name0, DOB=DOB0)


@app.route("/login", methods=["post", "get"])
def login():
    return render_template("login.html")

@app.route("/create", methods=["post", "get"])
def create():
    return render_template("create.html")

@app.route("/acc_created", methods=["post", "get"])
def acc_created():
    output = request.form.to_dict()
    name = output["name"]
    global name0
    name0 = name
    print(name0)
    DOB = output["Date_of_Birth"]
    SCF.HTMLTrailAdd(mydb, name, DOB)
    return render_template("acc_created.html", name=name, DOB=DOB)


@app.route("/Withdraw", methods=["pst", "get"])
def withdraw():
    return render_template("withdraw.html")
    


if __name__ == '__main__':
    app.run(debug=True, port=8000)
